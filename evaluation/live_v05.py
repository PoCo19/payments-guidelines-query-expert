"""Local multi-product generation smoke checks, not an accuracy benchmark."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from app import Engine,read_json
from product_scope import memberships,source_coverage

e=Engine(config=read_json(ROOT/'config.products.json'));rows=[]
report={'fingerprint':e.fingerprint,'note':'Developer-selected live smoke cases; automated support checking is not independent expert verification.','rows':rows,'passed':False}
for product in ['AePS','CTS','IMPS','NACH','NETC','RuPay','UPI']:
 docs=[d for d in e.docs if d['series']==product and d['availability']=='converted' and e.parts_by_doc[d['id']] and not source_coverage(e,d['id'])['empty_pages']]
 # Short sources keep this reproducible local smoke check bounded.
 docs=[d for d in docs if not any(x in d['subject'].lower() for x in ['pcomp','compliance','self-attestation','self attestation']) and 120<=sum(len(p['text'].split()) for p in e.pages_by_doc[d['id']])<=450]
 d=sorted(docs,key=lambda d:d['id'])[0]
 q='State one operational instruction in the selected circular as one concise claim. Do not include dates or numerical limits.'
 r=e.answer(dict(query=q,document_ids=[d['id']],series=product,route='summary',method='hybrid',mode='generate',scope='strict'))
 assert r['sources'] and all(s['document_id']==d['id'] and product in memberships(s) for s in r['sources'])
 assert all(c.get('support_status')=='automated_supported' for c in r['claims'])
 rows.append(dict(product=product,document_id=d['id'],title=d['subject'],query=q,result=r))
 print(product,'claims',len(r['claims']),'withheld',len(r['flagged_claims']),'ms',r['elapsed_ms'],flush=True)
 (ROOT/'reports/v05_live_answers.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
for q in ['What does OC 13 require?','Compare UPI OC 186 and OC 999.']:
 r=e.answer(dict(query=q,mode='generate',method='hybrid'));assert r['abstained'] and not r['sources'];rows.append(dict(query=q,result=r))
report['passed']=True
(ROOT/'reports/v05_live_answers.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print('Live source-isolation, support-label and abstention checks passed.',flush=True)
