"""Paired development retrieval check; no independent answer-quality claim."""
import argparse,hashlib,json,sys,time
from datetime import datetime,timezone
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app import Engine,read_json
from evaluation.ragas_runner import load_cases,case_payload
from evaluation.payments_eval import source_hits


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--config',type=Path,default=ROOT/'config.json')
    args=parser.parse_args()
    out=args.output
    out.mkdir(parents=True,exist_ok=True)
    path=out/'retrieval-pairs.json'
    if path.exists():raise SystemExit('Preserve previous results; choose another output for a repeat.')
    engine=Engine(config=read_json(args.config))
    cases=[];datasets={}
    for name in ('context_regression_20261017','reference_graph_rbi_cases_20261018','notification_paraphrases_20261019'):
        source=ROOT/'evaluation'/f'{name}.json'
        loaded,fp=load_cases(source);cases.extend(loaded);datasets[name]=fp
    record=dict(status='running',started=datetime.now(timezone.utc).isoformat(),datasets=datasets,corpus=engine.fingerprint,
        config_sha256=hashlib.sha256(args.config.read_bytes()).hexdigest(),
        graph=engine.evidence_graph.fingerprint,models={k:engine.config[k] for k in ('generation_model','embedding_model')},
        code_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.glob('*.py')},rows=[],
        limitation='Existing development cases. Both arms keep graph enabled. Only overview amendment recovery differs. No answer correctness score.')
    def save():path.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
    for i,case in enumerate(cases):
        row=dict(id=case['id'],case=case)
        for arm in (['before','after'] if i%2==0 else ['after','before']):
            start=time.monotonic()
            try:
                payload=case_payload(case,mode='evidence',method='hybrid',rerank=True)
                if arm=='before':
                    with patch('evidence_focus.overview_change_matches',return_value=[]):r=engine.answer(payload)
                else:r=engine.answer(payload)
                row[arm]=dict(hits=source_hits(case,r),status=r['response_status'],sources=r['sources'],trace=r['retrieval_trace'],seconds=round(time.monotonic()-start,3))
            except Exception as exc:row[arm]=dict(error=str(exc))
        record['rows'].append(row);save()
        print(i+1,case['id'],row['before'].get('hits'),row['after'].get('hits'),flush=True)
    record['summary']={arm:dict(anchors_found=sum(sum(r[arm].get('hits',[])) for r in record['rows']),errors=sum('error' in r[arm] for r in record['rows'])) for arm in ('before','after')}
    record['losses']=[r['id'] for r in record['rows'] if any(a and not b for a,b in zip(r['before'].get('hits',[]),r['after'].get('hits',[])))]
    record['status']='complete';save();print(record['summary'],record['losses'],flush=True)
    return bool(record['losses'] or any(v['errors'] for v in record['summary'].values()))


if __name__=='__main__':raise SystemExit(main())
