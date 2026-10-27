import json
import unittest
from types import SimpleNamespace
from unittest.mock import Mock
from claim_check import check_claims,with_citation_companions
from claim_repair import repair_claims
from evidence_spans import source_spans
from request_runtime import CURRENT,Run
from scope_guard import table_scope_issue,attribution_scope_issue,beyond_ceiling_issue
from tools.repair_ocr_sample import apply_edits

TABLE='''Annexure
| Category | Code | Per-transaction limit | Cumulative limit (24 hrs) |
|---|---|---|---|
| School fees | 9911 | ₹3 lakh | ₹8 lakh |
| Medical services | 9911 | ₹4 lakh | ₹9 lakh |
| Travel | 9912 | ₹2 lakh | ₹6 lakh |
Notes: these are illustrative test values.'''

class ScopeGuardTests(unittest.TestCase):
    def test_address_digits_cannot_support_an_unstated_money_amount(self):
        from scope_guard import monetary_support_issue
        source=dict(text='The mandate limit is Rs 5 lakh. Address: 10th floor. Contact 1001.')
        self.assertIsNotNone(monetary_support_issue('The limit is Rs 10 lakh.',[source]))
        self.assertIsNotNone(monetary_support_issue('The limit is Rs 5 crore.',[source]))
        self.assertIsNone(monetary_support_issue('The limit is INR 500,000.',[source]))
    def test_money_guard_does_not_interpret_unitless_table_cells(self):
        from scope_guard import monetary_support_issue
        self.assertIsNone(monetary_support_issue('The limit is Rs 5 lakh.',[dict(text='Limits in lakh | Amount | 5 |')]))
    def test_money_guard_runs_even_if_model_would_accept_address_digits(self):
        engine=SimpleNamespace(config={'generation_model':'test'},ollama=Mock())
        kept,flagged,_=check_claims(engine,[dict(text='The mandate limit is Rs 10 lakh.',sources=['S1'])],
            [dict(citation='S1',text='The mandate limit is Rs 5 lakh. Address 10th floor.')])
        self.assertFalse(kept);self.assertTrue(flagged);engine.ollama.assert_not_called()
    def test_within_ceiling_exemption_does_not_establish_above_ceiling_rule(self):
        sources=[dict(text='Transactions are capped at 7000, up to which extra authentication is not required.')]
        self.assertIsNotNone(beyond_ceiling_issue('The cap is 7000, above which extra authentication may be required.',sources))
        self.assertIsNone(beyond_ceiling_issue('Up to 7000, extra authentication is not required.',sources))
    def test_explicit_above_ceiling_rule_is_still_semantically_checked(self):
        sources=[dict(text='Up to 7000 no extra authentication is required. Above 7000, a separate method is required.')]
        self.assertIsNone(beyond_ceiling_issue('The boundary is 7000, above which a separate method is required.',sources))
    def test_named_circular_cannot_borrow_scope_from_unnamed_citation(self):
        sources=[dict(circular_number='70B',text='Capital Market | ₹5 lakh'),dict(circular_number='42',text='The IPO mandate limit is ₹5 lakh.')]
        self.assertIsNotNone(attribution_scope_issue('Under OC 70B, a single IPO mandate has a limit of ₹5 lakh.',sources))
        self.assertIsNotNone(attribution_scope_issue('Under OC 70B, a single IPO mandate has a limit of ₹5 lakh.',sources[:1]))
        self.assertIsNone(attribution_scope_issue('OC 70B specifies Capital Market limits; OC 42 specifies the IPO mandate limit.',sources))
    def test_attribution_guard_is_not_product_specific(self):
        sources=[dict(circular_number='12',text='Wallet balances.'),dict(circular_number='9',text='CBDC transfers.')]
        self.assertIsNotNone(attribution_scope_issue('Circular 12 permits CBDC transfers.',sources))
    def test_appending_correct_source_does_not_excuse_wrong_sentence(self):
        sources=[dict(circular_number='70B',text='Capital Market | ₹5 lakh'),dict(circular_number='42',text='The IPO mandate limit is ₹5 lakh.')]
        self.assertIsNotNone(attribution_scope_issue('OC 70B establishes the IPO limit. This rule is in Circular 42.',sources))
    def test_negative_scope_comparison_is_not_forced_into_wrong_source(self):
        sources=[dict(circular_number='70B',title='Limits in UPI',text='Capital Market | ₹5 lakh | ₹10 lakh')]
        self.assertIsNone(attribution_scope_issue('UPI OC 70B does not make a single IPO mandate limit 10 lakh; instead, the Capital Market cumulative limit is 10 lakh.',sources))
    def issue(self,claim,text=TABLE):return table_scope_issue(claim,[dict(text=text)])
    def test_same_code_does_not_transfer_amount_between_categories(self):
        self.assertIsNotNone(self.issue('School fees with code 9911 have a cumulative limit of ₹9 lakh.'))
    def test_wrong_column_is_rejected(self):
        self.assertIsNotNone(self.issue('School fees have a per-transaction limit of ₹8 lakh.'))
    def test_matching_category_and_column_passes(self):
        self.assertIsNone(self.issue('School fees have a cumulative limit of ₹8 lakh.'))
    def test_flattened_table_remains_checkable(self):
        self.assertIsNotNone(self.issue('School fees have a cumulative limit of ₹9 lakh.',' '.join(TABLE.split())))
    def test_prose_rule_is_not_replaced_by_table_rule(self):
        self.assertIsNone(self.issue('Tax payments have a limit of ₹5 lakh.','Tax payments have a limit of ₹5 lakh.\n'+TABLE))
    def test_selected_quotes_must_include_numbers(self):
        source=dict(citation='S1',text='The limit is 80. '+('Other information. '*200)+'The limit is 90.')
        engine=SimpleNamespace(config={'generation_model':'test'},ollama=Mock(return_value={'response':json.dumps(dict(status='supported',reason='claimed',evidence_ids=['S1.1']))}))
        kept,flagged,_=check_claims(engine,[dict(text='The limit is 90.',sources=['S1'])],[source])
        self.assertFalse(kept);self.assertIn('Selected supporting quotes',flagged[0]['review_reasons'][-1])
    def test_contradictory_legacy_verdict_is_not_accepted(self):
        engine=SimpleNamespace(config={'generation_model':'test'},ollama=Mock(return_value={'response':json.dumps(dict(status='supported',reason='conflict',evidence_ids=['S1.1']))}))
        kept,_,_=check_claims(engine,[dict(text='Consent is required.',sources=['S1'])],[dict(citation='S1',text='Consent is required.')])
        self.assertFalse(kept)
    def test_spans_preserve_text_and_stop_at_sentence(self):
        text=('A'*400)+'. '+('B'*400)+'. End.'
        anchors,_=source_spans([dict(citation='S1',text=text)])
        self.assertEqual(''.join(a['quote'] for a in anchors.values()),text)
        self.assertEqual(anchors['S1.1']['quote'],('A'*400)+'. ')


