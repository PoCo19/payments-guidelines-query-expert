"""Development smoke cases, not independent payments-answer acceptance."""
import json,sys,time,hashlib
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from app import Engine,ROOT,read_json
out=Path(__file__).parent
engine=Engine(config=read_json(ROOT/'config.json'))
cases=[('gibberish','asdfg qwerty zzzxv 123blah'),
       ('unrelated','How do I bake a chocolate cake?'),
       ('invented_reference','Summarise UPI OC999999.'),
       ('short_explanation','What is UPI Lite? Answer briefly.'),
       ('scope_history','Does the 10 lakh cumulative Capital Market figure in UPI OC185B make a single IPO mandate limit 10 lakh?')]
metadata=dict(corpus_fingerprint=engine.fingerprint,config_sha256=hashlib.sha256((ROOT/'config.json').read_bytes()).hexdigest(),
              generation_model=engine.config['generation_model'],embedding_model=engine.config['embedding_model'],
              purpose='Development regression smoke; no independent correctness score.')
(out/'smoke-config.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')
for name,query in cases:
 start=time.monotonic()
 try:r=engine.answer(dict(query=query,mode='generate',answer_style='auto',series='UPI'))
 except Exception as exc:r=dict(error=type(exc).__name__+': '+str(exc))
 row=dict(case=name,query=query,elapsed_seconds=round(time.monotonic()-start,3),result=r)
 (out/(name+'.json')).write_text(json.dumps(row,indent=2,ensure_ascii=False),encoding='utf-8')
 print(json.dumps(dict(case=name,status=r.get('response_status'),claims=len(r.get('claims',[])),error=r.get('error'),elapsed_seconds=row['elapsed_seconds'])),flush=True)
