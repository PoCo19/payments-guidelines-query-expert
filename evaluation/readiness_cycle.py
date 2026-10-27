"""Capture a readiness iteration against the frozen development regression set."""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import statistics
import sys
import time
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app import Engine,read_json
from evaluation.ragas_runner import load_cases,case_payload,save,request,local_url
from evaluation.payments_eval import validate_anchors,source_hits
from tools.document_pipeline import input_hashes


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--ids')
    ap.add_argument('--mode',choices=['evidence','generate'],default='evidence')
    args=ap.parse_args()
    path=ROOT/'evaluation/context_regression_20261017.json'
    cases,fingerprint=load_cases(path)
    if args.ids:
        selected=set(args.ids.split(','));assert selected<={c['id'] for c in cases}
        cases=[c for c in cases if c['id'] in selected]
    config=read_json(ROOT/'config.json')
    models=request(local_url(config['ollama_url'])+'/api/tags',timeout=10)
    engine=Engine(config=config);assert engine.vector_ready
    validate_anchors(cases,engine)
    baseline=read_json(ROOT/'evaluation/improvement_runs/20261017T145242617297Z/capture.json')
    old={r['id']:r for r in baseline['rows'] if r['arm']=='baseline'}
    hashes=lambda:{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.glob('*.py'))}
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    out=ROOT/'evaluation/readiness_runs'/dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out.mkdir(parents=True,exist_ok=False)
    record=dict(status='running',mode=args.mode,configuration=config,dataset_sha256=fingerprint,
        config_sha256=sha(ROOT/'config.json'),source_hashes=input_hashes(engine.data_dir),code_hashes=hashes(),
        runner_sha256=sha(Path(__file__)),installed_models=models,rows=[],
        caveat='Existing AI-assisted development cases. No independent answer-accuracy claim.')
    assert record['source_hashes']==baseline['source_hashes'] and record['config_sha256']==baseline['config_sha256']
    save(out/'capture.json',record)
    for c in cases:
        start=time.monotonic();row=dict(id=c['id'],case=c)
        try:
            r=engine.answer(case_payload(c,mode=args.mode,method='hybrid',rerank=True))
            hits=source_hits(c,r);before=old[c['id']]['anchor_hits']
            row.update(status='ok',response=r,anchor_hits=hits,baseline_anchor_hits=before,
                lost=sum(a and not b for a,b in zip(before,hits)),gained=sum(not a and b for a,b in zip(before,hits)))
        except Exception as exc:row.update(status='error',error=f'{type(exc).__name__}: {exc}')
        row['seconds']=round(time.monotonic()-start,3);record['rows'].append(row);save(out/'capture.json',record)
        print(c['id'],row['status'],row.get('anchor_hits'),row['seconds'],flush=True)
    rows=record['rows'];ok=[r for r in rows if r['status']=='ok']
    record['summary']=dict(cases=len(rows),errors=len(rows)-len(ok),
        anchors_found=sum(sum(r['anchor_hits']) for r in ok),anchors_expected=sum(len(c['references']) for c in cases),
        lost=sum(r['lost'] for r in ok),gained=sum(r['gained'] for r in ok),
        model_fallbacks=sum(bool(r['response'].get('model_failure')) for r in ok),
        coverage_reviews_unavailable=sum(r['response'].get('coverage_check',{}).get('status')=='unavailable' for r in ok),
        coverage_reviews_flagged=sum(r['response'].get('coverage_check',{}).get('status')=='issues_flagged' for r in ok),
        support_checks_unavailable=sum(bool(c.get('failure_reason')) for r in ok for c in r['response'].get('claim_checks',[])),
        median_seconds=statistics.median(r['seconds'] for r in ok) if ok else None)
    record['snapshot_unchanged']=(record['source_hashes']==input_hashes(engine.data_dir) and record['code_hashes']==hashes()
        and record['config_sha256']==sha(ROOT/'config.json') and fingerprint==sha(path))
    record['status']='complete';record['benchmark_valid']=record['snapshot_unchanged'] and not record['summary']['errors'] and not record['summary']['model_fallbacks']
    record['benchmark_valid_meaning']='Execution/input integrity only. Does not certify answer correctness or successful coverage review; inspect separate review counts and complete responses.'
    save(out/'capture.json',record)
    print(json.dumps(record['summary']),out,flush=True)
    return int(not record['benchmark_valid'])


if __name__=='__main__':raise SystemExit(main())
