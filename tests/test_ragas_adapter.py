"""Evaluation integrity checks; no RAGAS install or model calls required."""
import copy
import unittest
from evaluation.ragas_runner import adapt, aggregate, displayed_answer, local_url, metric_skip, verify_resume


class RagasAdapterTests(unittest.TestCase):
    def setUp(self):
        self.case = dict(id='test', query='Who checks?', route='clause', references=[
            dict(document_id='d', page=2, quote='Bank checks')], expected_answer='The bank.')
        self.claim = dict(text='The bank checks.', sources=['S1'])
        self.response = dict(mode='generate', answer='Draft answer - check excerpts.',
                             claims=[self.claim], answer_blocks=[dict(type='paragraph', claims=[self.claim])],
                             sources=[dict(citation='S1', document_id='d', page=2, text='Bank\nchecks.', issue_date='2026-01-01')],
                             abstained=False, retrieval_trace={})

    def test_actual_answer_not_status_banner(self):
        sample = adapt(self.case, self.response)
        self.assertEqual(sample['response'], 'The bank checks.')
        self.assertEqual(sample['checks']['anchor_hits'], [True])
        self.assertIn('2026-01-01', sample['retrieved_contexts'][0])

    def test_display_order_and_checked_claims(self):
        second = dict(text='Then confirm.', sources=['S1'])
        self.response['claims'] = [self.claim, second]
        self.response['answer_blocks'] = [dict(type='bullets', claims=[second, self.claim])]
        self.assertEqual(displayed_answer(self.response)[0], 'Then confirm.\nThe bank checks.')

    def test_evidence_mode_rejected(self):
        self.response['mode'] = 'evidence'
        with self.assertRaises(ValueError): adapt(self.case, self.response)

    def test_banner_without_claims_rejected(self):
        self.response.update(claims=[], answer_blocks=[])
        with self.assertRaises(ValueError): adapt(self.case, self.response)

    def test_abstention_not_counted_as_faithful_answer(self):
        self.response.update(claims=[], answer_blocks=[], abstained=True, answer='Cannot answer.')
        sample = adapt(self.case, self.response)
        self.assertEqual(sample['response'], 'Cannot answer.')
        self.assertFalse(sample['checks']['abstention_matches_expectation'])
        self.assertIsNone(sample['checks']['citation_ids_valid'])
        self.assertIsNotNone(metric_skip(sample, 'faithfulness'))

    def test_negative_answer_is_visible_failure(self):
        self.case.update(expect_abstain=True, references=[])
        sample = adapt(self.case, self.response)
        self.assertFalse(sample['checks']['abstention_matches_expectation'])
        self.assertEqual(metric_skip(sample, 'faithfulness'), 'negative_case_use_abstention_checks')

    def test_wrong_page_does_not_pass_anchor(self):
        self.response['sources'][0]['page'] = 1
        self.assertEqual(adapt(self.case, self.response)['checks']['anchor_hits'], [False])

    def test_missing_and_foreign_citations_fail(self):
        self.claim['sources'] = ['S9']
        self.assertFalse(adapt(self.case, self.response)['checks']['citation_ids_valid'])
        self.claim['sources'] = []
        self.assertEqual(adapt(self.case, self.response)['checks']['uncited_claims'], 1)

    def test_summary_rubric_not_treated_as_complete_reference(self):
        self.case['route'] = 'summary'
        sample = adapt(self.case, self.response)
        self.assertIsNotNone(metric_skip(sample, 'factual_correctness'))
        self.assertIsNone(metric_skip(sample, 'faithfulness'))

    def test_denominators_include_failures_skips_and_pending(self):
        rows = [dict(metrics={'m': dict(status='ok', value=0.0)}),
                dict(metrics={'m': dict(status='ok', value=1.0)}),
                dict(metrics={'m': dict(status='error')}),
                dict(metrics={'m': dict(status='skipped')}), dict(metrics={})]
        self.assertEqual(aggregate(rows, 'm'), dict(mean=.5, scored=2, errors=1, skipped=1, pending=1, total=5))

    def test_all_failed_scores_not_zero_or_perfect(self):
        self.assertIsNone(aggregate([dict(metrics={'m': dict(status='error')})], 'm')['mean'])

    def test_only_local_endpoints(self):
        self.assertEqual(local_url('http://127.0.0.1:11434/'), 'http://127.0.0.1:11434')
        for url in ['https://example.com', 'http://127.0.0.1.evil.test', 'http://user:pass@localhost']:
            with self.assertRaises(ValueError): local_url(url)

    def test_resume_refuses_different_capture_or_judge(self):
        saved = dict(capture_sha256='a', judge_digest='model-a')
        verify_resume(saved, dict(saved))
        for changes in [dict(capture_sha256='b'), dict(judge_digest='model-b')]:
            with self.assertRaises(ValueError): verify_resume(saved, dict(saved, **changes))


if __name__ == '__main__':
    unittest.main()
