"""Small paired follow-up on new wording, with focus recovery ablated in baseline."""
import copy
import datetime as dt
import hashlib
import json
from pathlib import Path
import sys
import time
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app import Engine,read_json
from evaluation.ragas_runner import case_payload,save,request,local_url
from evaluation.payments_eval import source_hits,validate_anchors
from tools.document_pipeline import input_hashes


def main():
    parents={c['id']:c for c in read_json(ROOT/'evaluation/expanded_evidence_cases_20261017.json')}
    questions=[('X-PAY-015','For automatic FASTag balance replenishment, does exemption from pre-transaction notification also remove the post-transaction notification duty?'),
               ('X-PAY-015','NCMC auto-replenishment: what notice is due before the debit and what message must follow after the debit?'),
               ('X-LIMIT-03','Under UPI, what is the credit card bill payment limit for one transaction versus the cumulative limit in 24 hours?'),
               ('X-LIMIT-03','Is the daily cap for UPI credit-card bill payments identical to the single-transaction ceiling?')]
    cases=[]
    for i,(parent,query) in enumerate(questions,1):
        c=copy.deepcopy(parents[parent]);c.update(id=f'READY-{i:02}',query=query,parent_case=parent);cases.append(c)
    config=read_json(ROOT/'config.json');models=request(local_url(config['ollama_url'])+'/api/tags',timeout=10)
    engine=Engine(config=config);validate_anchors(cases,engine)
    out=ROOT/'evaluation/readiness_runs'/('paraphrases-'+dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
    out.mkdir(parents=True)
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    code={str(p.relative_to(ROOT)):sha(p) for p in ROOT.glob('*.py')}
    record=dict(status='running',cases=cases,configuration=config,source_hashes=input_hashes(engine.data_dir),code_hashes=code,
        runner_sha256=sha(Path(__file__)),installed_models=models,rows=[],
        caveat='New AI-assisted paraphrases of development cases, not held-out or independently reviewed. Baseline disables only table/phase recovery; no answers generated.')
    save(out/'capture.json',record)
    for i,c in enumerate(cases):
        for arm in (['baseline','focused'] if i%2==0 else ['focused','baseline']):
            start=time.monotonic();payload=case_payload(c,mode='evidence',method='hybrid',rerank=True)
            if arm=='baseline':
                with patch('evidence_focus.table_matches',return_value=[]),patch('evidence_focus.phase_companions',return_value=[]):r=engine.answer(payload)
            else:r=engine.answer(payload)
            row=dict(id=c['id'],arm=arm,response=r,anchor_hits=source_hits(c,r),seconds=round(time.monotonic()-start,3))
            record['rows'].append(row);save(out/'capture.json',record);print(c['id'],arm,row['anchor_hits'],flush=True)
    record['snapshot_unchanged']=(record['source_hashes']==input_hashes(engine.data_dir) and all(sha(ROOT/p)==h for p,h in code.items()) and config==read_json(ROOT/'config.json'))
    record['benchmark_valid']=record['snapshot_unchanged'] and not any(r['response'].get('model_failure') for r in record['rows'])
    record['status']='complete';save(out/'capture.json',record);print(out,flush=True)


if __name__=='__main__':main()
