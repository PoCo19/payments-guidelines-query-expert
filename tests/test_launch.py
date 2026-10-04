"""Workflow invariants and actual HTTP contract, independent of Ollama availability."""
import copy
import io
import json
import tempfile
import threading
import unittest
import urllib.request
import urllib.error
from pathlib import Path
from http.server import ThreadingHTTPServer
from unittest.mock import patch
from launch_orchestrator.core import Store, Conflict, team_input
from launch_orchestrator.demo import create_demo
from launch_orchestrator.generation import Worker, template_pack, generate
from launch_app import Application, handler_for


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.store=Store(Path(self.temp.name)/'launch.db')
        self.w=create_demo(self.store,'Tester')

    def tearDown(self): self.temp.cleanup()

    def action(self,action,**kw):
        self.w=self.store.mutate(self.w['id'],{'actor':'Tester','role':'product','revision':self.w['revision'],'action':action,**kw});return self.w

    def approve(self): self.action('facts_approve',note='Checked exact quotations and scope')

    def generate(self,team='cs'):
        self.store.enqueue(self.w['id'],{'actor':'Tester','role':'product','revision':self.w['revision'],'kind':'generate','team':team,'mode':'template'})
        job=self.store.take_job();self.store.finish_job(job,template_pack(job['request']['snapshot'],team));self.w=self.store.get(self.w['id']);return job

    def complete(self):
        self.approve()
        for team in ('cs','marketing','bd','risk'):
            self.generate(team);self.action('artifact_review',team=team,decision='approved',note='Reviewed simulated output')
        for team in ('risk','cs','marketing','bd'):
            t=next(t for t in self.w['tasks'] if t['team']==team)
            self.action('task_save',**{**t,'status':'done','owner':'Test owner','evidence':'Simulated completion evidence'})

    def test_full_journey_and_export(self):
        self.complete();self.assertTrue(self.w['readiness']['ready'])
        self.action('launch_decide',note='Simulated pilot approved for demonstration')
        self.assertEqual(self.w['decision']['status'],'recorded')
        text=self.store.export(self.w['id']);self.assertIn('SIMULATED CAPSTONE',text);self.assertIn('Customer Success',text)

    def test_no_launch_without_gates(self):
        with self.assertRaises(ValueError):self.action('launch_decide',note='Attempt early launch')

    def test_fact_change_reopens_all(self):
        self.complete();self.action('launch_decide',note='Reviewed')
        f=self.w['facts'][0];self.action('fact_save',**{**f,'value':f['value']+' Review scope again.'})
        self.assertFalse(self.w['facts_approved']);self.assertTrue(all(a['status']=='stale' for a in self.w['artifacts'].values()))
        self.assertTrue(all(t['status']=='todo' for t in self.w['tasks']));self.assertEqual(self.w['decision']['status'],'requires_review')

    def test_control_change_scoped_and_dependency_cascades(self):
        self.complete();c=self.w['controls'][0]
        self.action('control_save',**{**c,'scope':'Updated test scope'})
        self.assertEqual(self.w['artifacts']['risk']['status'],'stale');self.assertEqual(self.w['artifacts']['bd']['status'],'approved')
        self.assertEqual(next(t for t in self.w['tasks'] if t['team']=='bd')['status'],'todo')
        self.assertEqual(self.w['artifacts']['marketing']['status'],'approved');self.assertTrue(self.w['facts_approved'])

    def test_partner_change_only_bd(self):
        self.complete();p=self.w['partners'][0];self.action('partner_save',**{**p,'stage':'interested'})
        self.assertEqual(self.w['artifacts']['bd']['status'],'stale');self.assertEqual(self.w['artifacts']['risk']['status'],'approved')

    def test_forged_quote_rejected(self):
        f=self.w['facts'][0]
        with self.assertRaises(ValueError):self.action('fact_save',**{**f,'quote':'This quotation was invented'})

    def test_team_private_source_not_shared_fact(self):
        self.action('source_add',title='Risk notes',text='Private control evidence',scope='risk',kind='internal')
        s=self.w['sources'][-1]
        with self.assertRaises(ValueError):self.action('fact_save',label='Leak',value='Leak',source_id=s['id'],quote=s['text'])
        self.assertNotIn(s,team_input(self.w,'marketing')['sources']);self.assertIn(s,team_input(self.w,'risk')['sources'])
        self.assertEqual(team_input(self.w,'marketing')['controls'],[])

    def test_stale_revision_rejected(self):
        revision=self.w['revision'];self.approve()
        with self.assertRaises(Conflict):self.action('facts_approve',revision=revision,note='Old tab')

    def test_roles_checked(self):
        with self.assertRaises(ValueError):self.action('facts_approve',role='marketing',note='Wrong role')
        self.approve();self.generate('risk')
        with self.assertRaises(ValueError):self.action('artifact_review',role='cs',team='risk',decision='approved',note='Wrong role')

    def test_generation_requires_approval(self):
        with self.assertRaises(ValueError):self.generate()

    def test_duplicate_jobs_rejected(self):
        self.approve();p={'actor':'Tester','role':'product','revision':self.w['revision'],'kind':'generate','team':'cs','mode':'template'}
        self.store.enqueue(self.w['id'],p)
        with self.assertRaises(Conflict):self.store.enqueue(self.w['id'],p)

    def test_changed_input_supersedes_job(self):
        self.approve();self.store.enqueue(self.w['id'],{'actor':'Tester','role':'product','revision':self.w['revision'],'kind':'generate','team':'cs','mode':'template'})
        job=self.store.take_job();f=self.w['facts'][0];self.action('fact_save',**{**f,'value':'Changed scope'})
        self.store.finish_job(job,template_pack(job['request']['snapshot'],'cs'));self.w=self.store.get(self.w['id'])
        self.assertEqual(self.w['jobs'][0]['state'],'superseded');self.assertNotIn('cs',self.w['artifacts'])

    def test_review_during_generation_not_overwritten(self):
        self.approve();self.generate()
        self.store.enqueue(self.w['id'],{'actor':'Tester','role':'product','revision':self.w['revision'],'kind':'generate','team':'cs','mode':'template'})
        job=self.store.take_job();self.action('artifact_review',team='cs',decision='approved',note='Reviewed while rerun pending')
        self.store.finish_job(job,template_pack(job['request']['snapshot'],'cs'));w=self.store.get(self.w['id'])
        self.assertEqual(w['jobs'][0]['state'],'superseded');self.assertEqual(w['artifacts']['cs']['status'],'approved')

    def test_failure_preserves_deliverable(self):
        self.approve();self.generate();original=copy.deepcopy(self.w['artifacts']['cs'])
        self.store.enqueue(self.w['id'],{'actor':'Tester','role':'product','revision':self.w['revision'],'kind':'generate','team':'cs','mode':'ollama'})
        def fail(*args):raise RuntimeError('Offline')
        Worker(self.store,{},fail).process_one();w=self.store.get(self.w['id'])
        self.assertEqual(w['jobs'][0]['state'],'failed');self.assertEqual(w['artifacts']['cs'],original)

    def test_invalid_model_schema_failed(self):
        self.approve();self.store.enqueue(self.w['id'],{'actor':'Tester','role':'product','revision':self.w['revision'],'kind':'generate','team':'cs','mode':'ollama'})
        Worker(self.store,{},lambda *args:{'items':[]}).process_one()
        self.assertEqual(self.store.get(self.w['id'])['jobs'][0]['state'],'failed')

    def test_restart_marks_interruption(self):
        self.approve();self.store.enqueue(self.w['id'],{'actor':'Tester','role':'product','revision':self.w['revision'],'kind':'generate','team':'cs','mode':'template'})
        self.store.take_job();self.store.recover_jobs();self.assertEqual(self.store.get(self.w['id'])['jobs'][0]['state'],'interrupted')

    def test_absolute_claim_blocks_approval(self):
        self.approve();self.generate();a=copy.deepcopy(self.w['artifacts']['cs']);a['items'][0]['body']='Available to all banks with zero risk.'
        self.action('artifact_save',team='cs',items=a['items'],open_questions=[],note='Test unsupported claim')
        with self.assertRaises(ValueError):self.action('artifact_review',team='cs',decision='approved',note='Attempt approval')

    def test_question_item_blocks_approval(self):
        self.approve();self.generate();a=copy.deepcopy(self.w['artifacts']['cs']);a['items'][0]['kind']='open_question'
        self.action('artifact_save',team='cs',items=a['items'],open_questions=[],note='Test unresolved item')
        with self.assertRaises(ValueError):self.action('artifact_review',team='cs',decision='approved',note='Attempt approval')

    def test_unknown_fact_rejected(self):
        self.approve();self.generate();a=copy.deepcopy(self.w['artifacts']['cs']);a['items'][0]['fact_ids']=['invented']
        with self.assertRaises(ValueError):self.action('artifact_save',team='cs',items=a['items'],note='Bad reference')

    def test_edits_archive_and_reopen(self):
        self.complete();a=copy.deepcopy(self.w['artifacts']['cs']);a['items'][0]['body']='Revised summary for review.'
        self.action('artifact_save',team='cs',items=a['items'],open_questions=[],note='Edited content')
        self.assertEqual(len(self.w['archive']),1);self.assertEqual(self.w['artifacts']['cs']['version'],2)
        self.assertIsNone(self.w['artifacts']['cs']['review']);self.assertEqual(next(t for t in self.w['tasks'] if t['team']=='cs')['status'],'todo')

    def test_dependency_cycle_rollback(self):
        risk=next(t for t in self.w['tasks'] if t['team']=='risk');bd=next(t for t in self.w['tasks'] if t['team']=='bd')
        with self.assertRaises(ValueError):self.action('task_save',**{**risk,'depends_on':[bd['id']]})
        self.assertEqual(self.store.get(self.w['id'])['revision'],self.w['revision'])

    def test_dependency_completion_order(self):
        self.approve();self.generate('bd');self.action('artifact_review',team='bd',decision='approved',note='Reviewed')
        bd=next(t for t in self.w['tasks'] if t['team']=='bd')
        with self.assertRaises(ValueError):self.action('task_save',**{**bd,'status':'done','owner':'Owner','evidence':'Proof'})

    def test_done_requires_evidence(self):
        self.complete();t=self.w['tasks'][0]
        with self.assertRaises(ValueError):self.action('task_save',**{**t,'evidence':''})

    def test_reopening_dependency_reopens_downstream(self):
        self.complete();risk=next(t for t in self.w['tasks'] if t['team']=='risk');self.action('task_save',**{**risk,'status':'in_progress'})
        self.assertEqual(next(t for t in self.w['tasks'] if t['team']=='bd')['status'],'todo')

    def test_control_status_requires_evidence(self):
        c=self.w['controls'][0]
        with self.assertRaises(ValueError):self.action('control_save',**{**c,'status':'tested','evidence':''})

    def test_partner_ready_requires_evidence(self):
        p=self.w['partners'][0]
        with self.assertRaises(ValueError):self.action('partner_save',**{**p,'stage':'ready','evidence':''})

    def test_extraction_additive_and_deduplicated(self):
        self.store.enqueue(self.w['id'],{'actor':'Tester','role':'product','revision':self.w['revision'],'kind':'extract','mode':'ollama'})
        job=self.store.take_job();self.store.finish_job(job,{'facts':[self.w['facts'][0]],'open_questions':['Clarify launch date']});self.w=self.store.get(self.w['id'])
        self.assertEqual(len(self.w['facts']),6)
        with self.assertRaises(ValueError):self.approve()
        self.action('questions_resolve',note='No date commitment in this simulated scope');self.approve()

    def test_database_persists(self):
        self.approve();other=Store(self.store.path);self.assertTrue(other.get(self.w['id'])['facts_approved'])

    def test_job_result_applied_once(self):
        self.approve();job=self.generate();revision=self.w['revision']
        self.store.finish_job(job,template_pack(job['request']['snapshot'],'cs'))
        self.assertEqual(self.store.get(self.w['id'])['revision'],revision)

    def test_team_source_scoped_invalidation(self):
        self.complete();self.action('source_add',title='Marketing evidence',text='Internal brand requirement',scope='marketing',kind='internal')
        self.assertTrue(self.w['facts_approved']);self.assertEqual(self.w['artifacts']['marketing']['status'],'stale');self.assertEqual(self.w['artifacts']['risk']['status'],'approved')

    def test_shared_source_invalidates_baseline(self):
        self.complete();self.action('source_add',title='New source',text='New scope evidence',scope='shared',kind='internal')
        self.assertFalse(self.w['facts_approved']);self.assertTrue(all(a['status']=='stale' for a in self.w['artifacts'].values()))

    def test_source_span_extraction_copies_exact_quote(self):
        snapshot=team_input(self.w,'cs');seen={}
        def respond(request,**kw):
            payload=json.loads(request.data);seen.update(payload)
            key=payload['format']['properties']['facts']['items']['properties']['excerpt_id']['enum'][0]
            content={'facts':[{'label':'Pilot scope','value':'Requires participant confirmation','excerpt_id':key}],'open_questions':[]}
            return io.BytesIO(json.dumps({'message':{'content':json.dumps(content)}}).encode())
        with patch('urllib.request.urlopen',side_effect=respond):
            result=generate({'generation_model':'test','ollama_url':'http://localhost'},{'kind':'extract','team':None,'request':{'mode':'ollama','snapshot':snapshot}})
        self.assertEqual(result['facts'][0]['quote'],self.w['facts'][0]['quote']);self.assertEqual(seen['options']['num_ctx'],16384)

    def test_team_model_references_are_source_spans(self):
        snapshot=team_input(self.w,'cs')
        def respond(request,**kw):
            payload=json.loads(request.data);schema=payload['format']['properties']['items']['items']['properties']
            key=schema['source_refs']['items']['enum'][0]
            content={'items':[{'title':'Pilot','body':'Confirmed participants only','kind':'source_summary','fact_ids':[self.w['facts'][0]['id']],'source_refs':[key]}],'open_questions':[]}
            return io.BytesIO(json.dumps({'message':{'content':json.dumps(content)}}).encode())
        with patch('urllib.request.urlopen',side_effect=respond):
            result=generate({'generation_model':'test','ollama_url':'http://localhost'},{'kind':'generate','team':'cs','request':{'mode':'ollama','snapshot':snapshot}})
        self.assertEqual(result['items'][0]['source_refs'][0]['quote'],self.w['facts'][0]['quote'])

    def test_truncated_model_response_rejected(self):
        with patch('urllib.request.urlopen',return_value=io.BytesIO(b'{"done_reason":"length"}')):
            with self.assertRaisesRegex(ValueError,'token limit'):
                generate({'generation_model':'test','ollama_url':'http://localhost'},{'kind':'extract','team':None,'request':{'mode':'ollama','snapshot':team_input(self.w,'cs')}})

    def test_oversized_input_not_silently_truncated(self):
        snapshot=team_input(self.w,'cs');snapshot['brief']='x'*27000
        with patch('urllib.request.urlopen') as request:
            with self.assertRaisesRegex(ValueError,'budget'):generate({}, {'kind':'extract','team':None,'request':{'mode':'ollama','snapshot':snapshot}})
            request.assert_not_called()


class HttpTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp=tempfile.TemporaryDirectory();cls.app=Application(Path(cls.temp.name)/'db',{'generation_model':'test','ollama_url':'http://127.0.0.1:1'})
        cls.server=ThreadingHTTPServer(('127.0.0.1',0),handler_for(cls.app));cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()
        cls.base='http://127.0.0.1:'+str(cls.server.server_port)

    @classmethod
    def tearDownClass(cls): cls.server.shutdown();cls.server.server_close();cls.thread.join();cls.temp.cleanup()

    def request(self,path,data=None,headers=None):
        h={'Content-Type':'application/json'};h.update(headers or {})
        req=urllib.request.Request(self.base+path,data=json.dumps(data).encode() if data is not None else None,headers=h)
        return urllib.request.urlopen(req,timeout=5)

    def test_static_and_csp(self):
        with self.request('/') as r:self.assertIn('UPI Feature Workspace',r.read().decode());self.assertIn("frame-ancestors 'none'",r.headers['Content-Security-Policy'])

    def test_cross_origin_rejected(self):
        with self.assertRaises(urllib.error.HTTPError) as cm:self.request('/api/launches',{}, {'Origin':'https://example.com'})
        self.assertEqual(cm.exception.code,403)

    def test_host_rejected(self):
        with self.assertRaises(urllib.error.HTTPError) as cm:self.request('/api/launches',headers={'Host':'malicious.example'})
        self.assertEqual(cm.exception.code,403)

    def test_path_traversal_not_served(self):
        with self.assertRaises(urllib.error.HTTPError) as cm:self.request('/../config.json')
        self.assertEqual(cm.exception.code,404)

    def test_create_get_mutate_export(self):
        with self.request('/api/launches',{'actor':'Tester','role':'product','title':'HTTP test','brief':'Brief','simulated':True}) as r:w=json.load(r)
        with self.request('/api/launches/'+w['id']) as r:self.assertEqual(json.load(r)['title'],'HTTP test')
        with self.request('/api/launches/'+w['id']+'/actions',{'actor':'Tester','role':'product','revision':w['revision'],'action':'brief_save','title':'Changed','brief':'Updated brief'}) as r:self.assertEqual(json.load(r)['title'],'Changed')
        with self.request('/api/launches/'+w['id']+'/export') as r:self.assertIn('SIMULATED',r.read().decode())


if __name__=='__main__':unittest.main()
