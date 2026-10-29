import unittest
from unittest.mock import patch
from evidence_focus import overview_change_matches
from tests import test_work_items as work_fixture
from tests import test_research as research_fixture


class OverviewEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.rule = dict(id='revised:2', document_id='revised', title='Amendment to Pocket Pay limits',
                         text='For Pocket Pay, the enhanced limits shall be 100 per transaction. Other conditions apply.')

    def test_operative_clause_survives_instead_of_reference_preface(self):
        preface=dict(self.rule,id='revised:1',text='Reference: Pocket Pay was introduced and its limit was increased previously.')
        self.assertEqual(overview_change_matches('What is Pocket Pay? Answer briefly.',[preface,self.rule]),[self.rule])

    def test_explanation_style_words_are_normalized_like_query_terms(self):
        for query in ['Explain Pocket Pay in simple words.', 'Describe Pocket Pay in simple terms.']:
            self.assertEqual(overview_change_matches(query,[self.rule]),[self.rule])

    def test_unrelated_and_partial_topic_matches_are_not_added(self):
        for title in ['Amendment to Merchant Pay limits', 'Pocket payments', 'General limits']:
            self.assertFalse(overview_change_matches('Explain Pocket Pay.',[dict(self.rule,title=title)]))

    def test_history_exact_reference_and_narrow_questions_do_not_expand(self):
        for query in ['What is Pocket Pay in OC169A?', 'Explain the original Pocket Pay.',
                      'Explain Pocket Pay in 2023.', 'What is Pay?', 'Pocket Pay transaction limit?']:
            self.assertFalse(overview_change_matches(query,[self.rule]),query)

    def test_recovery_is_bounded_and_deduplicated_by_document(self):
        parts=[dict(self.rule,id=str(i),document_id=str(i)) for i in range(5)]
        self.assertEqual(len(overview_change_matches('Explain Pocket Pay.',parts)),2)
        self.assertEqual(len(overview_change_matches('Explain Pocket Pay.',[self.rule,self.rule])),1)


class ChangeSummaryTests(unittest.TestCase):
    setUp=work_fixture.WorkTests.setUp

    def test_no_generic_department_actions_and_analyst_notes_survive_regeneration(self):
        item=self.store.create(dict(kind='impact',query='Explain this change.',document_ids=['a','b']),self.engine)
        item=self.store.generate(item['id'],item['revision'],self.engine)
        self.assertEqual(item['draft']['actions'],'')
        prompt=self.engine.answer.call_args.args[0]['query']
        self.assertIn('not automatically retained or withdrawn',prompt)
        self.assertIn('separate citations',prompt)
        item=self.store.edit(item['id'],dict(revision=item['revision'],text=item['draft']['text'],
            actions='Check our internal procedure.',reviewer_questions='Who owns this process?'),self.engine)
        item=self.store.generate(item['id'],item['revision'],self.engine)
        self.assertEqual(item['draft']['actions'],'Check our internal procedure.')
        self.assertEqual(item['draft']['reviewer_questions'],'Who owns this process?')


class OverviewScopeTests(unittest.TestCase):
    setUp=research_fixture.ResearchTests.setUp

    def answer(self, **scope):
        return self.e.answer(dict(query='Explain UPI consent.',mode='evidence',method='bm25',**scope))

    def test_explicit_document_selection_bypasses_overview_recovery(self):
        with patch('evidence_focus.overview_change_matches') as recover:
            result=self.answer(document_ids=['network'],scope='strict')
        recover.assert_not_called()
        self.assertEqual({s['document_id'] for s in result['sources']},{'network'})

    def test_product_filter_applies_even_to_recovered_candidate(self):
        outside=next(p for p in self.e.parts_by_id.values() if p['document_id']=='framework')
        with patch('evidence_focus.overview_change_matches',return_value=[outside]):
            result=self.answer(series='UPI',scope='related')
        self.assertEqual({s['document_id'] for s in result['sources']},{'network'})

    def test_issue_cutoff_cannot_be_bypassed_by_recovery(self):
        outside=next(p for p in self.e.parts_by_id.values() if p['document_id']=='framework')
        self.e.by_id['framework']['issue_date']='2026-01-01'
        with patch('evidence_focus.overview_change_matches',return_value=[outside]):
            result=self.answer(cutoff='2025-06-01',scope='related')
        self.assertNotIn('framework',{s['document_id'] for s in result['sources']})
