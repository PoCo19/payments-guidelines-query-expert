import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app import Engine
from research import check_answer_coverage, diversity_select, plan_query, followup_query


class ResearchTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.docs = [
            dict(id='framework', subject='Consent framework', series='Payments', issuer='Authority Alpha', document_type='Directions', circular_number='A1', applicability={'entities':['banks'],'page':1,'quote':'These consent requirements apply to banks.'}),
            dict(id='network', subject='UPI consent operations', series='UPI', issuer='Network Beta', document_type='Circular', circular_number='B1'),
            dict(id='institution', subject='Consent implementation', series='Internal operations', issuer='Institution Gamma', document_type='Internal procedure', circular_number='C1'),
            dict(id='unrelated', subject='Catering services', series='Facilities', issuer='Provider Delta', document_type='Manual', circular_number='D1'),
        ]
        texts = {
            'framework':'# Applicability\nThese consent requirements apply to banks. Participants must obtain customer consent for the service.\n# Exceptions\nConsent rules do not apply to the explicitly exempt test environment.',
            'network':'# UPI consent requirements\nUPI participants must capture customer consent and retain the confirmation before processing the request.',
            'institution':'# Consent implementation\nOperations teams must reconcile consent confirmations every day and investigate missing customer approvals.',
            'unrelated':'Catering services offer meals at midday. Menu preferences depend on seasonal produce and kitchen opening hours.',
        }
        for d in self.docs:
            d.update(availability='converted', product_memberships=[d['series']], issue_date='2025-01-01', source_pdf='https://example.org/'+d['id'], related_circulars=[], page_count=1, source_coverage={'page_count_verified':True})
        self.pages = [dict(document_id=d['id'],source_page=1,text=texts[d['id']],method='fixture',review_status='synthetic_test') for d in self.docs]
        (root/'index.json').write_text(json.dumps(self.docs),encoding='utf-8')
        (root/'all_circular_pages.jsonl').write_text(''.join(json.dumps(p)+'\n' for p in self.pages),encoding='utf-8')
        (root/'feature_rules.json').write_text('[]')
        self.e = Engine(data_dir=root, config=dict(vector_backend='json',embedding_model='',generation_model='test',multi_product=True,chunker_version='clauses-v1',adaptive_retrieval=True,research_enabled=True,reranker_enabled=False,claim_check_enabled=False,context_scope='related',context_char_budget=18000))

    def ask(self, query='UPI consent requirements and exceptions', **kwargs):
        return self.e.answer(dict(query=query,method='bm25',mode='evidence',**kwargs))

    def test_topic_retrieves_any_publisher_without_inferred_product_exclusion(self):
        r = self.ask()
        ids = {s['document_id'] for s in r['sources']}
        self.assertTrue({'framework','network','institution'}.issubset(ids))
        self.assertNotIn('unrelated', ids)
        self.assertEqual(r['retrieval_trace']['query_plan']['product_filter'], None)
        self.assertEqual({s['source_group'] for s in r['sources']},{'authority alpha','network beta','institution gamma'})

    def test_explicit_product_filter_is_hard_boundary(self):
        self.assertEqual({s['document_id'] for s in self.ask(series='UPI')['sources']},{'network'})

    def test_explicit_document_selection_is_respected(self):
        r=self.ask(document_ids=['network'],scope='strict')
        self.assertEqual({s['document_id'] for s in r['sources']},{'network'})

    def test_broad_overview_uses_topic_route(self):
        r=self.ask('Give an overview of UPI consent')
        self.assertEqual(r['retrieval_trace']['route'],'topic')
        self.assertGreater(len({s['document_id'] for s in r['sources']}),1)

    def test_named_summary_keeps_document_coverage_route(self):
        r=self.ask('Summarise selected document', document_ids=['framework'])
        self.assertEqual(r['retrieval_trace']['route'],'summary')
        self.assertTrue(r['retrieval_trace']['document_coverage']['framework']['complete'])

    def test_entity_is_context_not_unverified_exclusion(self):
        r=self.ask(entity='banks')
        self.assertEqual(r['retrieval_trace']['query_plan']['entity'],'banks')
        self.assertTrue(any(s['document_id']=='institution' for s in r['sources']))

    def test_infers_entity_only_from_corpus_labels(self):
        p=plan_query(self.e,'Consent requirements for banks')
        self.assertEqual(p['entity'],'banks')
        self.assertEqual(plan_query(self.e,'Consent requirements for an unknown entity')['entity'],'')
        with self.assertRaises(ValueError):
            plan_query(self.e,'Question',entity=123)

    def test_qualification_survives_section_boundary(self):
        r=self.ask('UPI consent requirements')
        self.assertTrue(any('explicitly exempt' in s['text'] for s in r['sources']))

    def test_coverage_map_is_not_a_completeness_claim(self):
        r=self.ask('UPI consent requirements and deadline')
        c=r['retrieval_trace']['aspect_coverage']
        self.assertEqual(next(x for x in c if x['aspect']=='timing')['status'],'not_located')
        self.assertTrue(r['retrieval_trace']['followup_query'])
        self.assertNotIn('complete',r['retrieval_trace'])

    def test_only_one_followup_search(self):
        with patch.object(self.e,'search',wraps=self.e.search) as search:
            self.ask('UPI consent requirements and deadline')
        self.assertEqual(search.call_count,2)

    def test_simple_query_does_not_add_followup(self):
        with patch.object(self.e,'search',wraps=self.e.search) as search:
            self.ask('UPI consent requirements')
        self.assertEqual(search.call_count,1)

    def test_budget_is_respected(self):
        with patch.dict(self.e.config,context_char_budget=2000):
            r=self.ask()
        self.assertLessEqual(r['retrieval_trace']['evidence_characters'],2000)

    def test_no_publisher_quota_inserts_irrelevant_passages(self):
        candidates=[dict(self.e.parts_by_doc['network'][0],rerank_score=5),dict(self.e.parts_by_doc['unrelated'][0],rerank_score=-20)]
        selected=diversity_select(candidates,self.e.by_id,plan_query(self.e,'UPI consent'))
        self.assertEqual([s['document_id'] for s in selected],['network'])

    def test_duplicate_text_does_not_fill_context(self):
        p=self.e.parts_by_doc['network'][0]
        candidates=[dict(p,id='one'),dict(p,id='two',document_id='institution')]
        self.assertEqual(len(diversity_select(candidates,self.e.by_id,plan_query(self.e,'consent'))),1)

    def test_retrieval_does_not_change_index_fingerprint(self):
        before=json.dumps(self.e.parts,sort_keys=True)
        self.ask()
        self.assertEqual(before,json.dumps(self.e.parts,sort_keys=True))

    def review(self, findings):
        r=self.ask()
        self.e.ollama=lambda *args:dict(response=json.dumps({'findings':findings}))
        return check_answer_coverage(self.e,[dict(text='Consent is required.',sources=['S1'])],r['sources'],r['retrieval_trace']['query_plan'])

    def test_empty_review_does_not_assert_complete(self):
        self.assertEqual(self.review([])['status'],'no_additional_issue_flagged')

    def test_fabricated_review_quotes_fail_closed(self):
        self.assertEqual(self.review([dict(kind='possible_omission',reason='Missing',evidence_ids=['S999.1'])])['status'],'unavailable')

    def test_real_quote_omission_is_retained(self):
        r=self.ask();s=r['sources'][0]
        f=dict(kind='possible_omission',reason='Review this qualification',evidence_ids=[s['citation']+'.1'])
        result=self.review([f]);self.assertEqual(result['status'],'issues_flagged')
        self.assertIn(result['findings'][0]['quotes'][0]['quote'],s['text'])

    def test_conflict_requires_two_valid_passages(self):
        r=self.ask();s=r['sources'][0]
        f=dict(kind='possible_conflict',reason='Conflict',evidence_ids=[s['citation']+'.1'])
        self.assertEqual(self.review([f])['status'],'unavailable')

    def test_generation_receives_plan_and_evidence_map(self):
        calls=[]
        def model(endpoint,payload):
            calls.append(payload)
            prompt=json.loads(payload['prompt'])
            if 'findings' in payload['format']['properties']:
                return dict(response=json.dumps({'findings':[]}))
            source=prompt['evidence'][0]['citation']
            return dict(response=json.dumps(dict(abstain=False,claims=[dict(text='Consent is required.',sources=[source])],layout=[dict(type='paragraph',claim_indices=[1])])))
        self.e.ollama=model
        r=self.e.answer(dict(query='UPI consent requirements',method='bm25',mode='generate'))
        self.assertEqual(len(calls),2)
        self.assertTrue(json.loads(calls[0]['prompt'])['evidence_map'])
        self.assertEqual(r['coverage_check']['status'],'no_additional_issue_flagged')


if __name__=='__main__':
    unittest.main()
