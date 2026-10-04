import copy,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
from app import Engine,ROOT,read_json
from product_scope import resolve,number,fiscal_year,source_coverage
from tools.audit_product_pack import split_pages
from tools.import_products import build
from embedding_cache import build_cached,cache_key

class MultiProductTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cfg=read_json(ROOT/('config.products.json' if (ROOT/'config.products.json').exists() else 'config.example.json'));cfg.update(vector_backend='json',embedding_model='',reranker_enabled=False)
  cls.e=Engine(config=cfg)
  cls.old=Engine(data_dir=ROOT/'data',config=read_json(ROOT/'tests/fixtures/legacy_config.json'))
 def ask(self,q,**kw):return self.e.answer(dict(query=q,mode='evidence',method='bm25',**kw))
 def test_no_listing_lost(self):self.assertEqual(sum(len(d.get('source_listings',[])) for d in self.e.docs),1955)
 def test_all_existing_chunks_preserved(self):
  for p in self.old.parts:self.assertEqual(p['text'],self.e.parts_by_id[p['id']]['text'],p['id'])
 def test_existing_review_hashes_preserved(self):self.assertEqual(self.e.reviews,self.old.reviews)
 def test_missing_newer_documents_retained(self):
  for key in ['2026-OC-186A','2026-OC-227A']:self.assertTrue(self.e.parts_by_doc[key])
 def test_unique_document_and_page_ids(self):
  self.assertEqual(len(self.e.by_id),len(self.e.docs));self.assertEqual(len(self.e.page_lookup),len(self.e.pages))
 def test_one_canonical_per_pdf_url(self):
  urls=[d['source_pdf'] for d in self.e.docs if d.get('source_pdf')];self.assertEqual(len(urls),len(set(urls)))
 def test_membership_filter(self):
  d=next(d for d in self.e.docs if len(d['product_memberships'])>=5)
  for product in d['product_memberships']:self.assertTrue(self.e.eligible(d,product))
  self.assertFalse(self.e.eligible(d,'imaginary'))
 def test_ambiguous_number_abstains(self):
  r=self.ask('What does OC 13 require?');self.assertFalse(r['sources']);self.assertTrue(r['retrieval_trace']['ambiguities'])
 def test_product_still_ambiguous_across_years(self):self.assertFalse(self.ask('Summarise NACH OC 13')['sources'])
 def test_fiscal_year_resolves(self):
  r=self.ask('Summarise AePS OC 33 FY 2018-19');self.assertTrue(r['sources']);self.assertTrue(all('AePS' in p['product_memberships'] for p in r['sources']))
 def test_unavailable_side_does_not_compare(self):self.assertFalse(self.ask('Compare UPI OC 186 and OC 999')['sources'])
 def test_unknown_issue_dates_excluded(self):
  d=next(d for d in self.e.docs if d['metadata_quality']=='inventory_unverified' and d['availability']=='converted');self.assertFalse(self.e.eligible(d,cutoff='2026-12-31'))
 def test_fiscal_year_not_issue_date(self):
  docs=[d for d in self.e.docs if d['metadata_quality']=='inventory_unverified'];self.assertTrue(all(d['issue_date'] is None for d in docs))
 def test_blank_page_preserved_not_embedded(self):
  r=self.ask('Summarise AePS OC 33 FY 2018-19');key=r['sources'][0]['document_id'];self.assertEqual(self.e.page_lookup[key,1]['text'],'');self.assertFalse(any(p['page']==1 for p in self.e.parts_by_doc[key]))
 def test_incomplete_source_not_claimed_complete(self):
  r=self.ask('Summarise AePS OC 33 FY 2018-19');cov=next(iter(r['retrieval_trace']['document_coverage'].values()));self.assertFalse(cov['complete']);self.assertEqual(cov['empty_pages'],[1])
 def test_unverified_page_count_not_complete(self):
  d=next(d for d in self.e.docs if d['availability']=='converted' and not d['source_coverage']['page_count_verified']);r=self.ask('Summarise selected circular',document_ids=[d['id']]);self.assertFalse(r['retrieval_trace']['document_coverage'][d['id']]['complete'])
 def test_quarantine_excluded(self):
  for d in self.e.docs:
   if d['availability']=='needs_source_review':self.assertFalse(self.e.parts_by_doc[d['id']]);self.assertFalse(self.ask('Summarise selected circular',document_ids=[d['id']])['sources'])
 def test_existing_failed_link_not_silently_recovered(self):self.assertFalse(self.e.parts_by_doc['2024-OC-76B'])
 def test_explicit_selection_disambiguates(self):
  d=next(d for d in self.e.docs if d['series']=='NACH' and d['circular_number']=='13' and d['availability']=='converted');r=self.ask('Summarise selected circular',document_ids=[d['id']]);self.assertEqual({s['document_id'] for s in r['sources']},{d['id']})
 def test_selected_circular_respects_filter(self):self.assertFalse(self.ask('Summarise selected circular',document_ids=['2026-OC-186A'],series='AePS')['sources'])
 def test_bad_selection_and_year_rejected(self):
  for kw in [dict(document_ids='bad'),dict(document_ids=['x','x']),dict(fiscal_year='2020')]:
   with self.assertRaises(ValueError):self.ask('Summarise selected circular',**kw)
 def test_same_number_in_two_selected_documents(self):
  docs=[d for d in self.e.docs if d['series']=='NACH' and d['circular_number']=='13' and d['availability']=='converted'][:2];self.assertEqual(len(docs),2)
  r=self.ask('Compare selected circulars',document_ids=[d['id'] for d in docs]);self.assertEqual({p['document_id'] for p in r['sources']},{d['id'] for d in docs})
 def test_neighbor_ownership(self):
  for p in self.e.parts:
   for attr in ['previous_chunk_id','next_chunk_id']:
    if p.get(attr):self.assertEqual(p['document_id'],self.e.parts_by_id[p[attr]]['document_id'])
 def test_source_word_spans(self):
  for p in self.e.parts:self.assertEqual(p['text'],' '.join(self.e.page_lookup[p['document_id'],p['page']]['text'].split()[p['start_word']:p['end_word']]))
 def test_imported_unicode_line_separator(self):
  self.assertTrue(any('\u2028' in p['text'] or '\u0085' in p['text'] for p in self.e.pages))
 def test_markdown_preamble_and_empty_page(self):self.assertEqual(split_pages('# Title\nmetadata\n<!-- Page 1 -->\n<!-- Page 2 -->\nText'),[(1,''),(2,'Text')])
 def test_existing_destination_not_overwritten(self):
  with self.assertRaises(ValueError):build(ROOT/'does-not-exist',ROOT/'data/all-products-v1')
 def test_unknown_fiscal_year_not_a_filter(self):
  from product_scope import fiscal_year
  self.assertEqual(fiscal_year({'fiscal_year':'unknown'}),'')
  self.assertNotIn('unknown',self.e.stats()['fiscal_years'])
 def test_number_normalization(self):self.assertEqual(number('013A'),'13A');self.assertNotEqual(number('13A'),number('13'))

