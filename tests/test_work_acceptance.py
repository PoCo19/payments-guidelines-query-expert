import csv
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from evaluation.workbench_acceptance import validate


class AcceptanceGateTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        cases=[dict(id=f'{prefix}-{i}',review_status='independently_reviewed',reviewer='Synthetic test reviewer',
                    originals_verified=True,expected_outcome='Synthetic expectation',essential_qualifications=[],references=[])
               for prefix,count in [('QD',20),('IB',10),('NC',20)] for i in range(count)]
        self.data=self.root/'cases.json';self.data.write_text(json.dumps(dict(cases=cases)))
        self.manifest=dict(dataset_sha256=hashlib.sha256(self.data.read_bytes()).hexdigest(),review_gate='approved',scoring_allowed=True)
        (self.root/'manifest.json').write_text(json.dumps(self.manifest))
        for filename,count,field in [('graph_anchors.csv',55,'verified'),('graph_relationships.csv',13,'approved')]:
            with (self.root/filename).open('w',newline='') as f:
                writer=csv.writer(f);writer.writerow(['reviewer',field])
                writer.writerows([['Synthetic test reviewer','yes']]*count)

    def test_review_gate_passes_only_attributed_frozen_fixture(self):
        self.assertEqual(validate(self.root)[2],[])
        (self.root/'graph_relationships.csv').write_text('reviewer,approved\n,no\n')
        self.assertTrue(any('13' in e for e in validate(self.root)[2]))

    def test_unreviewed_manifest_and_changed_questions_are_blocked(self):
        self.manifest.update(review_gate='pending',scoring_allowed=False)
        (self.root/'manifest.json').write_text(json.dumps(self.manifest))
        self.data.write_text(self.data.read_text()+' ')
        errors=validate(self.root)[2]
        self.assertTrue(any('fingerprint' in e for e in errors))
        self.assertTrue(any('pending' in e for e in errors))
