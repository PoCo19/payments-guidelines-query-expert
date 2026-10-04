"""Frozen, AI-assisted retrieval evaluation. No independent accuracy claim."""
import csv,hashlib,json,statistics,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from app import Engine

def summarize(rows):
 hits=[h for r in rows for h in r['anchor_hits']]
 negative=[r for r in rows if not r['anchor_hits']]
 return dict(anchor_recall=sum(hits)/len(hits) if hits else None,anchor_count=len(hits),negative_empty=sum(r['empty'] for r in negative),negative_cases=len(negative),median_ms=round(statistics.median(r['elapsed_ms'] for r in rows),1),p95_ms=sorted(r['elapsed_ms'] for r in rows)[int(.95*(len(rows)-1))])

def main():
 raw=(ROOT/'evaluation/rag_cases.json').read_bytes();checksum=hashlib.sha256(raw).hexdigest()
 if checksum!=(ROOT/'evaluation/rag_cases.sha256').read_text().strip():raise ValueError('Frozen dataset changed. Create a new version instead.')
 cases=json.loads(raw);e=Engine();runs={}
 baseline=json.loads((ROOT/'evaluation/v03_50case_baseline.json').read_text());runs['v03_bm25']=dict(summary=summarize(baseline['rows']),rows=baseline['rows'])
 for name,method,rerank in [('v04_bm25','bm25',False),('v04_bm25_reranked','bm25',True),('v04_hybrid_reranked','hybrid',True)]:
  rows=[]
  for c in cases:
   result=e.answer(dict(query=c['query'],method=method,mode='evidence',scope=c['scope'],series=c['series'],cutoff=c.get('cutoff',''),rerank=rerank))
   hits=[any(s['document_id']==a['document_id'] and s['page']==a['page'] and a['quote'] in ' '.join(s['text'].split()) for s in result['sources']) for a in c['references']]
   rows.append(dict(id=c['id'],split=c['split'],route=result['retrieval_trace']['route'],anchor_hits=hits,source_ids=[s['id'] for s in result['sources']],elapsed_ms=result['elapsed_ms'],empty=not result['sources'],trace=result['retrieval_trace']))
  runs[name]=dict(summary=summarize(rows),by_route={route:summarize([r for r in rows if r['route']==route]) for route in {r['route'] for r in rows}},rows=rows)
  print(name,runs[name]['summary'],flush=True)
 result=dict(dataset_hash=checksum,note='Provisional AI-assisted set, all 50 cases await independent source review. 32 development and 18 reserved-review cases; neither is independently authored held-out gold. Exact anchor recall is retrieval coverage, not answer accuracy. Negative empty evidence is not generated abstention. Pipeline and budget changed, so baseline difference is not solely reranking.',fingerprint=e.fingerprint,runs=runs)
 (ROOT/'evaluation/v04_retrieval_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
 worksheet=ROOT/'evaluation/independent_review.csv'
 if not worksheet.exists():
  with worksheet.open('w',newline='',encoding='utf-8-sig') as f:
   fields=['id','query','expected_answer','references','reviewer','source_verified','answer_correct','citation_support','missing_requirements','notes'];w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
   for c in cases:w.writerow({k:c[k] for k in fields[:3]}|{'references':json.dumps(c['references'])})
 print('Saved evaluation/v04_retrieval_results.json. No independent gold score published.')
if __name__=='__main__':main()