class ActivationTests(unittest.TestCase):
 def test_failed_or_stale_report_blocks_activation(self):
  from tools.activate_corpus import verify_report
  e=type('Fake',(),{'fingerprint':'current','registry':type('Registry',(),{'fingerprint':'registry'})()})()
  for report in [{},{'passed':False},{'passed':True,'fingerprint':'old'},{'passed':True,'fingerprint':'current','registry_fingerprint':'old'}]:
   with self.assertRaises(ValueError):verify_report(report,e)
 def test_incomplete_index_blocks_activation(self):
  from tools.activate_corpus import verify_report
  e=type('Fake',(),{'fingerprint':'current','registry':type('Registry',(),{'fingerprint':'registry'})(),'vector_ready':False,'vector_status':'Not built'})()
  with self.assertRaises(ValueError):verify_report({'passed':True,'fingerprint':'current','registry_fingerprint':'registry'},e)
 def test_changed_model_blocks_activation(self):
  from tools.activate_corpus import verify_report
  collection=type('Collection',(),{'metadata':{'model_digest':'old'},'count':lambda self:1})()
  e=type('Fake',(),{'fingerprint':'current','registry':type('Registry',(),{'fingerprint':'registry'})(),'vector_ready':True,'parts':[1],'store':type('Store',(),{'collection':collection})(),'model_digest':lambda self:'new'})()
  with self.assertRaises(ValueError):verify_report({'passed':True,'fingerprint':'current','registry_fingerprint':'registry'},e)

class EmbeddingCacheTests(unittest.TestCase):
 def test_keys_include_model_digest_and_exact_text(self):
  self.assertNotEqual(cache_key('m','a','t'),cache_key('m','b','t'));self.assertNotEqual(cache_key('m','a','t'),cache_key('m','a',' t'))
 def test_resumable_cache_and_model_invalidation(self):
  with tempfile.TemporaryDirectory() as temp:
   e=type('Fake',(),{})();e.config={'embedding_model':'m','embedding_cache':str(Path(temp)/'cache.sqlite3')};e.data_dir=Path(temp);e.parts=[{'id':'a','title':'A','text':'Text'}];e.fingerprint='fp';e.model_digest=lambda:'d1';e.unit=Engine.unit
   e.store=type('Store',(),{'status':'Ready','build':lambda self,v,d:None})();e.registry=type('Registry',(),{'persist':lambda self,p:None})();calls=[]
   e.ollama=lambda *args:(calls.append(args) or {'embeddings':[[1.,0.]]})
   build_cached(e);build_cached(e);self.assertEqual(len(calls),1)
   e.model_digest=lambda:'d2';build_cached(e);self.assertEqual(len(calls),2)
if __name__=='__main__':unittest.main()
