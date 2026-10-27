"""Workflow product controls; no live corpus/model mutation."""
import copy
import unittest
from types import SimpleNamespace
from unittest.mock import Mock
from tests import test_work_items as fixture
from work_items import related_sources, snapshot


class WorkbenchProductTests(unittest.TestCase):
    setUp = fixture.WorkTests.setUp
    generate = fixture.WorkTests.generate
    review = fixture.WorkTests.review
    approved = fixture.WorkTests.approved

    def job(self):
        return dict(status='completed',result=copy.deepcopy(self.result),research_request=dict(query='Who qualifies?',mode='generate',method='bm25',rerank=False,scope='strict',entity='bank',fiscal_year='2026-27',feature='test'),research_snapshot=snapshot(self.engine,self.result))

    def test_archive_trash_restore_preserves_approved_history(self):
        item=self.approved()
        for disposition in ('archived','trash','active'):
            item=self.store.visibility(item['id'],dict(revision=item['revision'],disposition=disposition),self.engine)
            self.assertEqual(item['state'],'Approved')
            self.assertEqual(item['disposition'],disposition)
            self.assertEqual(item['version'],2)
        self.assertTrue(any(h['action']=='approve' for h in item['history']))
        self.assertEqual(self.store.list(self.engine)[0]['disposition'],'active')

    def test_hidden_items_cannot_generate_edit_or_review(self):
        item=self.generate()
        item=self.store.visibility(item['id'],dict(revision=item['revision'],disposition='trash'),self.engine)
        for operation in (lambda:self.generate(item),lambda:self.review(item,'submit'),lambda:self.store.edit(item['id'],dict(revision=item['revision'],text='Only merchants [S1].'),self.engine)):
            with self.assertRaisesRegex(ValueError,'Restore'):operation()
        self.assertIn('Location: trash',self.store.export(item['id'],self.engine))

    def test_restore_rechecks_stale_approval(self):
        item=self.approved()
        item=self.store.visibility(item['id'],dict(revision=item['revision'],disposition='archived'),self.engine)
        self.engine.fingerprint='changed'
        stale=self.store.get(item['id'],self.engine)
        self.assertEqual(stale['state'],'Needs revalidation')
        with self.assertRaisesRegex(ValueError,'changed'):
            self.store.visibility(item['id'],dict(revision=item['revision'],disposition='active'),self.engine)
        restored=self.store.visibility(item['id'],dict(revision=stale['revision'],disposition='active'),self.engine)
        self.assertEqual(restored['state'],'Needs revalidation')

    def test_visibility_rejects_busy_and_invalid_destination(self):
        with self.store.connect() as db:db.execute('UPDATE work_items SET busy=1 WHERE id=?',(self.item['id'],))
        with self.assertRaisesRegex(ValueError,'running'):
            self.store.visibility(self.item['id'],dict(revision=1,disposition='trash'),self.engine)
        with self.assertRaisesRegex(ValueError,'Choose'):
            self.store.visibility(self.item['id'],dict(revision=1,disposition='destroy'),self.engine)

    def test_import_preserves_server_evidence_and_all_retrieval_settings(self):
        job=self.job();item=self.store.import_answer(job,self.engine)
        self.engine.answer.assert_not_called()
        self.assertEqual(item['draft']['result'],job['result'])
        self.assertEqual(item['draft']['snapshot'],job['research_snapshot'])
        self.assertEqual(item['state'],'Draft')
        generated=self.generate(item)
        request=self.engine.answer.call_args.args[0]
        for field in ('method','rerank','scope','entity','fiscal_year','feature'):
            self.assertEqual(request[field],job['research_request'][field])
        self.assertEqual(generated['draft']['origin_request'],job['research_request'])
        self.assertIn('Original research settings',self.store.export(item['id'],self.engine))

    def test_import_rejects_stale_clarification_excerpts_and_unknown_citations(self):
        job=self.job();job['research_snapshot']['corpus']='old'
        with self.assertRaisesRegex(ValueError,'changed'):self.store.import_answer(job,self.engine)
        for field,value in [('status','running'),('research_snapshot',None)]:
            job=self.job();job[field]=value
            with self.assertRaisesRegex(ValueError,'completed'):self.store.import_answer(job,self.engine)
        for result in (dict(self.result,claims=[]),dict(self.result,sources=[])):
            job=self.job();job['result']=result
            with self.assertRaisesRegex(ValueError,'cited answer'):self.store.import_answer(job,self.engine)
        job=self.job();job['research_request']['mode']='evidence'
        with self.assertRaisesRegex(ValueError,'cited answer'):self.store.import_answer(job,self.engine)
        job=self.job();job['result']['claims'][0]['sources']=['S99']
        with self.assertRaisesRegex(ValueError,'unknown citation'):self.store.import_answer(job,self.engine)

    def test_import_question_revision_retains_original_scope_filters(self):
        item=self.store.import_answer(self.job(),self.engine)
        item=self.store.edit(item['id'],dict(revision=item['revision'],request=dict(item['draft']['request'],query='Which merchants qualify?')),self.engine)
        self.assertEqual(item['draft']['text'],'')
        self.generate(item)
        request=self.engine.answer.call_args.args[0]
        self.assertEqual(request['query'],'Which merchants qualify?')
        self.assertEqual(request['entity'],'bank')
        self.assertEqual(request['scope'],'strict')

    def test_audience_validation_and_export(self):
        item=self.store.create(dict(query='Who qualifies?',audience='Operations'),self.engine)
        self.assertIn('Operations',self.store.export(item['id'],self.engine))
        for audience in (42,'x'*121):
            with self.assertRaisesRegex(ValueError,'Audience'):self.store.create(dict(query='Question',audience=audience),self.engine)

    def test_impact_labels_are_analyst_annotations_and_clear_on_text_edit(self):
        item=self.store.create(dict(kind='impact',query='What changed?',document_ids=['a','b']),self.engine)
        item=self.generate(item)
        item=self.store.edit(item['id'],dict(revision=item['revision'],finding_labels={'0':'retained'}),self.engine)
        self.assertEqual(item['draft']['finding_labels'],{'0':'retained'})
        self.assertIn('Retained requirement: Only verified merchants qualify.',self.store.export(item['id'],self.engine))
        with self.assertRaisesRegex(ValueError,'classification'):
            self.store.edit(item['id'],dict(revision=item['revision'],finding_labels={'99':'change'}),self.engine)
        edited=self.store.edit(item['id'],dict(revision=item['revision'],text='Reworded finding [S1].'),self.engine)
        self.assertEqual(edited['draft']['finding_labels'],{})

    def test_related_sources_keep_relationship_evidence_and_unknown_dates(self):
        self.engine.by_id={
            'seed':dict(id='seed',series='UPI',family='115',issue_date='2026-01-01',availability='converted'),
            'older':dict(id='older',series='UPI',family='115',issue_date='2025-01-01',availability='converted'),
            'future':dict(id='future',series='UPI',family='115',issue_date='2026-02-01',availability='converted'),
            'unknown':dict(id='unknown',series='RBI',availability='converted'),
            'unavailable':dict(id='unavailable',series='UPI',family='115',availability='missing'),
            'other-product':dict(id='other-product',series='RuPay',family='115',availability='converted')}
        self.engine.registry=SimpleNamespace(neighboring_documents=Mock(return_value=[('unknown','references_seed',dict(evidence_status='metadata_only'))]))
        rows=related_sources(self.engine,'seed')
        self.assertEqual({r['document']['id'] for r in rows},{'older','future','unknown'})
        self.assertEqual(rows[0]['document']['id'],'older')
        unknown=next(r for r in rows if r['document']['id']=='unknown')
        self.assertEqual(unknown['chronology'],'date not established')
        self.assertIn('source text not verified',unknown['reasons'][0])
        self.assertEqual(next(r for r in rows if r['document']['id']=='future')['chronology'],'later')
        with self.assertRaisesRegex(ValueError,'not found'):related_sources(self.engine,'missing')

if __name__=='__main__':unittest.main()
