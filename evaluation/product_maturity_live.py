"""Small development probe: preserve all outputs; not independent acceptance."""
import argparse
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app import Engine,read_json
from work_items import WorkStore


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--config',type=Path,default=ROOT/'config.json')
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    engine=Engine(config=read_json(args.config))
    meta=dict(started=datetime.now(timezone.utc).isoformat(),corpus=engine.fingerprint,
              graph=engine.evidence_graph.fingerprint,
              config_sha256=hashlib.sha256(args.config.read_bytes()).hexdigest(),
              code_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.glob('*.py')})
    try:
        with urlopen('http://127.0.0.1:11434/api/tags',timeout=10) as r:meta['models']=json.load(r)
    except Exception as exc:meta['model_metadata_error']=str(exc)
    (args.output/'metadata.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
    cases=[('lite_limits','What are the UPI Lite transaction and total balance limits?',{}),
           ('lite_paraphrase','Explain UPI Lite in simple words.',{}),
           ('historical','What limit did UPI OC169 introduce?',{'document_ids':['2023-UPI-169'],'scope':'strict'}),
           ('ipo_control','Does the 10 lakh cumulative Capital Market figure in UPI OC185B make a single IPO mandate limit 10 lakh?',{}),
           ('gibberish','asdfgh zxqv blorpt',{}),
           ('invented','What does UPI OC999999 say about fees?',{})]
    for name,query,scope in cases:
        start=time.monotonic()
        payload=dict(query=query,mode='generate',method='hybrid',rerank=True,answer_style='auto',**scope)
        try:record=dict(request=payload,result=engine.answer(payload))
        except Exception as exc:record=dict(request=payload,error=str(exc))
        record['seconds']=round(time.monotonic()-start,3)
        (args.output/(name+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
        print(name,record.get('result',{}).get('response_status',record.get('error')),record['seconds'],flush=True)
    store=WorkStore(ROOT/'data/qa-maturity-20261028/live-check.sqlite3')
    item=store.create(dict(kind='impact',query='What changed in the UPI Lite limits addendum compared with the baseline? Include source-backed conditions and dates, and identify unresolved points.',document_ids=['2025-OC-169A','2023-UPI-169']),engine)
    start=time.monotonic()
    item=store.generate(item['id'],item['revision'],engine)
    (args.output/'change-revised.json').write_text(json.dumps(dict(seconds=time.monotonic()-start,item=item),ensure_ascii=False,indent=2),encoding='utf-8')
    print('change-revised',item['draft']['result']['response_status'],flush=True)


if __name__=='__main__':main()
