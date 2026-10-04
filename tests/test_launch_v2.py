import base64
import copy
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch
from launch_orchestrator.core import Store,Conflict,team_input,validate_pack
from launch_orchestrator.demo import create_feature_demo
from launch_orchestrator.documents import extract_document
from launch_orchestrator.generation import Worker,generate,template_pack


class WorkspaceV2Tests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.store=Store(Path(self.tmp.name)/'db');self.w=create_feature_demo(self.store,'Tester')
    def tearDown(self):self.tmp.cleanup()
    def action(self,action,**kw):
        self.w=self.store.mutate(self.w['id'],{'actor':'Tester','role':'product','revision':self.w['revision'],'action':action,**kw});return self.w
    def approve(self):self.action('facts_approve',note='Synthetic facts reviewed')
    def batch(self):
        self.approve();self.store.enqueue_all(self.w['id'],{'actor':'Tester','role':'product','revision':self.w['revision'],'mode':'template'})
        worker=Worker(self.store,{})
        for _ in range(4):self.assertTrue(worker.process_one())
        self.w=self.store.get(self.w['id'])
    def test_existing_feature_and_next_step(self):
        self.assertEqual(self.w['workspace_type'],'existing');self.assertEqual(self.w['next_step']['view'],'brief')
        self.assertTrue(all('pilot' not in t['title'].lower() for t in self.w['tasks']))
    def test_empty_workspace_next_step_is_sources(self):
        w=self.store.create({'actor':'Tester','role':'product','title':'Feature','brief':'Review existing flow','workspace_type':'existing'})
        self.assertEqual(w['next_step']['view'],'sources')
    def test_invalid_workspace_type(self):
        with self.assertRaises(ValueError):self.store.create({'actor':'Tester','role':'product','title':'Feature','brief':'Brief','workspace_type':'made_up'})
    def test_all_drafts_queued_atomically(self):
        self.batch();self.assertEqual(len(self.w['artifacts']),4);self.assertTrue(all(j['state']=='completed' for j in self.w['jobs']))
        self.assertEqual(len(self.w['artifacts']['risk']['rule_assessments']),1)
    def test_batch_duplicate_and_role_protection(self):
        self.approve();p={'actor':'Tester','role':'product','revision':self.w['revision'],'mode':'template'}
        self.store.enqueue_all(self.w['id'],p)
        with self.assertRaises(Conflict):self.store.enqueue_all(self.w['id'],p)
        with self.assertRaises(ValueError):self.store.enqueue_all(self.w['id'],dict(p,role='cs'))
        self.assertEqual(len(self.store.get(self.w['id'])['jobs']),4)
    def test_delete_requires_name_and_current_revision(self):
        p={'actor':'Tester','role':'product','revision':self.w['revision'],'confirmation':'wrong'}
        with self.assertRaises(ValueError):self.store.delete(self.w['id'],p)
        p.update(confirmation=self.w['title'],revision=0)
        with self.assertRaises(Conflict):self.store.delete(self.w['id'],p)
    def test_delete_during_running_job_does_not_resurrect(self):
        self.approve();self.store.enqueue_all(self.w['id'],{'actor':'Tester','role':'product','revision':self.w['revision'],'mode':'template'})
        job=self.store.take_job();self.store.delete(self.w['id'],{'actor':'Tester','role':'product','revision':self.w['revision'],'confirmation':self.w['title']})
        self.store.finish_job(job,template_pack(job['request']['snapshot'],job['team']))
        self.assertEqual(self.store.list(),[])
        with self.store.connect() as db:
            for table in ('events','jobs','launches'):self.assertEqual(db.execute('SELECT count(*) FROM '+table).fetchone()[0],0)
    def test_rule_active_requires_internal_source(self):
        self.action('source_add',title='Public source',text='A documented rule',scope='risk',kind='public')
        r=copy.deepcopy(self.w['risk_rules'][0]);r.update(status='active',source_id=self.w['sources'][-1]['id'],quote='A documented rule',verification='Claimed deployment')
        with self.assertRaisesRegex(ValueError,'internal'):self.action('risk_rule_save',**r)
    def test_active_rule_requires_deployment_note(self):
        r=copy.deepcopy(self.w['risk_rules'][0]);r.update(status='active',verification='')
        with self.assertRaisesRegex(ValueError,'deployment'):self.action('risk_rule_save',**r)
    def test_documented_rule_requires_quote(self):
        r=copy.deepcopy(self.w['risk_rules'][0]);r['quote']='Invented quote'
        with self.assertRaises(ValueError):self.action('risk_rule_save',**r)
    def test_rule_changes_only_stale_risk_content(self):
        self.batch();r=copy.deepcopy(self.w['risk_rules'][0]);r['condition']='Changed review condition'
        self.action('risk_rule_save',**r)
        self.assertEqual(self.w['artifacts']['risk']['status'],'stale');self.assertEqual(self.w['artifacts']['marketing']['status'],'draft')
    def test_rule_context_isolated(self):
        self.assertEqual(team_input(self.w,'marketing')['risk_rules'],[])
        self.assertEqual(len(team_input(self.w,'risk')['risk_rules']),1)
    def test_unknown_or_missing_rule_assessment_rejected(self):
        p=template_pack(team_input(self.w,'risk'),'risk');p['rule_assessments'][0]['rule_id']='invented'
        with self.assertRaises(ValueError):validate_pack(self.w,'risk',p)
        p['rule_assessments']=[]
        with self.assertRaises(ValueError):validate_pack(self.w,'risk',p)
    def test_rule_removal_export_remains_available(self):
        self.batch();self.action('risk_rule_remove',id=self.w['risk_rules'][0]['id'])
        self.assertIn('Removed rule',self.store.export(self.w['id']))
    def test_source_removal_downgrades_linked_rule(self):
        r=self.w['risk_rules'][0];self.action('source_remove',id=r['source_id'])
        self.assertEqual(self.w['risk_rules'][0]['status'],'proposed');self.assertEqual(self.w['risk_rules'][0]['source_id'],'')
    def test_source_removal_removes_derived_facts(self):
        self.action('source_remove',id=self.w['facts'][0]['source_id']);self.assertEqual(self.w['facts'],[]);self.assertFalse(self.w['facts_approved'])
    def test_legacy_workspace_loads_without_reinterpreting_controls(self):
        legacy=copy.deepcopy(self.w);legacy.pop('risk_rules');legacy.pop('workspace_type')
        with self.store.connect() as db:db.execute('UPDATE launches SET body=? WHERE id=?',(json.dumps(legacy),self.w['id']))
        loaded=self.store.get(self.w['id']);self.assertEqual(loaded['risk_rules'],[]);self.assertEqual(loaded['workspace_type'],'new_launch')
    def test_risk_schema_has_exact_rule_keys(self):
        snapshot=team_input(self.w,'risk');rid=self.w['risk_rules'][0]['id']
        def response(request,**kwargs):
            payload=json.loads(request.data);schema=payload['format']['properties']['rule_assessments'];self.assertEqual(schema['required'],[rid])
            pack=template_pack(snapshot,'risk');assess=pack.pop('rule_assessments')[0];assess.pop('rule_id');pack['rule_assessments']={rid:assess}
            return io.BytesIO(json.dumps({'message':{'content':json.dumps(pack)}}).encode())
        with patch('urllib.request.urlopen',side_effect=response):
            pack=generate({'generation_model':'test','ollama_url':'http://localhost'},{'kind':'generate','team':'risk','request':{'mode':'ollama','snapshot':snapshot}})
        self.assertEqual(pack['rule_assessments'][0]['rule_id'],rid)


