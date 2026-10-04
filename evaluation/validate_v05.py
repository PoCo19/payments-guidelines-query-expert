"""Expanded-corpus validation; developer checks, not independent answer accuracy."""
import hashlib,json,sqlite3,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from app import Engine,read_json
from product_scope import memberships

e=Engine(config=read_json(ROOT/'config.products.json'));assert e.vector_ready,e.vector_status
result={'fingerprint':e.fingerprint,'registry_fingerprint':e.registry.fingerprint,'dataset':str(e.data_dir),'note':'Developer structural/filter/regression checks; not independently reviewed answer accuracy. UPI cases use an explicit UPI product filter in the expanded corpus.','counts':{k:v for k,v in e.stats().items() if k in ('documents','converted','pages','chunks','series')},'checks':{},'upi':{},'products':[]}
manifest=read_json(e.data_dir/'source_manifest.json')
for relative,digest in manifest['hashes'].items():assert hashlib.sha256((e.data_dir/'sources'/relative).read_bytes()).hexdigest()==digest,relative
result['checks']['source_files_hash_verified']=len(manifest['hashes'])
with sqlite3.connect(e.registry.path) as db:
 assert db.execute('PRAGMA integrity_check').fetchone()[0]=='ok';assert not db.execute('PRAGMA foreign_key_check').fetchall()
 assert db.execute('SELECT COUNT(*) FROM chunks').fetchone()[0]==len(e.parts)
result['checks']['sqlite_integrity']='passed';result['checks']['vector_count']=e.store.collection.count()
raw=(ROOT/'evaluation/rag_cases.json').read_bytes();assert hashlib.sha256(raw).hexdigest()==(ROOT/'evaluation/rag_cases.sha256').read_text().strip()
cases=json.loads(raw)
for method in ['bm25','hybrid']:
 rows=[]
 for case in cases:
  series=case.get('series') or 'UPI'
  r=e.answer(dict(query=case['query'],method=method,mode='evidence',scope=case['scope'],series=series,cutoff=case.get('cutoff',''),rerank=True))
  hits=[any(s['document_id']==a['document_id'] and s['page']==a['page'] and a['quote'] in ' '.join(s['text'].split()) for s in r['sources']) for a in case['references']]
  rows.append(dict(id=case['id'],anchor_hits=hits,empty=not r['sources'],elapsed_ms=r['elapsed_ms'],source_ids=[s['id'] for s in r['sources']]))
 result['upi'][method]=dict(anchors_found=sum(sum(r['anchor_hits']) for r in rows),anchors_expected=sum(len(r['anchor_hits']) for r in rows),rows=rows)
 print(method,'UPI anchors',result['upi'][method]['anchors_found'],'/',result['upi'][method]['anchors_expected'],flush=True)
products=sorted({m for d in e.docs for m in memberships(d)}-{'Product Compliance'})
for product in products:
 docs=[d for d in e.docs if product in memberships(d) and d['availability']=='converted' and e.parts_by_doc[d['id']]]
 d=min(docs,key=lambda d:(len(e.parts_by_doc[d['id']]),d['id']))
 query=d['subject']
 # This is a product-isolation/search smoke check, intentionally title-derived.
 r=e.answer(dict(query=query,route='clause',method='hybrid',mode='evidence',series=product,document_ids=[d['id']],scope='strict'))
 assert r['sources'] and all(s['document_id']==d['id'] and product in s['product_memberships'] for s in r['sources']),product
 broad=e.search('payment transaction settlement',method='hybrid',series=product,k=8)
 assert broad and all(product in s['product_memberships'] for s in broad),product
 result['products'].append(dict(product=product,document_id=d['id'],query=query,sources=len(r['sources']),unrestricted_query_sources=len(broad),elapsed_ms=r['elapsed_ms']))
 print(product,'filter/selection passed',flush=True)
partial=e.answer(dict(query='Summarise AePS OC 33 FY 2018-19',method='hybrid',mode='evidence'))
assert partial['sources'] and not next(iter(partial['retrieval_trace']['document_coverage'].values()))['complete']
ambiguous=e.answer(dict(query='What does OC 13 require?',mode='generate',method='hybrid'))
assert ambiguous['abstained'] and not ambiguous['sources']
result['checks']['partial_source_warning']='passed';result['checks']['ambiguity_abstention']='passed'
result['passed']=all(v['anchors_found']==v['anchors_expected'] for v in result['upi'].values())
(ROOT/'reports/v05_validation.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
print('Validation result:',result['passed'],flush=True)
if not result['passed']:raise SystemExit(1)
