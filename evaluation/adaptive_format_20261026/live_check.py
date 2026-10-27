"""Small development smoke check, not independent answer-quality evaluation."""
import json, sys, time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from app import Engine, read_json, ROOT

engine=Engine(config=read_json(ROOT/'config.json'))
original_ollama=engine.ollama
raw_generations=[]
def recorded_ollama(endpoint,payload):
    reply=original_ollama(endpoint,payload)
    if endpoint=='/api/generate' and 'layout' in payload.get('format',{}).get('properties',{}):
        raw_generations.append(reply.get('response'))
    return reply
engine.ollama=recorded_ollama
questions=[
    'Compare UPI OC128 and OC128A on the treatment of response codes 59 and K1. Give a short explanation and, if useful, a comparison table followed by key qualifications.',
    'What is UPI Lite? Answer briefly.',
]
if '--simple' in sys.argv:
    questions=['Compare the purposes of UPI Lite and UPI Tap & Pay in a two-column table. Keep each cell self-contained and the answer brief.']
out=Path(__file__).parent
for i,q in enumerate(questions,1):
    raw_generations.clear()
    start=time.monotonic()
    result=engine.answer(dict(query=q,mode='generate',series='UPI',answer_style='auto'))
    record=dict(question=q,elapsed_seconds=round(time.monotonic()-start,3),result=result,raw_generations=raw_generations)
    suffix=sys.argv[1] if len(sys.argv)>1 else ''
    (out/f'live-{i}{suffix}.json').write_text(json.dumps(record,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps(dict(case=i,status=result.get('response_status'),formatting_source=result.get('formatting_source'),blocks=[b['type'] for b in result.get('answer_blocks',[])],claims=len(result.get('claims',[])),elapsed_seconds=record['elapsed_seconds'])),flush=True)
