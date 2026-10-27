"""Validate an independently reviewed pack before capturing supervised workflows.

The provisional pack intentionally fails this gate. This runner does not grade
answer correctness or impersonate a payments reviewer.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from evaluation.ragas_runner import save


def validate(pack):
    pack=Path(pack)
    data=json.loads((pack/'cases.json').read_text(encoding='utf-8'))
    manifest=json.loads((pack/'manifest.json').read_text(encoding='utf-8'))
    errors=[]
    sha=hashlib.sha256((pack/'cases.json').read_bytes()).hexdigest()
    if sha!=manifest.get('dataset_sha256'):errors.append('Dataset fingerprint differs from manifest.')
    if manifest.get('review_gate')!='approved' or manifest.get('scoring_allowed') is not True:
        errors.append('Independent reference review is pending.')
    cases=data.get('cases',[])
    if len(cases)!=50 or len({c['id'] for c in cases})!=50:errors.append('Need 50 unique cases.')
    if sum(c['id'].startswith('QD-') for c in cases)!=20 or sum(c['id'].startswith('IB-') for c in cases)!=10 or sum(c['id'].startswith('NC-') for c in cases)!=20:
        errors.append('Need 20 Query Desk, 10 brief and 20 control cases.')
    for case in cases:
        if case.get('review_status')!='independently_reviewed' or not case.get('reviewer') or case.get('originals_verified') is not True:
            errors.append(case['id']+': missing independent original-source review.')
        if not case.get('expected_outcome') or not isinstance(case.get('essential_qualifications'),list):
            errors.append(case['id']+': missing expected outcome/qualification list.')
        if not isinstance(case.get('references'),list):
            errors.append(case['id']+': reference list must be explicit (empty only for a reviewed no-evidence outcome).')
    for name,total,field in [('graph_anchors.csv',55,'verified'),('graph_relationships.csv',13,'approved')]:
        with (pack/name).open(encoding='utf-8-sig',newline='') as stream:rows=list(csv.DictReader(stream))
        if len(rows)!=total or any(not r.get('reviewer','').strip() or r.get(field,'').strip().lower() not in ('yes','true') for r in rows):
            errors.append(f'{name}: all {total} entries require attributed independent review.')
    return cases,manifest,errors


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pack',type=Path,required=True)
    parser.add_argument('--capture',action='store_true')
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    cases,manifest,errors=validate(args.pack)
    if errors:
        print(json.dumps(dict(status='blocked_pending_review',errors=errors),indent=2))
        return 2
    if not args.capture:
        print('Review pack gate passed; no model execution or acceptance score.')
        return 0
    if not args.out:parser.error('--out must name a new capture directory')
    from app import Engine,read_json
    from work_items import WorkStore
    from tools.document_pipeline import input_hashes
    from evaluation.payments_eval import validate_anchors
    from evaluation.ragas_runner import request,local_url
    engine=Engine(config=read_json(ROOT/'config.json'))
    if input_hashes(engine.data_dir)!=manifest['source_hashes']:raise ValueError('Source release changed since review.')
    graph=engine.evidence_graph
    if not graph or hashlib.sha256((ROOT/engine.config['evidence_graph_path']).read_bytes()).hexdigest()!=manifest['graph_sha256']:
        raise ValueError('Graph changed since review.')
    validate_anchors(cases,engine)
    args.out.mkdir(parents=True,exist_ok=False)
    store=WorkStore(args.out/'acceptance-workflows.sqlite3')
    record=dict(status='running',dataset_sha256=manifest['dataset_sha256'],configuration=engine.config,
        source_hashes=input_hashes(engine.data_dir),models=request(local_url(engine.config['ollama_url'])+'/api/tags'),
        graph=graph.fingerprint,rows=[],scoring='Independent correctness and citation scoring remains required. First case includes cold costs.')
    save(args.out/'capture.json',record)
    for i,case in enumerate(cases):
        started=time.monotonic();row=dict(id=case['id'],kind=case['kind'],cold_start=i==0)
        try:
            item=store.create(case,engine)
            item=store.generate(item['id'],item['revision'],engine)
            row.update(status='captured',item=item)
        except Exception as exc:row.update(status='error',error=f'{type(exc).__name__}: {exc}')
        row['seconds']=round(time.monotonic()-started,3)
        record['rows'].append(row);save(args.out/'capture.json',record)
        print(row['id'],row['status'],row['seconds'],flush=True)
    record['status']='captured_awaiting_independent_scoring'
    save(args.out/'capture.json',record)
    return int(any(r['status']=='error' for r in record['rows']))


if __name__=='__main__':raise SystemExit(main())
