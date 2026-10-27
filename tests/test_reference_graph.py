import copy,json,tempfile,unittest
from pathlib import Path
from types import SimpleNamespace
from reference_graph import build_graph,ReferenceGraph
from scope_guard import collective_attribution_issue
from claim_check import without_inline_citation_markers
from claim_repair import repair_claims
from unittest.mock import Mock


def doc(key,n,series='UPI',**kw):
    return dict(id=key,circular_number=n,series=series,subject=key,availability='converted',**kw)


def page(key,text):return dict(document_id=key,source_page=1,text=text)


class CorpusGraphTests(unittest.TestCase):
    def setUp(self):
        self.docs=[doc('a','115'),doc('b','115B'),doc('other','290'),doc('general','401'),doc('different','115',series='RuPay')]
        self.pages=[page('a','UPI Lite balance ceiling.'),page('b','Refer to OC115. UPI Lite balance ceiling revised.'),
                    page('other','Refer to OC115B for UPI Lite. OC401 governs transaction limits.'),
                    page('general','General UPI transaction limits. UPI Lite has separate conditions.'),page('different','Cards.')]
        self.rules=[dict(id='lite',pattern=r'UPI Lite',label='UPI Lite')]
    def build(self):return build_graph(self.docs,self.pages,self.rules)
    def test_family_does_not_confine_references_or_topics(self):
        g=self.build()
        self.assertTrue(any(e['from_id']=='other' and e['to_id']=='b' for e in g['edges']))
        self.assertEqual({m['document_id'] for m in g['topic_mentions']},{'a','b','other','general'})
        family=next(f for f in g['numbering_families'] if f['document_ids']==['a','b'])
        self.assertIn('not_amendment_proof',family['basis'])
        self.assertTrue(all(e['relation']=='references' for e in g['edges']))
    def test_general_document_remains_without_topic(self):
        self.pages[3]['text']='General framework for all system participants.'
        g=self.build()
        self.assertTrue(any(e['to_id']=='general' for e in g['edges']))
        self.assertFalse(any(m['document_id']=='general' for m in g['topic_mentions']))
    def test_cross_product_topics_need_explicit_name_not_generic_issuer(self):
        rules=[dict(id='cards',label='RuPay cards',pattern='issuer|card',products=['RuPay']),
               dict(id='lite',label='UPI Lite',pattern='UPI Lite',products=['UPI'])]
        d=doc('rbi','REF-1','General',issuer='RBI')
        g=build_graph([d],[page('rbi','An issuer may discuss UPI Lite in general directions.')],rules)
        self.assertEqual([m['topic_id'] for m in g['topic_mentions']],['lite'])
    def test_ambiguous_missing_unavailable_not_silently_resolved(self):
        self.docs += [doc('a-old','115'),doc('unavailable','17',availability_override=True)]
        self.docs[-1]['availability']='no_public_pdf'
        self.pages[1]['text']+=' Refer to OC17 and OC999.'
        g=self.build();refs={e['reference']:e for e in g['edges'] if e['from_id']=='b'}
        self.assertEqual(refs['115']['status'],'ambiguous');self.assertIsNone(refs['115']['to_id'])
        self.assertEqual(refs['17']['status'],'unavailable');self.assertEqual(refs['999']['status'],'missing')
    def test_full_identifier_can_cross_issuer_and_product(self):
        self.docs.append(doc('rbi','RBI/DPSS/2024-25/999','General',issuer='RBI'))
        self.pages[0]['text']+=' Refer to RBI/DPSS/2024-25/999.'
        g=self.build();self.assertTrue(any(e['from_id']=='a' and e['to_id']=='rbi' for e in g['edges']))
    def test_parenthesized_or_hyphenated_suffix_never_links_to_base(self):
        self.pages[2]['text']='Refer to OC115(B), OC115-B and OC.115B. Also OC115-3 is an incomplete identifier.'
        g=self.build();edges=[e for e in g['edges'] if e['from_id']=='other']
        self.assertEqual(sum(e['to_id']=='b' for e in edges),3)
        self.assertFalse(any(e['to_id']=='a' for e in edges))
        self.assertEqual(edges[-1]['status'],'incomplete_identifier')
    def test_candidate_expansion_obeys_filters_and_does_not_follow_topic_alone(self):
        g=self.build();engine=SimpleNamespace(docs=self.docs,pages=self.pages,registry=SimpleNamespace(rules=self.rules),
            parts_by_doc={d['id']:[dict(id=d['id']+':1',document_id=d['id'],text=next(p['text'] for p in self.pages if p['document_id']==d['id']))] for d in self.docs},
            query_terms=lambda text:text.lower().split())
        with tempfile.TemporaryDirectory() as t:
            path=Path(t)/'g.json';path.write_text(json.dumps(g))
            graph=ReferenceGraph(path,engine)
            found=graph.expand('UPI Lite balance',engine.parts_by_doc['a'],lambda key:key!='b')
            self.assertFalse(found)
            found=graph.expand('UPI Lite balance',engine.parts_by_doc['a'],lambda key:True)
            self.assertEqual([p['document_id'] for p,e in found],['b'])
            self.assertNotIn('general',[p['document_id'] for p,e in found])
    def test_cached_pages_reresolve_when_missing_target_arrives(self):
        self.pages[0]['text']+=' Refer to OC999.'
        g=self.build();self.docs.append(doc('new','999'))
        updated=build_graph(self.docs,self.pages,self.rules,g)
        self.assertEqual(updated['summary']['pages_reused'],len(self.pages))
        self.assertTrue(any(e['to_id']=='new' for e in updated['edges']))
        self.pages[0]['text']+=' Changed.'
        changed=build_graph(self.docs,self.pages,self.rules,updated)
        self.assertEqual(changed['summary']['pages_reused'],len(self.pages)-1)
    def test_anchor_offsets_are_exact_and_stale_graph_refused(self):
        g=self.build()
        for e in g['edges']:
            p=next(p for p in self.pages if p['document_id']==e['from_id']);a=e['evidence']
            self.assertEqual(a['quote'],p['text'][a['start']:a['end']])
        e=SimpleNamespace(docs=self.docs,pages=copy.deepcopy(self.pages),registry=SimpleNamespace(rules=self.rules))
        with tempfile.TemporaryDirectory() as t:
            path=Path(t)/'graph.json';path.write_text(json.dumps(g))
            ReferenceGraph(path,e)
            e.pages[0]['text']+=' changed'
            with self.assertRaises(ValueError):ReferenceGraph(path,e)

    def test_fabricated_anchor_is_refused_even_with_matching_corpus_hash(self):
        g=self.build();g['edges'][0]['evidence']['quote']='Invented source reference'
        engine=SimpleNamespace(docs=self.docs,pages=self.pages,registry=SimpleNamespace(rules=self.rules))
        with tempfile.TemporaryDirectory() as t:
            path=Path(t)/'g.json';path.write_text(json.dumps(g))
            with self.assertRaises(ValueError):ReferenceGraph(path,engine)


