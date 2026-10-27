"""Compare a narrow generation instruction with unchanged retrieval and checking."""
import datetime as dt,hashlib,json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from app import Engine,read_json
from evaluation.ragas_runner import load_cases,case_payload,save,request,local_url
from evaluation.payments_eval import source_hits
from tools.document_pipeline import input_hashes

GUIDANCE=(' Before finalising an amount-based answer, read the applicability passages from that same circular. '
    'State any material eligibility restriction together with the amount, and cite both passages when needed. '
    'A later circular that recalls an earlier enhancement is evidence that it REFERENCES the earlier rule; '
    'do not say both circulars independently introduced or set that enhancement. '
    'Avoid repeating the same conclusion across multiple claims. Each claim should add a distinct answer-relevant fact.')

def main():
    config=read_json(ROOT/'config.json');e=Engine(config=config);assert e.vector_ready
    cases,fp=load_cases(ROOT/'evaluation/context_regression_20261017.json')
    ids={'X-LIMIT-03','G-LIMIT-04','G-IPO-02','G-DD-01'};cases=[c for c in cases if c['id'] in ids]
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    out=ROOT/'evaluation/quality_runs'/('generation-'+dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));out.mkdir(parents=True)
    record=dict(status='running',configuration=config,installed_models=request(local_url(config['ollama_url'])+'/api/tags',timeout=10),
        code_hashes={p.name:sha(p) for p in ROOT.glob('*.py')},source_hashes=input_hashes(e.data_dir),dataset_sha256=fp,
        guidance=GUIDANCE,runner_sha256=sha(Path(__file__)),rows=[],caveat='Development experiment. All raw answers retained; correctness requires review.')
    original=e.ollama
    def candidate(endpoint,payload):
        if 'abstain' in payload.get('format',{}).get('properties',{}):
            payload=dict(payload,system=payload['system']+GUIDANCE)
        return original(endpoint,payload)
    save(out/'capture.json',record)
    try:
        for i,c in enumerate(cases):
            for arm in (['baseline','candidate'] if i%2==0 else ['candidate','baseline']):
                e.ollama=original if arm=='baseline' else candidate
                start=time.monotonic();response=e.answer(case_payload(c,mode='generate',method='hybrid',rerank=True))
                record['rows'].append(dict(id=c['id'],case=c,arm=arm,response=response,anchor_hits=source_hits(c,response),seconds=round(time.monotonic()-start,3)))
                save(out/'capture.json',record);print(c['id'],arm,response['response_status'],[(r['text']) for r in response['claims']],flush=True)
    finally:e.ollama=original
    record['snapshot_unchanged']=all(sha(ROOT/p)==h for p,h in record['code_hashes'].items()) and config==read_json(ROOT/'config.json') and record['source_hashes']==input_hashes(e.data_dir)
    record['status']='complete';save(out/'capture.json',record);print(out,flush=True)

if __name__=='__main__':main()
