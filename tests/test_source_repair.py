import unittest
from unittest.mock import patch
from tools.repair_oc185b_source import corrected_page,OLD,NEW
from tools.document_pipeline import sha


class SourceRepairTests(unittest.TestCase):
    def test_repair_is_exact_and_preserves_raw_text(self):
        raw='Before. '+OLD+' A separate provision is unchanged.'
        with patch('tools.repair_oc185b_source.EXPECTED_PAGE',sha(raw.encode())):
            page={'text':raw,'source_page':1,'document_id':'2025-OC-185B'}
            result=corrected_page(page)
        self.assertEqual(result['text'],raw.replace(OLD,NEW))
        self.assertEqual(result['raw_extracted_text'],raw)
        self.assertEqual(page['text'],raw)

    def test_changed_source_and_duplicate_anchor_are_rejected(self):
        with self.assertRaisesRegex(ValueError,'re-review'):corrected_page({'text':'unknown'})
        raw=OLD+' '+OLD
        with patch('tools.repair_oc185b_source.EXPECTED_PAGE',sha(raw.encode())):
            with self.assertRaisesRegex(ValueError,'re-review'):corrected_page({'text':raw})
