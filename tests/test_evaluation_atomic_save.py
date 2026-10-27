import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from evaluation.ragas_runner import save


class AtomicSaveTests(unittest.TestCase):
    def test_transient_reader_lock_preserves_then_replaces_complete_capture(self):
        with tempfile.TemporaryDirectory() as directory:
            target=Path(directory)/'capture.json'
            target.write_text('{"old":true}')
            original=Path.replace; attempts=[]
            def replace(source,destination):
                attempts.append(1)
                if len(attempts)<3:
                    self.assertEqual(json.loads(target.read_text()),{'old':True})
                    raise PermissionError('test reader lock')
                return original(source,destination)
            with patch.object(Path,'replace',replace),patch('evaluation.ragas_runner.time.sleep'):
                save(target,{'new':[1,2,3]})
            self.assertEqual(json.loads(target.read_text()),{'new':[1,2,3]})
            self.assertFalse(target.with_suffix('.json.pending').exists())

    def test_persistent_lock_raises_and_retains_old_capture_and_pending(self):
        with tempfile.TemporaryDirectory() as directory:
            target=Path(directory)/'capture.json';target.write_text('{"old":true}')
            with patch.object(Path,'replace',side_effect=PermissionError('locked')),patch('evaluation.ragas_runner.time.sleep'):
                with self.assertRaises(PermissionError):save(target,{'new':True})
            self.assertEqual(json.loads(target.read_text()),{'old':True})
            self.assertEqual(json.loads(target.with_suffix('.json.pending').read_text()),{'new':True})
