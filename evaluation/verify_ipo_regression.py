"""Capture live regression journeys; saved responses still require semantic review."""
import datetime as dt
import hashlib
import json
from pathlib import Path
import sys
import time
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from evaluation.ragas_runner import save


def main():
    query='Does the 10 lakh cumulative Capital Market figure in UPI OC185B make a single IPO mandate limit 10 lakh?'
    cases=[('exact_all_products',query,''),
           ('spaced_all_products',query.replace('OC185B','OC 185B'),''),
           ('exact_upi_filter',query,'UPI'),
           ('summary_control','Summarise OC 186A, covering the requirements across its sections.','UPI'),
           ('notification_known_failure','If a FASTag or NCMC automatic top-up does not need advance debit notice, can the issuer skip the message after the debit as well?',''),
           ('chronology_control','For UPI mandate execution, explain how response codes 59 and K1 were treated before and after the deemed-debit addendum.','UPI')]
    files=['app.py','scope_guard.py','claim_check.py','claim_repair.py','request_runtime.py','evaluation/verify_ipo_regression.py','config.json']
    hashes=lambda:{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in files}
    out=ROOT/'evaluation/ipo_regression_20261017'/dt.datetime.now(dt.timezone.utc).strftime('live_%Y%m%dT%H%M%SZ.json')
    report=dict(status='running',base_url='http://127.0.0.1:8765',code_and_config_hashes=hashes(),rows=[],
                limitation='Development regression capture. Successful transport/status is not answer correctness. Review every claim against its cited source.')
    save(out,report)
    for ident,question,series in cases:
        payload=dict(query=question,series=series,method='hybrid',scope='related',rerank=True,mode='generate')
        row=dict(id=ident,payload=payload);start=time.monotonic()
        try:
            req=urllib.request.Request(report['base_url']+'/api/answer',json.dumps(payload).encode(),{'Content-Type':'application/json'})
            with urllib.request.urlopen(req,timeout=160) as response:row['response']=json.load(response)
        except Exception as exc:row['error']=type(exc).__name__+': '+str(exc)
        row['wall_seconds']=round(time.monotonic()-start,3);report['rows'].append(row);save(out,report)
        print(ident,row.get('error') or row['response']['response_status'],row['wall_seconds'],flush=True)
    report.update(status='complete',code_and_config_unchanged=hashes()==report['code_and_config_hashes'])
    save(out,report);print(out,flush=True)
    return int(any(r.get('error') for r in report['rows']) or not report['code_and_config_unchanged'])


if __name__=='__main__':raise SystemExit(main())
