import copy,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
from app import Engine,ROOT,read_json
from adaptive_context import route_question,mentions
from quality import apply_reviews,digest,ReviewStore
from claim_check import check_claims
from reranker import get_reranker

class AdaptiveTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  config=read_json(ROOT/('config.json' if (ROOT/'config.json').exists() else 'config.example.json'));config.update(vector_backend='json',embedding_model='',reranker_enabled=False)
  cls.e=Engine(data_dir=ROOT/"data",config={**config,"multi_product":False})
 def ask(self,q,**kw):return self.e.answer(dict(query=q,mode='evidence',method='bm25',**kw))
 def test_routes(self):
  self.assertEqual(route_question('Compare OC 186 and 186A'),'compare');self.assertEqual(route_question('Summarise OC 186A'),'summary');self.assertEqual(route_question('OC 186A consent'),'clause')
 def test_mentions_shorthand(self):self.assertEqual(mentions('Compare OC 186 and 186A'),['186','186A'])
 def test_summary_complete(self):
  r=self.ask('Summarise OC 186A');self.assertTrue(r['retrieval_trace']['document_coverage']['2026-OC-186A']['complete']);self.assertEqual(len(r['sources']),14)
 def test_comparison_both(self):
  r=self.ask('Compare OC 186 and 186A');self.assertEqual({s['document_id'] for s in r['sources']},{'2023-UPI-186','2026-OC-186A'})
 def test_missing_side(self):self.assertFalse(self.ask('Compare OC 186 and OC 999')['sources'])
 def test_filtered_side(self):self.assertFalse(self.ask('Compare OC 186 and OC 186A',cutoff='2024-01-01')['sources'])
 def test_summary_requires_number(self):self.assertFalse(self.ask('Summarise tap pay')['sources'])
 def test_small_budget_reports_partial(self):
  with patch.dict(self.e.config,context_char_budget=2000):
   r=self.ask('Summarise OC 186A');self.assertFalse(r['retrieval_trace']['document_coverage']['2026-OC-186A']['complete']);self.assertTrue(r['retrieval_trace']['notes'])
 def test_strict_does_not_expand(self):self.assertTrue(all(s['document_id']=='2026-OC-186A' for s in self.ask('OC 186A consent',scope='strict')['sources']))
 def test_corrected_and_original(self):
  p=self.e.page_lookup['2026-OC-186A',1];self.assertIn('₹5000',p['text']);self.assertIn('$5000',p['original_text'])
 def test_stale_review_rejected(self):
  p={'document_id':'d','source_page':1,'text':'raw'};r=dict(id='x',kind='correction',status='accepted',document_id='d',page=1,source_hash='bad')
  with self.assertRaises(ValueError):apply_reviews([{'id':'d'}],[p],[r])
 def test_duplicate_acceptance_does_not_poison_store(self):
  p=self.e.page_lookup['2026-OC-186A',1]
  payload=dict(kind='correction',status='accepted',reviewer='test',document_id='2026-OC-186A',page=1,source_hash=digest(p['original_text']),before='₹5000',after='Rs 5000')
  with tempfile.TemporaryDirectory() as directory:
   store=ReviewStore(directory);store.path.write_text(json.dumps(self.e.reviews),encoding='utf-8');store.save(payload,self.e);before=store.path.read_bytes()
   with self.assertRaises(ValueError):store.save(payload,self.e)
   self.assertEqual(before,store.path.read_bytes())
 def test_role_review_provenance(self):
  reviewed=[p for p in self.e.parts if p.get('review_id')];self.assertTrue(reviewed);self.assertTrue(all(p['role_basis']=='assistant_source_checked' for p in reviewed))
 def test_real_cpu_reranker(self):
  ranker=get_reranker(ROOT/'models/reranker');rows=ranker.rank('Who checks tap payment enablement before processing each transaction?',[
   dict(id='a',title='Tap Pay',text='Payee PSP integrates the transaction API.'),dict(id='b',title='Tap Pay',text='Remitter Bank checks enablement before processing each transaction.')]);self.assertEqual(rows[0]['id'],'b')

class ClaimTests(unittest.TestCase):
 def setUp(self):
  self.e=type('Fake',(),{'config':{'generation_model':'test'}})();self.sources=[dict(citation='S1',text='The limit is 5000. Consent is required.',method='ocr')]
 def check(self,text,reply):
  self.e.ollama=lambda *args:dict(response=json.dumps(reply));return check_claims(self.e,[dict(text=text,sources=['S1'])],self.sources)
 def test_circular_attribution_metadata(self):
  self.sources[0]['circular_number']='186A';self.assertTrue(self.check('Under OC 186A, consent is required.',dict(status='supported',reason='Direct',quotes=[dict(citation='S1',quote='Consent is required.')]))[0])
 def test_typographic_apostrophe(self):
  self.sources[0]['text']='Check the User\u2019s account.';self.assertTrue(self.check('Check the account.',dict(status='supported',reason='Direct',quotes=[dict(citation='S1',quote="Check the User's account.")]))[0])
 def test_ocr_word_change_not_accepted(self):
  self.sources[0]['text']='UP! Tap consent';self.assertFalse(self.check('Consent needed.',dict(status='supported',reason='Direct',quotes=[dict(citation='S1',quote='UPI Tap consent')]))[0])
 def test_number_absent(self):self.assertEqual(self.check('The limit is 9000.',{})[2][0]['status'],'unsupported')
 def test_exact_quote(self):self.assertEqual(len(self.check('Consent is required.',dict(status='supported',reason='Direct',quotes=[dict(citation='S1',quote='Consent is required.')]))[0]),1)
 def test_fabricated_quote(self):self.assertFalse(self.check('Consent is optional.',dict(status='supported',reason='bad',quotes=[dict(citation='S1',quote='Consent is optional.')]))[0])
 def test_foreign_citation(self):self.assertFalse(self.check('Consent is required.',dict(status='supported',reason='bad',quotes=[dict(citation='S9',quote='Consent is required.')]))[0])
 def test_malformed_judge(self):self.assertEqual(self.check('Consent is required.',{})[2][0]['status'],'uncertain')
 def test_unsupported_judge(self):self.assertFalse(self.check('Consent is optional.',dict(status='unsupported',reason='Contradicted',quotes=[]))[0])
 def test_currency_guard(self):self.assertEqual(self.check('The limit is $5000.',{})[2][0]['status'],'uncertain')
if __name__=='__main__':unittest.main()