class DocumentUploadTests(unittest.TestCase):
    def upload(self,name,data):return extract_document({'name':name,'data':base64.b64encode(data).decode()})
    def test_text_and_bom(self):self.assertEqual(self.upload('brief.md',b'\xef\xbb\xbfFeature text')['text'],'Feature text')
    def test_long_text_preview_is_explicit(self):
        r=self.upload('brief.txt',b'x'*25000);self.assertTrue(r['truncated']);self.assertEqual(len(r['text']),24000)
    def test_invalid_extension_and_base64(self):
        with self.assertRaises(ValueError):self.upload('file.exe',b'text')
        with self.assertRaises(ValueError):extract_document({'name':'a.pdf','data':'broken?'})
    def test_empty_and_oversized_files(self):
        with self.assertRaises(ValueError):self.upload('a.txt',b'')
        with self.assertRaises(ValueError):self.upload('a.txt',b'a'*(5*1024*1024+1))
    def test_docx_paragraphs(self):
        b=io.BytesIO()
        with zipfile.ZipFile(b,'w') as z:z.writestr('word/document.xml','<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>Feature source text</w:t></w:r></w:p></w:body></w:document>')
        self.assertEqual(self.upload('a.docx',b.getvalue())['text'],'Feature source text')
    def test_scanned_pdf_and_malformed_pdf_rejected(self):
        from pypdf import PdfWriter
        writer=PdfWriter();writer.add_blank_page(width=100,height=100);b=io.BytesIO();writer.write(b)
        with self.assertRaisesRegex(ValueError,'readable text'):self.upload('scan.pdf',b.getvalue())
        with self.assertRaises(ValueError):self.upload('bad.pdf',b'not a pdf')
    def test_pdf_text_extraction(self):
        from pypdf import PdfWriter
        from pypdf.generic import DictionaryObject,NameObject,DecodedStreamObject
        writer=PdfWriter();page=writer.add_blank_page(width=400,height=400)
        font=DictionaryObject({NameObject('/Type'):NameObject('/Font'),NameObject('/Subtype'):NameObject('/Type1'),NameObject('/BaseFont'):NameObject('/Helvetica')})
        page[NameObject('/Resources')]=DictionaryObject({NameObject('/Font'):DictionaryObject({NameObject('/F1'):writer._add_object(font)})})
        stream=DecodedStreamObject();stream.set_data(b'BT /F1 12 Tf 20 200 Td (Transaction rule evidence) Tj ET');page[NameObject('/Contents')]=writer._add_object(stream)
        b=io.BytesIO();writer.write(b);result=self.upload('rules.pdf',b.getvalue());self.assertIn('Transaction rule evidence',result['text']);self.assertEqual(result['pages'],1)


if __name__=='__main__':unittest.main()
