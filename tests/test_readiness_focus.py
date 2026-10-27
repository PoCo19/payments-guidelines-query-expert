import json
from types import SimpleNamespace
import unittest
from unittest.mock import Mock
from evidence_focus import table_matches,phase_companions
from scope_guard import notification_phase_issue,table_scope_issue,collective_attribution_issue
from claim_check import check_claims


TABLE='| Category | Per transaction | Daily cumulative | |---|---|---| | Credit Card Bill Payments | INR 5 lakh | INR 6 lakh | | Capital Market | INR 5 lakh | INR 10 lakh |'


class FocusTests(unittest.TestCase):
    def test_collective_source_claim_requires_each_named_document(self):
        self.assertIsNotNone(collective_attribution_issue('OC10 and OC10A consistently set the same limit.',[dict(circular_number='10A')]))
        self.assertIsNone(collective_attribution_issue('OC10 and OC10A consistently set the same limit.',[dict(circular_number='10'),dict(circular_number='10A')]))
        self.assertIsNone(collective_attribution_issue('OC10A updates the limit previously described by OC10.',[dict(circular_number='10A')]))

    def test_collective_selected_quotes_need_both_circulars(self):
        sources=[dict(citation='S1',text='The limit is INR 5 lakh.',circular_number='10'),dict(citation='S2',text='The limit is INR 5 lakh.',circular_number='10A')]
        engine=SimpleNamespace(config={'generation_model':'test'},ollama=Mock(return_value={'response':json.dumps(dict(status='supported',evidence_ids=['S2.1']))}))
        claims=[dict(text='Both OC10 and OC10A set a limit of INR 5 lakh.',sources=['S1','S2'])]
        kept,flagged,_=check_claims(engine,claims,sources)
        self.assertFalse(kept);self.assertTrue(flagged)
        engine.ollama.return_value={'response':json.dumps(dict(status='supported',evidence_ids=['S1.1','S2.1']))}
        kept,flagged,_=check_claims(engine,claims,sources)
        self.assertTrue(kept);self.assertFalse(flagged)

    def test_combined_limits_keep_their_own_columns(self):
        sources=[dict(text=TABLE)]
        for conjunction in ('while','and','whereas',';'):
            good=f'Credit Card Bill Payments allow INR 5 lakh for a single payment {conjunction} INR 6 lakh cumulative over 24 hours.'
            bad=f'Credit Card Bill Payments allow INR 6 lakh for a single payment {conjunction} INR 5 lakh cumulative over 24 hours.'
            with self.subTest(conjunction=conjunction):
                self.assertIsNone(table_scope_issue(good,sources))
                self.assertIsNotNone(table_scope_issue(bad,sources))

    def test_literal_category_and_hyphenated_query(self):
        p=dict(id='table',text=TABLE)
        self.assertEqual(table_matches('credit-card bill payment ceiling',[p]),[p])
        self.assertFalse(table_matches('Card payment ceiling',[p]))
        self.assertFalse(table_matches('Tax payment limit under MCC 5413',[p]))
        self.assertFalse(table_matches('How are credit card bills settled?',[p]))

    def test_focus_is_bounded_and_does_not_rewrite_sources(self):
        parts=[dict(id=str(i),text=TABLE) for i in range(4)]
        self.assertEqual(len(table_matches('Capital market limit',parts)),2)
        self.assertTrue(all(p['text']==TABLE for p in parts))

    def test_adjacent_phase_in_same_document_only(self):
        seed=dict(id='pre',document_id='one',text='Pre-transaction notification is exempt.',next_chunk_id='post')
        part=dict(id='post',document_id='one',text='Send a message.',section_heading='Post-transaction notification')
        engine=SimpleNamespace(parts_by_id={'post':part})
        self.assertEqual(phase_companions(engine,'Can the message after debit be skipped?',[seed]),[part])
        self.assertFalse(phase_companions(engine,'What is the pre-transaction notification rule?',[seed]))
        part['document_id']='other'
        self.assertFalse(phase_companions(engine,'What notice is required after debit?',[seed]))

    def test_phase_guard_preserves_distinctions(self):
        pre=dict(text='Pre-transaction notification is not required for auto-replenishment.')
        post=dict(text='An issuer shall send a post-transaction notification.')
        self.assertIsNotNone(notification_phase_issue('Post-transaction notification is not required.',[pre]))
        self.assertIsNotNone(notification_phase_issue('The issuer may skip the message after debit.',[pre]))
        self.assertIsNotNone(notification_phase_issue('The issuer does not need to send post-transaction notification.',[pre]))
        self.assertIsNone(notification_phase_issue('Pre-transaction notification is not required.',[pre]))
        self.assertIsNone(notification_phase_issue('Post-transaction notification is required.',[post]))
        self.assertIsNone(notification_phase_issue('The pre-transaction exemption does not establish a post-transaction exemption.',[pre]))
        self.assertIsNone(notification_phase_issue('Pre-transaction notification is exempt; post-transaction notification remains required.',[pre,post]))

    def test_selected_excerpts_cannot_borrow_other_phase(self):
        sources=[dict(citation='S1',text='Pre-transaction notification is exempt.'),dict(citation='S2',text='Post-transaction notification is required.')]
        engine=SimpleNamespace(config={'generation_model':'test'},ollama=Mock(return_value={'response':json.dumps(dict(status='supported',evidence_ids=['S1.1']))}))
        kept,flagged,_=check_claims(engine,[dict(text='Post-transaction notification is exempt.',sources=['S1','S2'])],sources)
        self.assertFalse(kept);self.assertTrue(flagged)

    def test_valid_selected_excerpt_survives(self):
        source=dict(citation='S1',text='Post-transaction notification is required.')
        engine=SimpleNamespace(config={'generation_model':'test'},ollama=Mock(return_value={'response':json.dumps(dict(status='supported',evidence_ids=['S1.1']))}))
        kept,flagged,_=check_claims(engine,[dict(text=source['text'],sources=['S1'])],[source])
        self.assertTrue(kept);self.assertFalse(flagged)

    def test_checker_failure_diagnostics_do_not_leak_to_next_claim(self):
        source=dict(citation='S1',text='Post-transaction notification is required.')
        engine=SimpleNamespace(config={'generation_model':'test'},ollama=Mock(side_effect=[TimeoutError('deadline'),{'response':json.dumps(dict(status='supported',evidence_ids=['S1.1']))}]))
        _,_,checks=check_claims(engine,[dict(text=source['text'],sources=['S1'])]*2,[source])
        self.assertIn('TimeoutError',checks[0]['failure_reason']);self.assertNotIn('failure_reason',checks[1])