class ExpansionBudgetTests(unittest.TestCase):
    def setUp(self):
        from tests.test_research import ResearchTests
        ResearchTests.setUp(self)

    def test_candidate_cannot_displace_existing_evidence(self):
        from tests.test_research import ResearchTests
        baseline=ResearchTests.ask(self)
        self.e.config['context_char_budget']=max(2000,baseline['retrieval_trace']['evidence_characters'])
        extra=dict(self.e.parts_by_doc['unrelated'][0],id='extra',text='Customer consent information. '*5)
        self.e.reference_graph=SimpleNamespace(expand=lambda *args:[(extra,dict(id='test-edge'))])
        candidate=ResearchTests.ask(self)
        self.assertEqual([s['id'] for s in baseline['sources']],[s['id'] for s in candidate['sources'][:len(baseline['sources'])]])
        self.assertLessEqual(candidate['retrieval_trace']['evidence_characters'],self.e.config['context_char_budget'])

    def test_strict_and_selected_summary_do_not_expand(self):
        from tests.test_research import ResearchTests
        self.e.reference_graph=Mock()
        ResearchTests.ask(self,scope='strict')
        ResearchTests.ask(self,query='Summarise the consent framework',route='summary',document_ids=['framework'])
        self.e.reference_graph.expand.assert_not_called()


class AnswerOwnershipTests(unittest.TestCase):
    def test_collective_category_cannot_borrow_from_amendment(self):
        sources=[dict(circular_number='20',text='School payments are limited to INR 4 lakh.'),
                 dict(circular_number='20B',text='Medical payments are limited to INR 4 lakh.')]
        self.assertIsNotNone(collective_attribution_issue('OC20 and OC20B both set a limit for medical payments of INR 4 lakh.',sources))
        self.assertIsNone(collective_attribution_issue('OC20 and OC20B set different limits for school and medical payments respectively.',sources))
        sources[0]['text']='Medical payments are limited to INR 4 lakh.'
        self.assertIsNone(collective_attribution_issue('OC20 and OC20B both set a limit for medical payments of INR 4 lakh.',sources))
    def test_known_navigation_label_not_a_factual_number(self):
        c=dict(text='Document S9 requires code 59, under section S9.',sources=['S9'])
        got=without_inline_citation_markers(c,{'S9':{}})
        self.assertEqual(got['text'],'The cited source requires code 59, under section S9.')
        self.assertEqual(got['original_text'],c['text'])
        self.assertEqual(without_inline_citation_markers(c,{}),c)
    def test_duplicate_repair_keeps_primary_coverage_and_citations(self):
        kept=[dict(text='The limit is 4.',sources=['S1'],draft_index=1)]
        flagged=[dict(text='Wrong 3.',sources=['S1'],draft_index=2,review_reasons=['wrong'])]
        replies=[dict(status='repairable',text='The limit is 4.',sources=['S1']),dict(status='supported',evidence_ids=['S1.1'])]
        engine=SimpleNamespace(config={'generation_model':'test'},ollama=Mock(side_effect=[dict(response=json.dumps(r)) for r in replies]))
        result,remaining,checks,audit=repair_claims(engine,kept,flagged,[],[dict(citation='S1',text='The limit is 4.')],'Limit?')
        self.assertEqual(len(result),1);self.assertFalse(remaining)
        self.assertEqual(result[0]['covered_draft_indices'],[1,2]);self.assertEqual(audit[0]['duplicate_of_draft_index'],1)
