"""Compare attribution repair instructions on identical saved failed claims."""
import argparse,copy,datetime as dt,hashlib,json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from app import Engine,read_json
from claim_repair import repair_claims
from evaluation.ragas_runner import save,request,local_url

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--ids');args=ap.parse_args()
    path=ROOT/'evaluation/readiness_runs/20261018T154442787264Z/capture.json'
    sources=[next(r for r in read_json(path)['rows'] if r['id']=='G-LIMIT-04')]
    phase_path=ROOT/'evaluation/quality_runs/20261019T181209842063Z/capture.json'
    sources.append(next(r for r in read_json(phase_path)['rows'] if r['id']=='RBI-REF-03'))
    if args.ids:
        ids=set(args.ids.split(','));assert ids<={s['id'] for s in sources}
        sources=[s for s in sources if s['id'] in ids]
    prior_path=ROOT/'evaluation/quality_review_20261019/before/claim_repair.py'
    prior={};exec(compile(prior_path.read_text(encoding='utf-8'),str(prior_path),'exec'),prior)
    config=read_json(ROOT/'config.json');engine=Engine(config=config)
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    record=dict(status='running',configuration=config,installed_models=request(local_url(config['ollama_url'])+'/api/tags',timeout=10),
        code_hashes={p.name:sha(p) for p in ROOT.glob('*.py')},source_capture_sha256=sha(path),
        phase_capture_sha256=sha(phase_path),
        baseline_repair_sha256=sha(prior_path),runner_sha256=sha(Path(__file__)),rows=[],
        caveat='Same frozen failed claims and evidence. A support-check acceptance is not independent correctness.')
    out=ROOT/'evaluation/quality_runs'/('repair-'+dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));out.mkdir(parents=True)
    save(out/'capture.json',record)
    for source in sources:
        response=source['response']
        for arm,fn in [('baseline',prior['repair_claims']),('candidate',repair_claims)]:
            start=time.monotonic()
            kept,flagged,checks,audit=fn(engine,copy.deepcopy(response['claims']),copy.deepcopy(response['flagged_claims']),
                copy.deepcopy(response['claim_checks']),copy.deepcopy(response['sources']),source['case']['query'])
            record['rows'].append(dict(id=source['id'],arm=arm,kept=kept,flagged=flagged,checks=checks,audit=audit,seconds=round(time.monotonic()-start,3)))
            save(out/'capture.json',record);print(source['id'],arm,[(a['status'],a.get('candidate',{}).get('text')) for a in audit],flush=True)
    record['snapshot_unchanged']=all(sha(ROOT/p)==h for p,h in record['code_hashes'].items()) and config==read_json(ROOT/'config.json')
    record['status']='complete';save(out/'capture.json',record);print(out,flush=True)

if __name__=='__main__':main()
