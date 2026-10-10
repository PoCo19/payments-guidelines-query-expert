"""Record a real, bounded answer with stage/model timings; no configuration mutation."""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from app import Engine,read_json

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config',type=Path,default=ROOT/'config.json')
    p.add_argument('--query',default='For e-mandates that automatically replenish FASTag or NCMC balances, is pre-transaction notification required? Answer briefly with the exception and cite the source.')
    args=p.parse_args();config=read_json(args.config);engine=Engine(config=config)
    out=ROOT/'reports/latency'/dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ');out.mkdir(parents=True)
    from request_runtime import PROGRESS
    token=PROGRESS.set(lambda message:print(message,flush=True))
    record=dict(query=args.query,config=config,config_sha256=hashlib.sha256(args.config.read_bytes()).hexdigest(),corpus_fingerprint=engine.fingerprint,
                code_hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ('app.py','request_runtime.py','claim_check.py','research.py')},
                limitation='One developer observation; not a controlled performance or answer-quality benchmark.')
    try:record['response']=engine.answer(dict(query=args.query,method='hybrid',mode='generate',scope='related'))
    except Exception as exc:record['error']=str(exc)
    finally:PROGRESS.reset(token)
    (out/'result.json').write_text(json.dumps(record,indent=2,ensure_ascii=False),encoding='utf-8')
    r=record.get('response',{});print(json.dumps(dict(path=str(out),claims=r.get('claims'),timing=r.get('timing'),coverage=r.get('coverage_check'),error=record.get('error')),ensure_ascii=False),flush=True)

if __name__=='__main__':main()
