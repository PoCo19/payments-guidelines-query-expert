import json
import os
from pathlib import Path
import tempfile
import unittest
import zipfile
from tools.handoff import restore, verify_package, sha


class HandoffTests(unittest.TestCase):
    def package(self, root, name='index.json'):
        package = root / 'package'
        package.mkdir()
        raw = b'[]\n'
        with zipfile.ZipFile(package / 'sources.zip', 'w') as z:
            z.writestr(name, raw)
        manifest = dict(archive_sha256=sha((package/'sources.zip').read_bytes()),
                        files={name:dict(sha256=sha(raw), bytes=len(raw))})
        (package/'manifest.json').write_text(json.dumps(manifest))
        return package

    def test_restore_idempotent_and_preserves_edits(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); package = self.package(root); dest = root/'restored'
            restore(dest, package); restore(dest, package)
            (dest/'index.json').write_text('edited')
            with self.assertRaisesRegex(ValueError, 'changed'):
                restore(dest, package)
            self.assertEqual((dest/'index.json').read_text(), 'edited')

    def test_tampered_archive_rejected_before_restore(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); package = self.package(root)
            with (package/'sources.zip').open('ab') as f: f.write(b'tampered')
            with self.assertRaisesRegex(ValueError, 'checksum'):
                restore(root/'restored', package)
            self.assertFalse((root/'restored').exists())

    def test_traversal_absolute_and_windows_paths_rejected(self):
        for name in ['../escape', '/escape', 'C:/escape', 'folder\\escape', 'a/./b']:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                package = self.package(Path(tmp), name)
                with self.assertRaisesRegex(ValueError, 'Unsafe'):
                    verify_package(package)

    def test_bad_member_hash_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            package = self.package(Path(tmp))
            manifest = json.loads((package/'manifest.json').read_text())
            manifest['files']['index.json']['sha256'] = '0'*64
            (package/'manifest.json').write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError, 'member checksum'):
                verify_package(package)

    @unittest.skipUnless(os.name == 'nt', 'Windows path limit guard')
    def test_long_destination_rejected_before_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); package = self.package(root)
            dest = root / ('x' * 200) / 'restored'
            with self.assertRaisesRegex(ValueError, 'shorter folder'):
                restore(dest, package)
            self.assertFalse(dest.parent.exists())


if __name__ == '__main__': unittest.main()