class ClaimRepairTests(unittest.TestCase):
    def test_companion_completion_is_bounded_to_retrieved_same_page(self):
        sources={'S1':dict(document_id='d',page=1,citation_companions=['S2','S3','S4','S5','S6']),
                 'S2':dict(document_id='d',page=1), 'S3':dict(document_id='other',page=1),
                 'S4':dict(document_id='d',page=2),'S5':dict(document_id='d',page=1,generation_eligible=False)}
        result=with_citation_companions(dict(text='Rule',sources=['S1']),sources)
        self.assertEqual(result['sources'],['S1','S2']);self.assertEqual(result['original_sources'],['S1'])
    def test_companion_addition_does_not_bypass_semantic_check(self):
        sources=[dict(citation='S1',document_id='d',page=1,text='Code 1',citation_companions=['S2']),dict(citation='S2',document_id='d',page=1,text='Code 2 is excluded')]
        engine=SimpleNamespace(config={'generation_model':'test'},ollama=Mock(return_value={'response':json.dumps(dict(status='unsupported',evidence_ids=['S2.1']))}))
        kept,flagged,_=check_claims(engine,[dict(text='Code 2 is included.',sources=['S1'])],sources)
        self.assertFalse(kept);self.assertEqual(flagged[0]['sources'],['S1','S2'])
    def setUp(self):
        self.sources=[dict(citation='S1',document_id='old',text='The original limit was 3.'),dict(citation='S2',document_id='new',text='The amended limit is 4.')]
        self.claim=dict(text='The amended limit is 4.',sources=['S1'],draft_index=1,support_status='unsupported',review_reasons=['Missing number'])
        self.checks=[dict(claim_index=0,status='unsupported')]
    def run_repair(self,replies,flagged=None):
        engine=SimpleNamespace(config={'generation_model':'test'},ollama=Mock(side_effect=[dict(response=json.dumps(r)) for r in replies]))
        return repair_claims(engine,[],flagged or [self.claim],list(self.checks),self.sources,'What is the amended limit?'),engine
    def test_citation_repair_rechecked_and_history_retained(self):
        (kept,flagged,checks,audit),engine=self.run_repair([dict(status='repairable',text='The amended limit is 4.',sources=['S2']),dict(status='supported',reason='Direct',evidence_ids=['S2.1'])])
        self.assertEqual(kept[0]['sources'],['S2']);self.assertFalse(flagged)
        self.assertEqual(audit[0]['original']['sources'],['S1']);self.assertEqual(audit[0]['original_check']['status'],'unsupported')
        self.assertTrue(checks[0]['repair_applied']);self.assertEqual(engine.ollama.call_count,2)
    def test_repair_cannot_bypass_number_guard(self):
        (kept,flagged,_,audit),engine=self.run_repair([dict(status='repairable',text='The amended limit is 999.',sources=['S2'])])
        self.assertFalse(kept);self.assertEqual(len(flagged),1);self.assertEqual(audit[0]['status'],'rejected');self.assertEqual(engine.ollama.call_count,1)
    def test_registry_label_repair_cannot_borrow_an_unrelated_rule(self):
        claim=dict(self.claim,text='Document reg-source-9988776655 says the original limit was 3.',review_reasons=['Claim contains a number absent from cited text.'])
        (kept,flagged,_,audit),engine=self.run_repair([dict(status='repairable',text='The amended limit is 4.',sources=['S2'])],[claim])
        self.assertFalse(kept);self.assertTrue(flagged)
        self.assertEqual(audit[0]['evidence_citations'],['S1'])
        self.assertEqual(engine.ollama.call_count,1)
    def test_registry_label_repair_rechecks_actual_amount(self):
        claim=dict(self.claim,text='Document reg-source-9988776655 says the original limit was 3.',review_reasons=['Claim contains a number absent from cited text.'])
        (kept,flagged,_,audit),_=self.run_repair([dict(status='repairable',text='The original limit was 3.',sources=['S1']),dict(status='supported',evidence_ids=['S1.1'])],[claim])
        self.assertFalse(flagged);self.assertEqual(len(kept),1)
        self.assertEqual(audit[0]['repair_scope'],'attached_evidence_for_registry_label')
    def test_unknown_or_quarantined_citation_rejected(self):
        self.sources.append(dict(citation='S9',text='The amended limit is 999.',generation_eligible=False))
        (kept,flagged,_,audit),_=self.run_repair([dict(status='repairable',text='The amended limit is 999.',sources=['S9'])])
        self.assertFalse(kept);self.assertTrue(flagged);self.assertEqual(audit[0]['status'],'unavailable_or_invalid')
    def test_repair_does_not_loop_and_caps_at_two(self):
        claims=[dict(self.claim,draft_index=i) for i in range(1,5)]
        (_,flagged,_,audit),engine=self.run_repair([dict(status='unresolved',text='',sources=[])]*2,claims)
        self.assertEqual(len(flagged),4);self.assertEqual(engine.ollama.call_count,2);self.assertEqual(len(audit),2)
    def test_exhausted_budget_does_not_add_calls(self):
        token=CURRENT.set(Run({'claim_review_budget_seconds':0}))
        try:
            (kept,flagged,_,_),engine=self.run_repair([])
            self.assertFalse(kept);self.assertTrue(flagged);engine.ollama.assert_not_called()
        finally:CURRENT.reset(token)
    def test_unavailable_checker_does_not_trigger_content_repair(self):
        failed=dict(self.claim,review_reasons=['Automated support check unavailable or malformed; claim withheld for review.'])
        (kept,flagged,_,audit),engine=self.run_repair([], [failed])
        self.assertFalse(kept);self.assertTrue(flagged);engine.ollama.assert_not_called()
        self.assertEqual(audit[0]['status'],'skipped_check_unavailable')
    def test_semantic_rejection_remains_withheld(self):
        (kept,flagged,_,audit),_=self.run_repair([dict(status='repairable',text='The amended limit is 4.',sources=['S2']),dict(status='unsupported',reason='Different scope',evidence_ids=['S2.1'])])
        self.assertFalse(kept);self.assertTrue(flagged);self.assertEqual(audit[0]['status'],'rejected')


class ReviewedEditTests(unittest.TestCase):
    def test_exact_edit_and_legacy_reflow(self):
        changes=[dict(before='A\nB',after='A | B')]
        self.assertEqual(apply_edits('A B',changes,allow_reflow=True),'A | B')
        with self.assertRaises(ValueError):apply_edits('A B',changes)
    def test_missing_ambiguous_or_changed_text_refused(self):
        for source in ['A C','A B A B']:
            with self.assertRaises(ValueError):apply_edits(source,[dict(before='A\nB',after='fixed')],allow_reflow=True)

if __name__=='__main__':unittest.main()
