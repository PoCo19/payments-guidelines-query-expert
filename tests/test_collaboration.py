"""Portable config selection must not replace a user's local override."""
import json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
import app

class CollaborationConfigTests(unittest.TestCase):
 def test_fresh_clone_and_local_override(self):
  with tempfile.TemporaryDirectory() as folder:
   root=Path(folder);example=root/'config.example.json';example.write_text('{}')
   with patch.object(app,'ROOT',root):
    self.assertEqual(app.default_config_path(),example)
    local=root/'config.json';local.write_text('{"generation_model":"personal"}')
    self.assertEqual(app.default_config_path(),local)
    self.assertEqual(json.loads(local.read_text())['generation_model'],'personal')
