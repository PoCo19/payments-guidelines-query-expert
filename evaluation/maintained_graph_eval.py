"""Current-code maintained graph ablation. Development evidence, not acceptance."""
import argparse
import datetime as dt
import hashlib
import statistics
import sys
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app import Engine, read_json
from evaluation.ragas_runner import load_cases, case_payload, save, request, local_url
from evaluation.payments_eval import validate_anchors, source_hits
from tools.document_pipeline import input_hashes


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ids')
    parser.add_argument('--mode',choices=['evidence','generate'],default='evidence')
    args=parser.parse_args()
    config=read_json(ROOT/'config.json')
    engine=Engine(config=config)
    assert engine.vector_ready and engine.evidence_graph, 'Need a valid maintained graph and vector index.'
    graph=engine.evidence_graph
    engine.reference_graph=None
    cases=[];datasets={}
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    for name in ('context_regression_20261017','reference_graph_rbi_cases_20261018','notification_paraphrases_20261019'):
        path=ROOT/'evaluation'/f'{name}.json'
        loaded,fp=load_cases(path);cases.extend(loaded);datasets[str(path)]=fp
    assert len(cases)==144 and len({c['id'] for c in cases})==144
    if args.ids:
        ids=set(args.ids.split(','));assert ids<={c['id'] for c in cases}
        cases=[c for c in cases if c['id'] in ids]
    validate_anchors(cases,engine)
    code={p.name:sha(p) for p in ROOT.glob('*.py')}
    out=ROOT/'evaluation/maintained_graph_runs'/dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out.mkdir(parents=True)
    record=dict(status='running',mode=args.mode,configuration=config,code_hashes=code,
        runner_sha256=sha(Path(__file__)),dataset_hashes=datasets,source_hashes=input_hashes(engine.data_dir),
        models=request(local_url(config['ollama_url'])+'/api/tags',timeout=10),
        graph_fingerprint=graph.fingerprint,rows=[],
        caveat='AI-assisted development cases; not independent answer accuracy or held-out acceptance. '
            'Only maintained graph differs. Broader graph is off in both arms. Order alternates. First pair includes cold costs.')
    save(out/'capture.json',record)
    try:
        for index,case in enumerate(cases):
            for arm in (['off','on'] if index%2==0 else ['on','off']):
                engine.evidence_graph=graph if arm=='on' else None
                started=time.monotonic();row=dict(id=case['id'],case=case,arm=arm,cold_pair=index==0)
                try:
                    response=engine.answer(case_payload(case,mode=args.mode,method='hybrid',rerank=True))
                    row.update(status='ok',response=response,anchor_hits=source_hits(case,response))
                except Exception as exc:row.update(status='error',error=f'{type(exc).__name__}: {exc}')
                row['seconds']=round(time.monotonic()-started,3)
                record['rows'].append(row);save(out/'capture.json',record)
            print(case['id'],[(r['arm'],r.get('anchor_hits',r.get('error'))) for r in record['rows'][-2:]],flush=True)
    finally:engine.evidence_graph=graph
    paired={arm:{r['id']:r for r in record['rows'] if r['arm']==arm and r['status']=='ok'} for arm in ('off','on')}
    changes=[];controls=[]
    for key in paired['off'].keys() & paired['on'].keys():
        before,after=paired['off'][key],paired['on'][key]
        if before['anchor_hits']!=after['anchor_hits']:
            changes.append(dict(id=key,before=before['anchor_hits'],after=after['anchor_hits']))
        if not before['case']['references']:
            controls.append(dict(id=key,off=before['response']['response_status'],on=after['response']['response_status'],
                off_sources=len(before['response']['sources']),on_sources=len(after['response']['sources'])))
    summary={}
    for arm,rows in paired.items():
        warm=sorted(r['seconds'] for r in rows.values() if not r['cold_pair'])
        summary[arm]=dict(cases=len(rows),anchors_found=sum(sum(r['anchor_hits']) for r in rows.values()),
            anchors_expected=sum(len(c['references']) for c in cases),
            errors=sum(r['status']=='error' and r['arm']==arm for r in record['rows']),
            model_failures=sum(bool(r['response'].get('model_failure')) for r in rows.values()),
            median_warm_seconds=statistics.median(warm) if warm else None,
            p95_warm_seconds=warm[min(len(warm)-1,int(.95*len(warm)))] if warm else None,
            graph_routes={status:sum(r['response']['retrieval_trace'].get('graph_context',{}).get('status','not_invoked')==status for r in rows.values())
                for status in sorted({r['response']['retrieval_trace'].get('graph_context',{}).get('status','not_invoked') for r in rows.values()})})
    record.update(status='complete',summary=summary,anchor_changes=sorted(changes,key=lambda x:x['id']),
        negative_controls=sorted(controls,key=lambda x:x['id']),
        snapshot_unchanged=all(sha(ROOT/p)==h for p,h in code.items()) and read_json(ROOT/'config.json')==config
            and all(sha(Path(p))==h for p,h in datasets.items()) and input_hashes(engine.data_dir)==record['source_hashes'])
    save(out/'capture.json',record)
    print(summary,out,flush=True)
    return int(not record['snapshot_unchanged'] or any(s['errors'] or s['model_failures'] for s in summary.values()))


if __name__=='__main__':raise SystemExit(main())
