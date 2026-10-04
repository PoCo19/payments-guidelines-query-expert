"""Live generation and claim-check smoke cases; inspect saved excerpts."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from app import Engine
from claim_check import check_claims
e=Engine();rows=[]
queries=[('clause','Under OC 186A, who checks enablement before each transaction?'),('currency','Under OC 201, what are the monthly and per-transaction limits for full delegation?'),('summary','Summarise OC 186A, covering its sections.'),('compare','Compare OC 186 and OC 186A: distinguish the original NFC tap flow and later device-lock requirements.'),('missing','Compare OC 186 and OC 999.'),('outside','Explain quantum photosynthesis and chlorophyll.')]
for name,q in queries:
 r=e.answer(dict(query=q,method='hybrid',mode='generate',scope='related'));rows.append(dict(name=name,query=q,result=r));print(name,'claims',len(r['claims']),'flagged',len(r['flagged_claims']),'abstained',r['abstained'],'ms',r['elapsed_ms'],flush=True)
 (ROOT/'evaluation/v04_live_results.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False),encoding='utf-8')
sources=[dict(citation='S1',text='Explicit consent is required before enabling the feature.',method='text')]
kept,flagged,checks=check_claims(e,[dict(text='No consent is required before enabling the feature.',sources=['S1'])],sources)
assert not kept,'Contradictory live claim incorrectly passed'
(ROOT/'evaluation/v04_adversarial_check.json').write_text(json.dumps(dict(kept=kept,flagged=flagged,checks=checks),indent=2),encoding='utf-8')
print('Contradiction withheld.',flush=True)
