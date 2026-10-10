"""Compare old/new context selection on the unchanged provisional 50 cases."""
import datetime as dt
import hashlib
import json
from pathlib import Path
import statistics
import sys
import time
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app import Engine, read_json, default_config_path


def main():
    dataset=ROOT/'evaluation/rag_cases.json'
    if hashlib.sha256(dataset.read_bytes()).hexdigest() != (ROOT/'evaluation/rag_cases.sha256').read_text().strip():
        raise ValueError('Frozen dataset checksum changed.')
    cases=read_json(dataset)
    folder=ROOT/'reports/research-comparison'/dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    folder.mkdir(parents=True)
    report=dict(dataset_sha256=hashlib.sha256(dataset.read_bytes()).hexdigest(),
                note='AI-assisted provisional source anchors. Retrieval coverage only, not answer accuracy or independent evaluation.',variants={})
    engines={}
    for enabled in (False,True):
        config=read_json(default_config_path());config['research_enabled']=enabled
        engine=Engine(config=config)
        name='research' if enabled else 'previous';engines[name]=engine
        report['variants'][name]=dict(config=config,fingerprint=engine.fingerprint,registry_fingerprint=engine.registry.fingerprint,rows=[])
        engine.answer(dict(query=cases[0]['query'],series='UPI',method='hybrid',scope='strict',rerank=True,mode='evidence'))
    report['embedding_digest']=engines['research'].model_digest()
    report['code_hashes']={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ('research.py','adaptive_context.py','product_scope.py','app.py')}
    for i,case in enumerate(cases):
        names=['previous','research'] if i%2==0 else ['research','previous']
        for name in names:
            engine=engines[name]
            start=time.perf_counter()
            row=dict(id=case['id'],anchor_count=len(case['references']),anchor_hits=[])
            try:
                r=engine.answer(dict(query=case['query'],series=case.get('series') or 'UPI',cutoff=case.get('cutoff',''),method='hybrid',scope=case['scope'],rerank=True,mode='evidence'))
                sources=r['sources']
                row.update(anchor_hits=[any(s['document_id']==a['document_id'] and s['page']==a['page'] and ' '.join(a['quote'].split()) in ' '.join(s['text'].split()) for s in sources) for a in case['references']],empty=not sources,
                           sources=[dict(id=s['id'],document_id=s['document_id'],page=s['page'],text=s['text']) for s in sources],route=r['retrieval_trace']['route'])
            except Exception as exc:
                row['error']=str(exc)
            row['elapsed_ms']=round((time.perf_counter()-start)*1000,2);report['variants'][name]['rows'].append(row)
        if (i+1)%10==0:print(str(i+1)+'/50 compared',flush=True)
    for name,variant in report['variants'].items():
        rows=variant['rows']
        summary=dict(anchors_found=sum(sum(r['anchor_hits']) for r in rows),anchors=sum(r['anchor_count'] for r in rows),negative_empty=sum(not r['anchor_count'] and r.get('empty',False) for r in rows),negative_cases=sum(not r['anchor_count'] for r in rows),failures=sum('error' in r for r in rows),median_ms=statistics.median(r['elapsed_ms'] for r in rows))
        variant['summary']=summary
        variant['by_route']={route:dict(cases=len(group),median_ms=statistics.median(r['elapsed_ms'] for r in group),anchors_found=sum(sum(r['anchor_hits']) for r in group)) for route in {r.get('route','error') for r in rows} if (group:=[r for r in rows if r.get('route','error')==route])}
        print(name+': '+json.dumps(summary),flush=True)
    report['embedding_digest_unchanged']=report['embedding_digest']==engines['research'].model_digest()
    (folder/'results.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
    print('Saved:',folder)


if __name__=='__main__':main()
