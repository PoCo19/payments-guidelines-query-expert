import importlib.util
import unittest
from pathlib import Path

spec=importlib.util.spec_from_file_location('midsem',Path(__file__).resolve().parents[1]/'evaluation/midsem_check.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class MidsemMetricTests(unittest.TestCase):
    def test_errors_do_not_improve_recall_or_negative_rate(self):
        s=module.summarize([dict(anchor_count=2,anchor_hits=[True,False],elapsed_ms=10,empty=False),dict(anchor_count=1,error='failed'),dict(anchor_count=0,error='failed')])
        self.assertEqual(s['anchor_recall'],1/3)
        self.assertEqual(s['negative_empty'],0)
        self.assertEqual(s['negative_cases'],1)
        self.assertEqual(s['failures'],2)

    def test_no_positive_cases_has_no_recall(self):
        s=module.summarize([dict(anchor_count=0,anchor_hits=[],empty=True,elapsed_ms=4)])
        self.assertIsNone(s['anchor_recall'])
        self.assertEqual(s['negative_empty'],1)
