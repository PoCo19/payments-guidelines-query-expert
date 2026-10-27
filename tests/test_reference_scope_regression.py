"""Reference typography must not reject supported scope or relax attribution."""
import unittest
import json
from types import SimpleNamespace
from unittest.mock import Mock
from claim_check import check_claims,without_inline_citation_markers
from scope_guard import attribution_scope_issue,scope_term_present,beyond_ceiling_issue


class ReferenceScopeTests(unittest.TestCase):
    def setUp(self):
        self.sources=[dict(document_id='limits',circular_number='185B',series='UPI',
            text='Capital Market: INR 5 lakh per transaction; INR 10 lakh cumulative over 24 hours.')]

    def test_equivalent_reference_spellings(self):
        for ref in ('OC185B','OC 185B','OC-185B','OC–185B','oc185b','OC No. 185B','OCNo.185B','Circular no. 185B'):
            with self.subTest(ref=ref):
                self.assertIsNone(attribution_scope_issue(
                    f'The INR 10 lakh figure in UPI {ref} is cumulative over 24 hours, not a single IPO mandate limit.',self.sources))

    def test_compact_reference_does_not_relax_product_attribution(self):
        issue=attribution_scope_issue('UPI OC185B establishes an IPO mandate limit of INR 5 lakh.',self.sources)
        self.assertIn('(IPO)',issue)

    def test_plural_scope_cannot_borrow_another_documents_rule(self):
        sources=self.sources+[dict(document_id='ipo',circular_number='127',series='UPI',text='The IPO limit is INR 5 lakh.')]
        for word in ('IPO','IPOs'):
            with self.subTest(word=word):
                self.assertIn('(IPO)',attribution_scope_issue(f'OC185B permits INR 5 lakh for {word}.',sources))
                self.assertIsNone(attribution_scope_issue(f'OC127 permits INR 5 lakh for {word}.',sources))
                self.assertIsNone(attribution_scope_issue(f'OC185B does not establish the ceiling for {word}.',sources))

    def test_compact_reference_does_not_relax_amount_ownership(self):
        self.assertIsNotNone(attribution_scope_issue('UPI OC185B permits INR 20 lakh per transaction.',self.sources))

    def test_generic_identifiers_and_cited_fragments(self):
        sources=[dict(document_id='bio',circular_number='226A',series='UPI',text='Biometric ceiling is INR 10 thousand.'),
                 dict(document_id='bio',circular_number='226A',series='UPI',text='Device conditions apply.')]
        self.assertIsNone(attribution_scope_issue('UPI OC226A describes biometric conditions.',sources))
        self.assertIn('(IPO)',attribution_scope_issue('UPI OC226A describes IPO conditions.',sources))

    def test_reference_without_cited_match_is_not_globally_exempted(self):
        self.assertIn('(OC127)',attribution_scope_issue('OC185B and OC127 establish a joint ceiling.',self.sources))

    def test_no_cross_sentence_amount_borrowing(self):
        sources=self.sources+[dict(document_id='ipo',circular_number='127',series='UPI',text='IPO ceiling INR 5 lakh.')]
        self.assertIsNotNone(attribution_scope_issue('OC127 establishes INR 10 lakh. OC185B explains cumulative limits.',sources))

    def test_literal_ocr_case_boundary_can_reach_semantic_check(self):
        original='The limit is Rs 5 lakh for Retail Direct SchemeandUPIbasedASBAIPO.'
        source=dict(circular_number='127',document_id='ipo',series='UPI',text=original)
        self.assertIsNone(attribution_scope_issue('Circular 127 establishes Rs 5 lakh for UPI-based ASBA IPOs.',[source]))
        self.assertEqual(source['text'],original)
        self.assertTrue(scope_term_present('ASBA',original))
        self.assertTrue(scope_term_present('ASBA','ASBAIPO'))
        self.assertTrue(scope_term_present('MCC','purpose Code01withMCC6211.'))
        self.assertTrue(scope_term_present('MCC','Code01MCC6211'))

    def test_ordinary_word_substrings_are_not_scope_evidence(self):
        for term,text in [('RDS','CARDS issued'),('RDS','CARDSissued'),('RDS','cards'),('IPO','tripod'),('PI','CAPITAL')]:
            with self.subTest(term=term,text=text):self.assertFalse(scope_term_present(term,text))

    def test_beyond_which_does_not_invent_an_above_ceiling_rule(self):
        source=dict(text='The per-transaction limit is capped at INR 5000, up to which no additional factor is required.')
        self.assertIsNotNone(beyond_ceiling_issue('The limit is INR 5000, beyond which additional factors may be required.',[source]))
        self.assertIsNone(beyond_ceiling_issue('The limit is capped at INR 5000, up to which no additional factor is required.',[source]))
        explicit=dict(text=source['text']+' Above this limit, additional authentication applies.')
        self.assertIsNone(beyond_ceiling_issue('Beyond this limit, additional authentication applies.',[explicit]))


class InlineCitationTests(unittest.TestCase):
    def test_only_known_attached_bracket_markers_are_removed(self):
        claim=dict(text='OC 42 (S8) requires consent [S8,S9].',sources=['S8','S9'])
        cleaned=without_inline_citation_markers(claim,{'S8':{},'S9':{}})
        self.assertEqual(cleaned['text'],'OC 42 requires consent.')
        self.assertEqual(cleaned['sources'],['S8','S9'])
        self.assertEqual(cleaned['original_text'],claim['text'])
        self.assertIn('(S8)',claim['text'])

    def test_unknown_labels_and_factual_codes_are_preserved(self):
        for text in ('Code S8 is excluded.','Code K1 is excluded.','Section (8) applies.','Claim (S99).','Claim [S9].'):
            claim=dict(text=text,sources=['S8'])
            self.assertEqual(without_inline_citation_markers(claim,{'S8':{},'S9':{}}),claim)

    def test_citation_number_no_longer_blocks_semantic_review(self):
        source=dict(citation='S8',circular_number='42',text='Consent is required.')
        engine=SimpleNamespace(config={'generation_model':'test'},ollama=Mock(return_value={'response':json.dumps(dict(status='supported',evidence_ids=['S8.1']))}))
        kept,flagged,_=check_claims(engine,[dict(text='OC42 (S8) requires consent.',sources=['S8'])],[source])
        self.assertEqual(len(kept),1);self.assertFalse(flagged)
        engine.ollama.assert_called_once()

    def test_cleaning_does_not_bypass_semantic_rejection(self):
        source=dict(citation='S8',circular_number='42',text='Consent is required.')
        engine=SimpleNamespace(config={'generation_model':'test'},ollama=Mock(return_value={'response':json.dumps(dict(status='unsupported',evidence_ids=['S8.1']))}))
        kept,flagged,_=check_claims(engine,[dict(text='OC42 (S8) waives consent.',sources=['S8'])],[source])
        self.assertFalse(kept);self.assertTrue(flagged)

    def test_factual_number_still_requires_support(self):
        source=dict(citation='S8',circular_number='42',text='Consent is required.')
        engine=SimpleNamespace(config={'generation_model':'test'},ollama=Mock())
        kept,flagged,_=check_claims(engine,[dict(text='OC42 (S8) permits 90 payments.',sources=['S8'])],[source])
        self.assertFalse(kept);self.assertIn('number absent',flagged[0]['review_reasons'][0]);engine.ollama.assert_not_called()
