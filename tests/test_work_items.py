import copy
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock,patch
from work_items import WorkStore,runtime_models
from graph_context import graph_status


class WorkTests(unittest.TestCase):
    def test_table_presentation_export_preserves_human_edits(self):
        second=dict(text='A second supported statement.',sources=['S1'])
        self.result['claims'].append(second)
        self.result['answer_blocks']=[dict(type='table',columns=['Evidence 1','Evidence 2'],claims=self.result['claims'])]
        item=self.generate()
        self.assertIn('| Evidence 1 | Evidence 2 |',self.store.export(item['id'],self.engine))
        item=self.store.edit(item['id'],dict(revision=item['revision'],text='Human wording [S1]'),self.engine)
        exported=self.store.export(item['id'],self.engine)
        self.assertIn('## Documented findings\n\nHuman wording [S1]',exported)
        self.assertNotIn('| Evidence 1 | Evidence 2 |',exported)
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path=Path(self.temp.name)/'work.sqlite3'
        self.store=WorkStore(self.path)
        self.result=dict(response_status='draft',sources=[dict(citation='S1',document_id='a',page=1,text='Only verified merchants qualify.',title='Test')],
            claims=[dict(text='Only verified merchants qualify.',sources=['S1'])],warnings=[],flagged_claims=[])
        self.engine=SimpleNamespace(config={'generation_model':'test'},fingerprint='one',evidence_graph=None,
            by_id={'a':dict(id='a',availability='converted'),'b':dict(id='b',availability='converted')},
            pages=[dict(document_id='a',text='Only verified merchants qualify.')],answer=Mock(side_effect=lambda p:copy.deepcopy(self.result)))
        self.item=self.store.create(dict(query='Who qualifies?'),self.engine)

    def generate(self,item=None):
        item=item or self.item
        return self.store.generate(item['id'],item['revision'],self.engine)

    def review(self,item,decision,**extra):
        return self.store.review(item['id'],dict(revision=item['revision'],decision=decision,**extra),self.engine)

    def approved(self):
        item=self.review(self.generate(),'submit')
        return self.review(item,'approve',reviewer='Reviewer',note='Checked original and scope.',sources_verified=True,qualifications_verified=True)

    def test_full_lifecycle_and_export(self):
        item=self.approved()
        self.assertEqual(item['state'],'Approved')
        text=self.store.export(item['id'],self.engine)
        for part in ('Approved','[S1]','Only verified merchants','Reviewer','Snapshot'):
            self.assertIn(part,text)

    def test_approved_edit_creates_new_draft_preserves_history(self):
        item=self.approved()
        edited=self.store.edit(item['id'],dict(revision=item['revision'],text='Verified merchants only [S1].'),self.engine)
        self.assertEqual(edited['state'],'Draft')
        self.assertEqual(edited['version'],item['version']+1)
        self.assertEqual(edited['versions'][-2]['text'],item['draft']['text'])
        self.assertTrue(any(x['action']=='approve' for x in edited['history']))

    def test_stale_edit_does_not_overwrite(self):
        old=self.generate()
        self.review(old,'submit')
        with self.assertRaisesRegex(ValueError,'changed'):
            self.store.edit(old['id'],dict(revision=old['revision'],text='Different [S1]'),self.engine)

    def test_changed_source_invalidates_approval_on_export(self):
        item=self.approved()
        self.engine.pages[0]['text']='New qualification.'
        self.assertIn('Needs revalidation',self.store.export(item['id'],self.engine))
        fresh=self.store.get(item['id'],self.engine)
        with self.assertRaises(ValueError):self.review(fresh,'submit')

    def test_new_corpus_invalidates_even_if_cited_page_unchanged(self):
        item=self.approved();self.engine.fingerprint='new'
        self.assertEqual(self.store.get(item['id'],self.engine)['state'],'Needs revalidation')

    def test_regeneration_refreshes_stale_snapshot(self):
        item=self.approved();self.engine.fingerprint='new'
        item=self.store.get(item['id'],self.engine)
        item=self.generate(item)
        self.assertEqual(item['state'],'Draft')
        self.assertEqual(item['draft']['snapshot']['corpus'],'new')

    def test_unknown_or_missing_citations_rejected(self):
        item=self.generate()
        for text in ('Uncited claim','Claim [S99]'):
            with self.subTest(text=text),self.assertRaises(ValueError):
                self.store.edit(item['id'],dict(revision=item['revision'],text=text),self.engine)

    def test_review_requires_attestation_and_name(self):
        item=self.review(self.generate(),'submit')
        for extra in ({},dict(reviewer='Reader',note='ok'),dict(reviewer='',note='ok',sources_verified=True,qualifications_verified=True)):
            with self.subTest(extra=extra),self.assertRaises(ValueError):self.review(item,'approve',**extra)

    def test_rejected_version_can_be_edited_not_approved(self):
        item=self.review(self.generate(),'submit')
        item=self.review(item,'reject',reviewer='Reader',note='Qualification incomplete.')
        with self.assertRaises(ValueError):self.review(item,'approve',reviewer='Reader',note='ok',sources_verified=True,qualifications_verified=True)
        self.assertEqual(self.store.edit(item['id'],dict(revision=item['revision'],text='Corrected [S1]'),self.engine)['state'],'Draft')

    def test_impact_requires_sources_and_separates_actions(self):
        with self.assertRaises(ValueError):self.store.create(dict(kind='impact',query='What changed?'),self.engine)
        item=self.store.create(dict(kind='impact',query='What changed?',document_ids=['b','a']),self.engine)
        item=self.generate(item)
        sent=self.engine.answer.call_args.args[0]
        self.assertEqual(sent['document_ids'],['b','a'])
        self.assertEqual(sent['route'],'compare')
        self.assertIn('do not assume',sent['query'])
        self.assertIn('Analyst-proposed actions',self.store.export(item['id'],self.engine))
        self.assertIn('Not supplied',self.store.export(item['id'],self.engine))

    def test_clarification_creates_request_version(self):
        item=self.generate()
        request=dict(item['draft']['request'],query='Who qualifies under UPI?',series='UPI')
        item=self.store.edit(item['id'],dict(revision=item['revision'],request=request),self.engine)
        self.assertEqual(item['draft']['text'],'')
        self.assertFalse(item['draft']['result'])
        self.assertEqual(len(item['versions']),3)

    def test_empty_evidence_cannot_be_submitted(self):
        self.result.update(claims=[],sources=[],answer='No evidence.',response_status='abstained')
        with self.assertRaises(ValueError):self.review(self.generate(),'submit')

    def test_outage_does_not_erase_previous_version(self):
        item=self.generate();self.engine.answer.side_effect=TimeoutError('Offline')
        with self.assertRaises(TimeoutError):self.generate(item)
        after=self.store.get(item['id'],self.engine)
        self.assertFalse(after['busy'])
        self.assertEqual(after['draft'],item['draft'])

    def test_restart_marks_interrupted_generation(self):
        with self.store.connect() as db:db.execute('UPDATE work_items SET busy=1 WHERE id=?',(self.item['id'],))
        store=WorkStore(self.path)
        item=store.get(self.item['id'],self.engine)
        self.assertFalse(item['busy'])
        self.assertEqual(item['history'][-1]['action'],'interrupted')

    def test_graph_status_degraded_is_distinct_from_disabled(self):
        self.assertEqual(graph_status(self.engine)['status'],'disabled')
        self.engine.config['evidence_graph_path']='missing.json'
        self.engine.evidence_graph_error='Stale source'
        status=graph_status(self.engine)
        self.assertEqual(status['status'],'degraded')
        self.assertEqual(status['warning'],'Stale source')

    def test_read_during_stale_regeneration_does_not_cancel_result(self):
        item=self.approved()
        self.engine.fingerprint='new'
        def answer(payload):
            reading=self.store.get(item['id'],self.engine)
            self.assertTrue(reading['busy'])
            self.assertEqual(reading['revision'],item['revision']+1)
            return copy.deepcopy(self.result)
        self.engine.answer.side_effect=answer
        self.assertEqual(self.generate(item)['draft']['snapshot']['corpus'],'new')

    def test_impact_question_budget_reserves_instruction_space(self):
        with self.assertRaisesRegex(ValueError,'1,000'):
            self.store.create(dict(kind='impact',query='a'*1001,document_ids=['a','b']),self.engine)
        self.engine.by_id['a']['subject']='Long title '*500
        item=self.store.create(dict(kind='impact',query='a'*1000,document_ids=['a','b']),self.engine)
        self.generate(item)
        self.assertLess(len(self.engine.answer.call_args.args[0]['query']),2000)

    def test_model_digest_change_invalidates_saved_work(self):
        old=dict(status='available',digests={'test':'old-weights'})
        new=dict(status='available',digests={'test':'new-weights'})
        with patch('work_items.runtime_models',return_value=old):
            item=self.approved()
        with patch('work_items.runtime_models',return_value=new):
            self.assertEqual(self.store.get(item['id'],self.engine)['state'],'Needs revalidation')

    def test_metadata_unavailable_is_explicit_and_cannot_approve(self):
        with patch('work_items.runtime_models',return_value=dict(status='unavailable',digests={})):
            item=self.review(self.generate(),'submit')
            with self.assertRaisesRegex(ValueError,'fingerprints'):
                self.review(item,'approve',reviewer='Test',note='Test only',sources_verified=True,qualifications_verified=True)

    def test_runtime_model_inspection_rejects_remote_endpoint(self):
        self.engine.config['ollama_url']='https://unrelated.example'
        with patch('work_items.urllib.request.build_opener') as request:
            self.assertEqual(runtime_models(self.engine)['status'],'unavailable')
            request.assert_not_called()


if __name__=='__main__':unittest.main()
