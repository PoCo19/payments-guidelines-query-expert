"""Repeat saved development failures with runtime telemetry; never acceptance scoring."""
import argparse,copy,datetime as dt,hashlib,json,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app import Engine,read_json
from claim_check import check_claims
from claim_repair import repair_claims
from evaluation.ragas_runner import save,request,local_url,case_payload
from request_runtime import CURRENT,Run
from tools.document_pipeline import input_hashes

def gpu():
    try:
        result=subprocess.run(['nvidia-smi','--query-gpu=name,memory.total,memory.used,utilization.gpu','--format=csv,noheader'],capture_output=True,text=True,timeout=5)
        return dict(status='available' if result.returncode==0 else 'unavailable',reading=result.stdout.strip())
    except (OSError,subprocess.TimeoutExpired):return dict(status='unavailable')

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repeats',type=int,default=2)
    ap.add_argument('--replay-only',action='store_true',help='Only recheck and repair the exact saved registry-label claim')
    args=ap.parse_args()
    if not 1<=args.repeats<=3:ap.error('repeats must be 1 to 3')
    prior_path=ROOT/'evaluation/maintained_graph_runs/20261022T171138330902Z/capture.json'
    prior=read_json(prior_path)
    cases={r['id']:r['case'] for r in prior['rows']}
    config=read_json(ROOT/'config.json');engine=Engine(config=config)
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    out=ROOT/'evaluation/readiness_diagnostics'/dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out.mkdir(parents=True)
    record=dict(status='running',mode='frozen_claim_replay' if args.replay_only else 'answers_and_replay',configuration=config,code_hashes={p.name:sha(p) for p in ROOT.glob('*.py')},
        runner_sha256=sha(Path(__file__)),input_capture_sha256=sha(prior_path),source_hashes=input_hashes(engine.data_dir),
        graph_fingerprint=engine.evidence_graph.fingerprint if engine.evidence_graph else None,
        installed_models=request(local_url(config['ollama_url'])+'/api/tags',timeout=10),gpu_start=gpu(),rows=[],
        caveat='Repeat of known development failures; no held-out or independent correctness score. First request includes cold costs. GPU readings are boundary samples, not continuous load control.')
    save(out/'capture.json',record)
    failures=0
    for repeat in range(0 if args.replay_only else args.repeats):
        for case_id,case in cases.items():
            row=dict(id=case_id,repeat=repeat+1,cold_candidate=not record['rows'],gpu_before=gpu())
            started=time.monotonic()
            try:
                result=engine.answer(case_payload(case,mode='generate',method='hybrid',rerank=True))
                row.update(response=result,status='model_failure' if result.get('model_failure') else 'completed')
            except Exception as exc:row.update(status='error',error_type=type(exc).__name__,error=str(exc)[:300])
            row.update(seconds=round(time.monotonic()-started,3),gpu_after=gpu())
            record['rows'].append(row);save(out/'capture.json',record)
            print(case_id,repeat+1,row['status'],row.get('response',{}).get('response_status'),row['seconds'],flush=True)
            failures+=row['status']!='completed'
            if failures>=2:break
        if failures>=2:break
    # The same saved claim and exact evidence isolate label normalization from
    # generation variability. A checker acceptance is still not expert review.
    source=next(r['response'] for r in prior['rows'] if r['id']=='G-IPO-02' and r['arm']=='on')
    originals=[a['original'] for a in source.get('claim_repairs',[]) if '(document ' in a['original']['text']]
    if originals and failures<2:
        run=Run(config);token=CURRENT.set(run)
        try:
            kept,flagged,checks=check_claims(engine,copy.deepcopy(originals),source['sources'])
            record['frozen_claim_replay']=dict(originals=originals,kept=kept,flagged=flagged,checks=checks,timing=run.report())
            fixed,remaining,review,audit=repair_claims(engine,copy.deepcopy(kept),copy.deepcopy(flagged),copy.deepcopy(checks),source['sources'],cases['G-IPO-02']['query'])
            record['frozen_claim_repair']=dict(kept=fixed,flagged=remaining,checks=review,audit=audit,timing=run.report())
        finally:CURRENT.reset(token)
    record.update(status='stopped_after_failures' if failures>=2 else 'complete',model_failures=failures,
        snapshot_unchanged=all(sha(ROOT/p)==h for p,h in record['code_hashes'].items()) and read_json(ROOT/'config.json')==config and input_hashes(engine.data_dir)==record['source_hashes'])
    save(out/'capture.json',record);print(out,flush=True)
    return int(bool(failures) or not record['snapshot_unchanged'])

if __name__=='__main__':raise SystemExit(main())
