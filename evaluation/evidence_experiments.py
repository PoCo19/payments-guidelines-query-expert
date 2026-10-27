"""Paired contextual-BM25 or fixed-evidence synthesis experiments; no live activation."""
import argparse
import copy
import datetime as dt
import hashlib
import json
from pathlib import Path
import statistics
import sys
import time
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app import Engine, read_json
from evaluation.ragas_runner import load_cases, case_payload, save, request, local_url
from evaluation.payments_eval import source_hits, validate_anchors
from tools.document_pipeline import input_hashes


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--kind',choices=['context','synthesis'],required=True)
    ap.add_argument('--dataset',type=Path,default=ROOT/'evaluation/rag_cases.json')
    ap.add_argument('--config',type=Path,default=ROOT/'config.json')
    ap.add_argument('--ids')
    ap.add_argument('--method',choices=['bm25','vector','hybrid'],default='hybrid')
    ap.add_argument('--rerank',action=argparse.BooleanOptionalAction,default=True)
    args=ap.parse_args()
    cases,data_hash=load_cases(args.dataset)
    if args.ids:
        ids=set(args.ids.split(','));assert ids.issubset({c['id'] for c in cases})
        cases=[c for c in cases if c['id'] in ids]
    config=read_json(args.config)
    base=Engine(config=dict(config,contextual_bm25_enabled=False,structured_evidence_enabled=False))
    variant=Engine(config=dict(config,contextual_bm25_enabled=True,structured_evidence_enabled=False)) if args.kind=='context' else base
    validate_anchors(cases,base)
    out=ROOT/'evaluation/improvement_runs'/dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out.mkdir(parents=True)
    modules=['app.py','structured_evidence.py','contextual_retrieval.py','claim_check.py','claim_repair.py','scope_guard.py','adaptive_context.py','research.py','context.py','query_understanding.py','query_policies.json','product_scope.py','graph_context.py','source_quality_gate.py','source_quality_flags.json','evaluation/evidence_experiments.py','evaluation/ragas_runner.py']
    if config.get('evidence_graph_path'):modules.append(config['evidence_graph_path'])
    report=dict(kind=args.kind,status='running',configuration=config,dataset_sha256=data_hash,config_sha256=digest(args.config),
        source_hashes=input_hashes(base.data_dir),corpus_fingerprint=base.fingerprint,
        code_hashes={p:digest(ROOT/p) for p in modules},rows=[],method=args.method,rerank=args.rerank,
        caveat='AI-assisted development cases. No independent answer-accuracy score. Context experiment enriches lexical indexing only; dense vectors unchanged.')
    try:report['installed_models']=request(local_url(config['ollama_url'])+'/api/tags',timeout=10)
    except Exception as exc:report['model_metadata_error']=str(exc)
    save(out/'capture.json',report)
    legacy=args.dataset.name=='rag_cases.json'
    for i,case in enumerate(cases):
        payload=case_payload(case,method=args.method,rerank=args.rerank,mode='evidence' if args.kind=='context' else 'generate',legacy_upi=legacy)
        frozen=None
        if args.kind=='synthesis':
            frozen=base.answer(dict(payload,mode='evidence'))
            if frozen.get('model_failure'):raise RuntimeError('Cannot freeze fallback evidence')
        for arm in (['baseline','variant'] if i%2==0 else ['variant','baseline']):
            engine=base if arm=='baseline' else variant
            start=time.monotonic();row=dict(id=case['id'],arm=arm,query=case['query'])
            try:
                if frozen is not None:
                    engine.config['structured_evidence_enabled']=arm=='variant'
                    with patch('app.assemble',return_value=copy.deepcopy((frozen['sources'],frozen['retrieval_trace']))):
                        response=engine.answer(payload)
                else:response=engine.answer(payload)
                row.update(status='ok',response=response,anchor_hits=source_hits(case,response),
                           negative=bool(case.get('expect_abstain')),wall_seconds=round(time.monotonic()-start,3))
                if args.kind=='context' and payload.get('route') not in ('summary','compare'):
                    candidate_start=time.monotonic()
                    candidates=engine.search(case['query'],method=args.method,series=payload.get('series',''),cutoff=payload.get('cutoff',''),k=6)
                    row['raw_top6']=[{k:p.get(k) for k in ('id','document_id','page','text','score')} for p in candidates]
                    row['raw_top6_anchor_hits']=source_hits(case,{'sources':candidates})
                    row['raw_top6_seconds']=round(time.monotonic()-candidate_start,3)
            except Exception as exc:row.update(status='error',error=type(exc).__name__+': '+str(exc))
            report['rows'].append(row);save(out/'capture.json',report)
            print(case['id'],arm,row['status'],row.get('anchor_hits'),row.get('wall_seconds'),flush=True)
    summary={}
    for arm in ('baseline','variant'):
        rows=[r for r in report['rows'] if r['arm']==arm];ok=[r for r in rows if r['status']=='ok']
        summary[arm]=dict(cases=len(rows),errors=len(rows)-len(ok),anchors_found=sum(sum(r['anchor_hits']) for r in ok),
            anchors_expected=sum(len(c['references']) for c in cases),
            negative_abstained=sum(r['negative'] and r['response']['abstained'] for r in ok),negative_cases=sum(bool(c.get('expect_abstain')) for c in cases),
            incomplete=sum(r['response'].get('response_status')=='incomplete' for r in ok),
            model_fallbacks=sum(bool(r['response'].get('model_failure')) for r in ok),
            median_seconds=statistics.median([r['wall_seconds'] for r in ok]) if ok else None)
    report.update(status='complete',summary=summary)
    report['snapshot_unchanged']=(input_hashes(base.data_dir)==report['source_hashes'] and digest(args.dataset)==data_hash and digest(args.config)==report['config_sha256'] and all(digest(ROOT/p)==h for p,h in report['code_hashes'].items()))
    report['benchmark_valid']=report['snapshot_unchanged'] and not report.get('model_metadata_error') and all(not s['errors'] and not s['model_fallbacks'] for s in summary.values())
    save(out/'capture.json',report)
    (out/'summary.md').write_text('# '+args.kind+' experiment\n\n'+report['caveat']+'\n\n```json\n'+json.dumps(summary,indent=2)+'\n```\n',encoding='utf-8')
    print(out,flush=True)
    return int(not report['benchmark_valid'])


if __name__=='__main__':raise SystemExit(main())
