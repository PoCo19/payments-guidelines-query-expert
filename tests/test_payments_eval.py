import unittest
from evaluation.ragas_runner import ROOT, load_cases, case_payload
from evaluation.payments_eval import source_hits


class PaymentsEvalTests(unittest.TestCase):
    def test_frozen_composition(self):
        cases,_=load_cases(ROOT/'evaluation/payments_cases_v1.json')
        self.assertEqual(len(cases),20)
        self.assertEqual(sum(bool(c.get('expect_abstain')) for c in cases),3)
        self.assertEqual(sum(len(c['references']) for c in cases),34)
        self.assertTrue(all(c['review_status']=='draft_requires_independent_review' for c in cases))

    def test_mixed_source_capture_does_not_force_upi(self):
        case={'query':'test','scope':'related','series':'','route':'clause','document_ids':['rbi:test']}
        self.assertEqual(case_payload(case)['series'],'')
        self.assertEqual(case_payload(case)['document_ids'],['rbi:test'])
        self.assertEqual(case_payload(case,legacy_upi=True)['series'],'UPI')

    def test_anchor_requires_text_and_ownership(self):
        case={'references':[dict(document_id='rbi:1',page=1,quote='required evidence')]}
        self.assertEqual(source_hits(case,{'sources':[dict(document_id='npci:1',page=1,text='required evidence')]}),[False])
        self.assertEqual(source_hits(case,{'sources':[dict(document_id='rbi:1',page=1,text='required   evidence')]}),[True])
