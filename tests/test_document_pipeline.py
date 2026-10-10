import hashlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app import Engine
from tools import document_pipeline as pipeline


TEXT = '# Settlement guidelines\n' + 'Participants must review settlement reports daily and reconcile exceptions against their records before reporting operational issues. ' * 3


class IntakeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.cleanup_store)
        self.root = Path(self.temp.name)
        self.addCleanup(patch.stopall)
        patch.object(pipeline, 'ROOT', self.root).start()
        self.base = self.root / 'data/base'
        (self.base / 'sources').mkdir(parents=True)
        for name, value in [('index.json', []), ('review_annotations.json', []), ('feature_rules.json', []), ('source_manifest.json', {'hashes': {}})]:
            pipeline.write(self.base / name, value)
        (self.base / 'all_circular_pages.jsonl').write_text('')
        self.active = self.root / 'config.json'
        pipeline.write(self.active, dict(data_dir=str(self.base), vector_backend='chroma', embedding_model='test:embed',
                                       chunker_version='clauses-v1', review_overlays=True, reranker_enabled=False,
                                       source_pack=str(self.root / 'originals')))
        self.before = self.active.read_bytes()
        self.source = self.root / 'source.md'
        self.source.write_text(TEXT, encoding='utf-8')
        self.item = dict(id='test:settlement:2026', file='source.md', title='Settlement guidelines', issuer='Test authority',
                         document_type='Directions', reference='SET-2026', products=['Payments'],
                         source_url='https://example.org/settlement', retrieved_on='2026-10-09')
        self.manifest = self.root / 'intake.json'

    def cleanup_store(self):
        # Chroma caches persistent clients; release only this test's handles on Windows.
        from chromadb.api.shared_system_client import SharedSystemClient
        for key, system in list(SharedSystemClient._identifier_to_system.items()):
            if str(key).startswith(str(self.root)):
                system.stop()
                del SharedSystemClient._identifier_to_system[key]
        self.temp.cleanup()

    def prepare(self, name='test-one', item=None):
        pipeline.write(self.manifest, dict(schema_version=1, documents=[item or self.item]))
        return pipeline.prepare(self.manifest, name)

    def mock_model(self):
        patch.object(Engine, 'model_digest', return_value='test-digest').start()
        def embed(engine, endpoint, payload):
            self.assertEqual(endpoint, '/api/embed')
            texts = payload['input'] if isinstance(payload['input'], list) else [payload['input']]
            return {'embeddings': [[1 + b for b in hashlib.sha256(t.encode()).digest()[:8]] for t in texts]}
        return patch.object(Engine, 'ollama', autospec=True, side_effect=embed).start()

    def test_prepare_keeps_active_and_provenance(self):
        self.prepare()
        self.assertEqual(self.before, self.active.read_bytes())
        target = pipeline.release_path('test-one')
        doc = pipeline.read(target/'index.json')[0]
        self.assertEqual(doc['issuer'], 'Test authority')
        self.assertEqual(doc['source_sha256'], pipeline.sha(self.source.read_bytes()))
        self.assertFalse(doc['source_coverage']['page_count_verified'])
        from product_scope import source_coverage
        e = Engine(config=dict(pipeline.read(target/'candidate_config.json'), vector_backend='json'))
        self.assertEqual(source_coverage(e, doc['id'])['page_basis'], 'logical_markdown')
        pipeline.check_candidate(target)

    def test_corrupt_source_blocks_build(self):
        self.prepare()
        target = pipeline.release_path('test-one')
        next((target/'sources/intake').glob('*.md')).write_text('tampered')
        with self.assertRaisesRegex(ValueError, 'changed'):
            pipeline.build('test-one')
        self.assertEqual(self.before, self.active.read_bytes())

    def test_jsonl_preserves_unicode_line_separators(self):
        text = 'Source text\u2028still inside one JSON record\u2029with two separators.'
        (self.base/'all_circular_pages.jsonl').write_text(json.dumps({'document_id':'legacy', 'source_page':1, 'text':text}, ensure_ascii=False)+'\n', encoding='utf-8')
        self.prepare()
        rows = (pipeline.release_path('test-one')/'all_circular_pages.jsonl').read_text(encoding='utf-8').split('\n')
        self.assertEqual(json.loads(rows[0])['text'], text)

    def test_malformed_markers_and_preamble_rejected(self):
        for text in ('<!-- Page 2 -->Text', '<!-- Page 1 -->A<!-- Page 1 -->B', 'Lost content<!-- Page 1 -->A'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                pipeline.extract(text.encode(), '.md')

    def test_thin_and_blank_pages_quarantined(self):
        self.source.write_text('<!-- Page 1 -->'+TEXT+'<!-- Page 2 -->', encoding='utf-8')
        self.prepare()
        doc = pipeline.read(pipeline.release_path('test-one')/'index.json')[0]
        self.assertEqual(doc['availability'], 'needs_source_review')
        self.assertEqual(doc['source_coverage']['empty_pages'], [2])

    def test_partial_opt_in_preserves_coverage(self):
        self.source.write_text('<!-- Page 1 -->'+TEXT+'<!-- Page 2 -->', encoding='utf-8')
        self.item['allow_partial'] = True
        self.prepare()
        target = pipeline.release_path('test-one')
        e = Engine(config=pipeline.read(target/'candidate_config.json'))
        self.assertTrue(e.parts)
        self.assertEqual(e.parts[0]['issuer'], self.item['issuer'])
        self.assertEqual(e.parts[0]['source_coverage']['empty_pages'], [2])

    def test_blank_pdf_detected_without_fake_ocr(self):
        from pypdf import PdfWriter
        writer = PdfWriter(); writer.add_blank_page(width=300, height=300)
        buf = io.BytesIO(); writer.write(buf)
        pages, method, physical = pipeline.extract(buf.getvalue(), '.pdf')
        self.assertEqual(pages, [(1, '')])
        self.assertEqual(method, 'pypdf')
        self.assertTrue(physical)

    def test_build_resume_reuses_embeddings_activate_rollback(self):
        self.prepare()
        model = self.mock_model()
        first = pipeline.build('test-one')
        self.assertGreater(first['embeddings']['computed'], 0)
        count = model.call_count
        second = pipeline.build('test-one')
        self.assertEqual(second['embeddings']['computed'], 0)
        self.assertEqual(model.call_count, count)
        pipeline.activate('test-one')
        self.assertEqual(pipeline.read(self.active)['data_dir'], str(pipeline.release_path('test-one')))
        with self.assertRaisesRegex(ValueError, 'active release'):
            pipeline.build('test-one')
        pipeline.rollback('test-one')
        self.assertEqual(pipeline.read(self.active), json.loads(self.before))

    def test_embedding_failure_never_activates(self):
        self.prepare()
        patch.object(Engine, 'model_digest', return_value='test-digest').start()
        patch.object(Engine, 'ollama', side_effect=ConnectionError('Ollama unavailable')).start()
        with self.assertRaises(ConnectionError):
            pipeline.build('test-one')
        self.assertEqual(self.before, self.active.read_bytes())
        with self.assertRaisesRegex(ValueError, 'Build and validate'):
            pipeline.activate('test-one')

    def test_live_review_changes_block_activation(self):
        self.prepare(); self.mock_model(); pipeline.build('test-one')
        pipeline.write(self.base/'review_annotations.json', [{'id':'new-review'}])
        with self.assertRaisesRegex(ValueError, 'changed'):
            pipeline.activate('test-one')
        self.assertEqual(self.before, self.active.read_bytes())

    def test_model_digest_change_blocks_activation(self):
        self.prepare(); self.mock_model(); pipeline.build('test-one')
        with patch.object(Engine, 'model_digest', return_value='new-digest'):
            with self.assertRaisesRegex(ValueError, 'Embedding model changed'):
                pipeline.activate('test-one')

    def test_repeated_intake_is_noop(self):
        self.prepare(); self.mock_model(); pipeline.build('test-one'); pipeline.activate('test-one')
        result = self.prepare('test-two')
        self.assertEqual(result['status'], 'unchanged')
        self.assertFalse(pipeline.release_path('test-two').exists())

    def test_id_conflict_and_duplicate_content_rejected(self):
        self.prepare(); self.mock_model(); pipeline.build('test-one'); pipeline.activate('test-one')
        duplicate = dict(self.item, id='test:duplicate', source_url='https://example.org/other')
        with self.assertRaisesRegex(ValueError, 'Identical file'):
            self.prepare('test-two', duplicate)
        self.source.write_text(TEXT+'Different text', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Existing id'):
            self.prepare('test-three')

    def test_revision_archives_only_local_snapshot(self):
        self.prepare(); self.mock_model(); pipeline.build('test-one'); pipeline.activate('test-one')
        digest = pipeline.sha(self.source.read_bytes())
        self.source.write_text(TEXT+' Revised requirements apply to settlement participants.', encoding='utf-8')
        new = dict(self.item, id='test:settlement:v2', revision_of=self.item['id'], expected_previous_sha256=digest)
        self.prepare('test-two', new)
        e = Engine(config=pipeline.read(pipeline.release_path('test-two')/'candidate_config.json'))
        self.assertEqual(e.by_id[self.item['id']]['availability'], 'archived_snapshot')
        self.assertFalse(e.parts_by_doc[self.item['id']])
        self.assertTrue(e.parts_by_doc[new['id']])
        self.assertFalse(e.registry.edges)  # No invented legal relationship.

    def test_missing_revision_declaration_rejected(self):
        self.prepare(); self.mock_model(); pipeline.build('test-one'); pipeline.activate('test-one')
        self.source.write_text(TEXT+'Changed text', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Source URL already'):
            self.prepare('test-two', dict(self.item, id='test:changed'))

    def test_release_traversal_rejected(self):
        with self.assertRaises(ValueError):
            self.prepare('../outside')

    def test_compact_dates_and_nonboolean_partial_rejected(self):
        for change in ({'retrieved_on':'20261009'}, {'allow_partial':1}, {'revision_of':[]}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                self.prepare(item=dict(self.item, **change))

    def test_applicability_preserves_exact_source_quote(self):
        self.item['applicability']=dict(entities=['participant banks'],page=1,quote='Participants must review settlement reports daily')
        self.prepare()
        doc=pipeline.read(pipeline.release_path('test-one')/'index.json')[0]
        self.assertEqual(doc['applicability']['entities'],['participant banks'])
        self.assertIn('not_independently_verified',doc['applicability']['basis'])

    def test_applicability_quote_must_match_page(self):
        self.item['applicability']=dict(entities=['banks'],page=2,quote='Invented scope')
        with self.assertRaisesRegex(ValueError,'Applicability quote'):
            self.prepare()

    def test_source_notes_are_preserved_for_reader(self):
        self.item['source_notes']=['Official HTML; physical PDF not acquired.']
        self.prepare()
        doc=pipeline.read(pipeline.release_path('test-one')/'index.json')[0]
        self.assertIn(self.item['source_notes'][0],doc['notes'])

    def test_source_notes_reject_non_text(self):
        for notes in ('one note',[None],['']):
            with self.subTest(notes=notes), self.assertRaisesRegex(ValueError,'source_notes'):
                self.prepare(item=dict(self.item,source_notes=notes))


if __name__ == '__main__':
    unittest.main()
