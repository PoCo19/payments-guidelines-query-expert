import unittest
from unittest.mock import patch
from request_runtime import CURRENT, PROGRESS, Run, tracked_answer


class RuntimeTests(unittest.TestCase):
    def test_call_timeout_consumes_shared_budget(self):
        with patch('request_runtime.time.monotonic', return_value=0) as clock:
            run=Run({'answer_timeout_seconds':20})
            self.assertEqual(run.timeout('generation'),20)
            clock.return_value=17
            self.assertEqual(run.timeout('coverage'),3)
            clock.return_value=21
            with self.assertRaises(TimeoutError):run.timeout('embedding')

    def test_claim_checks_have_cumulative_budget(self):
        with patch('request_runtime.time.monotonic', return_value=0) as clock:
            run=Run({'claim_review_budget_seconds':15})
            self.assertEqual(run.timeout('claim_support'),12)
            clock.return_value=13
            self.assertEqual(run.timeout('claim_support'),2)
            clock.return_value=16
            with self.assertRaises(TimeoutError):run.timeout('claim_support')

    def test_outage_returns_evidence_and_restores_context(self):
        seen=[]
        class Stub:
            config={}
            @tracked_answer
            def answer(self,payload):
                seen.append(payload)
                if payload['mode']=='generate':raise OSError('offline')
                return dict(claims=[],sources=[{'citation':'S1'}],warnings=[])
        result=Stub().answer(dict(query='test',mode='generate',method='hybrid',series='UPI'))
        self.assertTrue(result['abstained']);self.assertEqual(result['claims'],[])
        self.assertEqual(seen[-1]['method'],'bm25');self.assertFalse(seen[-1]['rerank'])
        self.assertEqual(seen[-1]['series'],'UPI');self.assertIsNone(CURRENT.get())

    def test_validation_error_is_not_disguised_as_outage(self):
        class Stub:
            config={}
            @tracked_answer
            def answer(self,payload):raise ValueError('bad input')
        with self.assertRaisesRegex(ValueError,'bad input'):Stub().answer({})
        self.assertIsNone(CURRENT.get())

    def test_stage_progress_and_timing(self):
        events=[];token=PROGRESS.set(events.append)
        try:
            run=Run({});run.set_stage('generation');run.set_stage('claim_support')
            self.assertEqual(len(events),2)
            self.assertEqual([s['stage'] for s in run.report()['stages']],['retrieval','generation','claim_support'])
        finally:PROGRESS.reset(token)

    def test_exhausted_review_budget_withholds_claims_without_model_call(self):
        from claim_check import check_claims
        from types import SimpleNamespace
        from unittest.mock import Mock
        engine=SimpleNamespace(config={'generation_model':'fixture'},ollama=Mock())
        token=CURRENT.set(Run({'claim_review_budget_seconds':0}))
        try:
            kept,flagged,checks=check_claims(engine,[dict(text='Consent is required.',sources=['S1'])],
                                            [dict(citation='S1',text='Consent is required.')])
            self.assertEqual(kept,[]);self.assertEqual(flagged[0]['support_status'],'uncertain')
            self.assertEqual(checks[0]['status'],'uncertain');engine.ollama.assert_not_called()
        finally:CURRENT.reset(token)
