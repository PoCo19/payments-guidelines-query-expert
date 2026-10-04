"""Check presentation with the installed models, preserving full answer evidence."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from app import Engine

e=Engine();rows=[]
cases=[
 ('short_auto','Under UPI OC 186A, who checks enablement before each transaction? Answer briefly.','auto'),
 ('list_auto','List three requirements for UPI Tap & Pay under OC 186A as bullet points.','auto'),
 ('mixed','Explain UPI Tap & Pay under OC 186A: one short overview followed by two specific requirements. Keep it concise.','mixed')]
for name,query,style in cases:
 r=e.answer(dict(query=query,mode='generate',method='hybrid',scope='strict',answer_style=style))
 blocks=r['answer_blocks'];flat=[c for b in blocks for c in b['claims']]
 assert flat and sorted(c['draft_index'] for c in flat)==sorted(c['draft_index'] for c in r['claims'])
 assert all(c['support_status']=='automated_supported' for c in flat)
 assert not {c['draft_index'] for c in flat}.intersection(c['draft_index'] for c in r['flagged_claims'])
 if name=='short_auto':assert all(b['type']=='paragraph' for b in blocks)
 if name=='list_auto':assert all(b['type']=='bullets' for b in blocks)
 if name=='mixed':assert any(b['type']=='paragraph' for b in blocks) and any(b['type'] in ('bullets','steps') for b in blocks)
 rows.append(dict(name=name,query=query,result=r))
 (ROOT/'reports/v051_live_formatting.json').write_text(json.dumps(dict(fingerprint=e.fingerprint,rows=rows,passed=len(rows)==len(cases)),ensure_ascii=False,indent=2),encoding='utf-8')
 print(name,[b['type'] for b in blocks],r['formatting_source'],'claims',len(flat),'withheld',len(r['flagged_claims']),'ms',r['elapsed_ms'],flush=True)
