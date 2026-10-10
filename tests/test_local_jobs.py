import base64
import threading
import time
import unittest
from types import SimpleNamespace
from unittest.mock import patch
from tests import test_document_pipeline as fixture
from local_jobs import LocalJobs, BusyError
from tools import document_pipeline as pipeline


class LocalJobTests(unittest.TestCase):
    cleanup_store=fixture.IntakeTests.cleanup_store
    def setUp(self):
        fixture.IntakeTests.setUp(self)
        self.engine=SimpleNamespace(docs=[])
        self.jobs=LocalJobs(lambda:self.engine,lambda e:setattr(self,'engine',e),self.active)
        self.payload=dict(filename='../escape.md',data_base64=base64.b64encode(fixture.TEXT.encode()).decode(),metadata=self.item)

    def test_upload_is_staged_and_path_is_not_trusted(self):
        result=self.jobs.upload(self.payload)
        self.assertEqual(self.before,self.active.read_bytes())
        self.assertEqual(result['metadata']['file'],'source.md')
        self.assertTrue((self.jobs.upload_root/result['token']/'source.md').exists())
        self.assertFalse((self.root/'escape.md').exists())
        self.assertFalse(result['physical_pages'])

    def test_upload_rejects_bad_encoding_and_fake_pdf(self):
        for payload in [dict(self.payload,data_base64='!!'),dict(self.payload,filename='fake.pdf')]:
            with self.assertRaises(ValueError):self.jobs.upload(payload)

    def test_duplicate_source_cannot_prepare(self):
        self.engine.docs=[dict(id='old',subject='old',source_pdf=self.item['source_url'])]
        result=self.jobs.upload(self.payload)
        with self.assertRaisesRegex(ValueError,'Duplicate'):self.jobs.prepare([result['token']])

    def test_changed_upload_cannot_prepare(self):
        result=self.jobs.upload(self.payload)
        (self.jobs.upload_root/result['token']/'source.md').write_text('changed')
        with self.assertRaisesRegex(ValueError,'changed'):self.jobs.prepare([result['token']])

    def test_prepare_keeps_active_and_scopes_releases(self):
        result=self.jobs.upload(self.payload);prepared=self.jobs.prepare([result['token']])
        self.assertEqual(self.before,self.active.read_bytes())
        self.assertEqual(prepared['preview']['documents'][0]['availability'],'converted')
        self.assertEqual(len(self.jobs.releases()),1)
        other=LocalJobs(lambda:self.engine,lambda e:None,self.root/'other.json')
        self.assertEqual(other.releases(),[])
        with self.assertRaisesRegex(ValueError,'different app'):other.preview(prepared['release'])

    def test_quarantined_document_cannot_activate(self):
        upload=self.jobs.upload(dict(self.payload,data_base64=base64.b64encode(b'Thin').decode()))
        result=self.jobs.prepare([upload['token']])
        with self.assertRaisesRegex(ValueError,'No newly searchable'):self.jobs.activate(result['release'])
        self.assertEqual(self.before,self.active.read_bytes())

    def test_serial_worker_reports_failures_and_releases_gate(self):
        entered=threading.Event();finish=threading.Event()
        def work(update):entered.set();finish.wait(3);raise ValueError('fixture failure')
        job=self.jobs.start('test',work);self.assertTrue(entered.wait(1))
        with self.assertRaises(BusyError):self.jobs.start('second',lambda u:None)
        finish.set()
        for _ in range(100):
            if self.jobs.get(job['id'])['status']=='failed':break
            time.sleep(.01)
        self.assertEqual(self.jobs.get(job['id'])['error'],'fixture failure')
        self.assertFalse(self.jobs.gate.locked())

    def test_bad_tokens_and_revision_upload_rejected(self):
        for tokens in [[],['../../outside'],['a'*32]*2]:
            with self.assertRaises(ValueError):self.jobs.prepare(tokens)
        with self.assertRaises(ValueError):self.jobs.upload(dict(self.payload,metadata=dict(self.item,revision_of='prior')))
