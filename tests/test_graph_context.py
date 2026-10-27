import json
from pathlib import Path
import unittest
from graph_context import EvidenceGraph, digest, load_graph
import test_research as fixture


class GraphTests(unittest.TestCase):
    def setUp(self):
        fixture.ResearchTests.setUp(self)
        self.path = Path(self.temp.name)/'graph.json'
        self.data = dict(schema_version=1,review_status='proposed_ai_assisted',nodes=[
            dict(id=p['document_id'],document_id=p['document_id'],page=1,
                 quote=p['text'].split('\n')[-1],page_sha256=digest(p['text']),aspect='consent',priority=0)
            for p in self.pages if p['document_id'] != 'unrelated'],
            edges=[dict(from_id='network',to_id='framework',type='amends_aspect',evidence_anchor='network',review_status='proposed_ai_assisted')],
            topics=[dict(id='consent',terms=['consent'],anchors=['network','framework'])])
        self.write()
        self.e.evidence_graph = EvidenceGraph(self.path,self.e)

    def write(self):
        self.path.write_text(json.dumps(self.data),encoding='utf-8')

    def ask(self, **kwargs):
        return self.e.answer(dict(query='UPI consent operations',mode='evidence',method='bm25',rerank=False,**kwargs))

    def test_graph_keeps_both_scopes_with_provenance(self):
        r=self.ask()
        g=r['retrieval_trace']['graph_context']
        self.assertEqual(g['status'],'active')
        self.assertTrue(g['complete_within_pilot'])
        self.assertEqual(g['relationships'][0]['type'],'amends_aspect')
        self.assertEqual(g['relationships'][0]['review_status'],'proposed_ai_assisted')
        self.assertTrue(any(s['retrieval_reason']=='graph_anchor' for s in r['sources']))
        self.assertEqual([s['citation'] for s in r['sources']],[f'S{i+1}' for i in range(len(r['sources']))])

    def test_explicit_product_filter_remains_a_boundary(self):
        r=self.ask(series='UPI')
        self.assertEqual({p['document_id'] for p in r['sources']},{'network'})
        self.assertFalse(r['retrieval_trace']['graph_context']['complete_within_pilot'])

    def test_strict_selected_summary_and_compare_bypass_graph(self):
        for options in [dict(scope='strict'),dict(document_ids=['network']),
                        dict(route='summary',document_ids=['network']),
                        dict(route='compare',document_ids=['network','framework'])]:
            with self.subTest(options=options):
                self.assertNotIn('graph_context',self.ask(**options)['retrieval_trace'])

    def test_ambiguous_prompt_cannot_be_resolved_by_graph(self):
        r=self.e.answer(dict(query='What is Tap & Pay?',mode='evidence'))
        self.assertEqual(r['response_status'],'clarification_needed')
        self.assertFalse(r['sources'])

    def test_stale_page_disables_entire_graph(self):
        self.data['nodes'][0]['page_sha256']='incorrect'; self.write()
        self.e.config['evidence_graph_path']=str(self.path)
        graph,error=load_graph(self.e)
        self.assertIsNone(graph);self.assertIn('source changed',error)

    def test_unavailable_or_fabricated_quote_rejected(self):
        for quote in ['', 'This is not in the source']:
            self.data['nodes'][0]['quote']=quote;self.write()
            with self.assertRaisesRegex(ValueError,'Invalid graph quote'):
                EvidenceGraph(self.path,self.e)

    def test_bad_relation_provenance_rejected(self):
        self.data['edges'][0]['evidence_anchor']='framework';self.write()
        with self.assertRaisesRegex(ValueError,'provenance'):
            EvidenceGraph(self.path,self.e)

    def test_unavailable_target_not_invented(self):
        self.e.by_id['network']['availability']='unavailable'
        with self.assertRaisesRegex(ValueError,'unavailable'):
            EvidenceGraph(self.path,self.e)

    def test_no_trigger_from_incidental_retrieval(self):
        parts,trace=self.e.evidence_graph.expand('catering services',['network'],[],lambda d:True)
        self.assertFalse(parts);self.assertEqual(trace['status'],'not_applicable')

    def test_topic_without_retrieved_identity_does_not_activate(self):
        parts,_=self.e.evidence_graph.expand('consent',['unrelated'],[],lambda d:True)
        self.assertFalse(parts)

    def test_bidirectional_cycle_is_bounded(self):
        self.data['edges'].append(dict(from_id='framework',to_id='network',type='references',evidence_anchor='framework',review_status='proposed_ai_assisted'))
        self.write();graph=EvidenceGraph(self.path,self.e)
        parts,trace=graph.expand('consent',['framework'],[],lambda d:True)
        self.assertEqual(len(parts),2)
        self.assertEqual(len({p['id'] for p in parts}),2)
        self.assertEqual(trace['max_hops'],2)

    def test_budget_and_partial_coverage_visible(self):
        self.e.config['context_char_budget']=2000
        self.e.evidence_graph.parts['framework']=dict(self.e.evidence_graph.parts['framework'],text='Long source qualification. '*150)
        r=self.ask()
        self.assertLessEqual(r['retrieval_trace']['evidence_characters'],2000)
        self.assertLessEqual(len(r['sources']),18)
        self.assertIn('Some evidence was omitted',' '.join(r['warnings']))

    def test_two_hops_do_not_follow_a_third_edge(self):
        p=next(p for p in self.pages if p['document_id']=='unrelated')
        self.data['nodes'].append(dict(id='unrelated',document_id='unrelated',page=1,quote=p['text'],page_sha256=digest(p['text']),aspect='context'))
        self.data['topics'][0]['anchors']+=['institution','unrelated']
        for a,b in [('framework','institution'),('institution','unrelated')]:
            self.data['edges'].append(dict(from_id=a,to_id=b,type='references',evidence_anchor=a,review_status='proposed_ai_assisted'))
        self.write();graph=EvidenceGraph(self.path,self.e)
        parts,trace=graph.expand('consent',['network'],[],lambda d:True)
        self.assertEqual({p['document_id'] for p in parts},{'network','framework','institution'})
        graph.coverage(trace,parts)
        self.assertFalse(trace['complete_within_pilot'])

    def test_graph_unavailable_preserves_baseline_with_warning(self):
        self.e.evidence_graph=None;self.e.evidence_graph_error='Graph expansion unavailable: stale source'
        r=self.ask()
        self.assertTrue(r['sources'])
        self.assertEqual(r['retrieval_trace']['graph_context']['status'],'unavailable')
        self.assertIn('stale source',' '.join(r['warnings']))

    def test_default_has_no_graph(self):
        self.assertEqual(load_graph(self.e),(None,None))

    def test_explicit_product_in_question_does_not_activate_other_product_topic(self):
        self.data['topics'][0]['products']=['UPI'];self.write()
        graph=EvidenceGraph(self.path,self.e)
        parts,trace=graph.expand('RuPay consent',['network'],[],lambda d:True)
        self.assertFalse(parts);self.assertEqual(trace['status'],'not_applicable')

    def test_shared_document_does_not_activate_unrequested_topic(self):
        self.data['topics'].append(dict(id='separate_scope',terms=['catering'],anchors=['network','institution']))
        self.write();graph=EvidenceGraph(self.path,self.e)
        _,trace=graph.expand('consent',['network'],['network'],lambda d:True)
        self.assertEqual(trace['topics'],['consent'])
        self.assertNotIn('institution',trace['expected_anchor_ids'])

    def test_topic_link_requires_both_source_anchors(self):
        self.data['edges'][0]['type']='related_topic';self.write()
        with self.assertRaisesRegex(ValueError,'both endpoints'):EvidenceGraph(self.path,self.e)
        self.data['edges'][0]['target_anchor']='framework';self.write()
        graph=EvidenceGraph(self.path,self.e)
        _,trace=graph.expand('consent',['network'],[],lambda d:True)
        self.assertEqual(trace['relationships'][0]['type'],'related_topic')

    def test_gaps_are_disclosed_without_inventing_text(self):
        self.data['topics'][0]['source_gaps']=['An intermediate circular is unavailable.']
        self.write();self.e.evidence_graph=EvidenceGraph(self.path,self.e)
        r=self.ask()
        self.assertIn('An intermediate circular is unavailable.',' '.join(r['warnings']))
        self.assertTrue(all('unavailable' not in s['text'] for s in r['sources']))

    def test_companion_citations_retain_separate_source_identity(self):
        for n in self.data['nodes']:n['support_group']='fixture_group'
        self.write();graph=EvidenceGraph(self.path,self.e)
        parts,trace=graph.expand('consent',['network'],[],lambda d:True)
        selected=[dict(p,citation=f'S{i+1}') for i,p in enumerate(parts)]
        graph.coverage(trace,selected)
        self.assertEqual(selected[0]['citation_companions'],['S2'])
        self.assertEqual(selected[1]['citation_companions'],['S1'])
        self.assertNotEqual(selected[0]['document_id'],selected[1]['document_id'])


if __name__=='__main__':unittest.main()
