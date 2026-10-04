"""Real Chroma migration parity, corpus audit and local-model integration checks."""
import json
import sys
import time
import statistics
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app import Engine, ROOT, read_json

out=ROOT/'evaluation'/'v03_results.json'
report={"note":"Developer checks, not held-out answer accuracy.","migration":[],"retrieval":[],"answers":[]}
def save():out.write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')

legacy=read_json(ROOT/'evaluation'/'migration_config.json')
old=Engine(config=dict(legacy,vector_backend='json'))
migrated=Engine(config=legacy)
cases=read_json(ROOT/'evaluation'/'cases.json')
cache={}
actual=old.ollama
def cached(endpoint,payload):
    key=json.dumps([endpoint,payload],sort_keys=True)
    if key not in cache:cache[key]=actual(endpoint,payload)
    return cache[key]
old.ollama=migrated.ollama=cached
for method in ('vector','hybrid'):
    for case in cases:
        args=(case['query'],method,case.get('series',''),case.get('cutoff',''))
        left=old.search(*args);right=migrated.search(*args)
        a=[p['id'] for p in left];b=[p['id'] for p in right]
        report['migration'].append(dict(query=case['query'],method=method,identical=a==b,
             old_ids=a,chroma_ids=b,overlap=len(set(a)&set(b))/len(a) if a else float(not b)))
print('Migration identical:',sum(r['identical'] for r in report['migration']),'/',len(report['migration']),flush=True)
save()

e=Engine()
report['stats']=e.stats()
report['model_digest']=e.model_digest()
report['chunk_words']={"min":min(len(p['text'].split()) for p in e.parts),
    "max":max(len(p['text'].split()) for p in e.parts),"median":statistics.median(len(p['text'].split()) for p in e.parts)}
report['reference_statuses']={status:sum(x['status']==status for x in e.registry.edges) for status in sorted({x['status'] for x in e.registry.edges})}
for method in ('bm25','vector','hybrid'):
    result=e.evaluate(method)
    report['retrieval'].append(result);save()
    print(method,result['hit_rate'],result['mrr'],result['mean_document_recall'],flush=True)

questions=[
 dict(query='According to OC 186A, what consent must the user give for UPI Tap & Pay on PoS?',scope='related'),
 dict(query='Compare OC 186 and OC 186A: how is the Tap & Pay initiation method extended?',scope='related'),
 dict(query='According to OC 201, who is the primary user and who is the secondary user?',scope='strict'),
 dict(query='What requirements are specified in OC 999?',scope='related'),
 dict(query='Explain quantum photosynthesis and chlorophyll.',scope='related'),
 dict(query='According to OC 186, how is Tap Pay initiated?',scope='related',cutoff='2024-01-01'),
]
for payload in questions:
    print('Answer:',payload['query'],flush=True)
    try:
        result=e.answer(dict(payload,method='hybrid',mode='generate'))
        report['answers'].append(dict(request=payload,**result))
        print(json.dumps({k:v for k,v in result.items() if k not in ('sources','warnings','retrieval_trace')},ensure_ascii=False),flush=True)
    except Exception as exc:
        report['answers'].append(dict(request=payload,error=str(exc)))
        print('ERROR',str(exc),flush=True)
    save()
if any('error' in r for r in report['answers']):sys.exit(1)
