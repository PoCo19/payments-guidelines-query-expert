"""Explicit transcriptions checked against the ten saved PDF page images.
No model-generated bulk replacement or global OCR cleanup is performed.
"""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
sample=json.loads((HERE/'sample.json').read_text(encoding='utf-8'))
pages=[json.loads(line) for line in (Path(sample['baseline'])/'all_circular_pages.jsonl').open(encoding='utf-8-sig') if line.strip()]
edits=[]
def add(doc,page,pairs):
    text=next(p['text'] for p in pages if p['document_id']==doc and p['source_page']==page)
    replacements=[]
    for old,new in pairs:
        assert text.count(old)==1,(doc,page,old)
        replacements.append(dict(before=old,after=new))
    edits.append(dict(document_id=doc,page=page,before_page_sha256=hashlib.sha256(text.encode('utf-8')).hexdigest(),replacements=replacements))

add('2024-OC-107A',1,[( '19" April, 2024','19th April, 2024'),('01* April, 2021','01st April, 2021'),('31%, May 2024','31st May 2024')])
add('2023-UPI-186',1,[('NPCIUPIOG No.186/2023-24 19" December 2023','NPCI/UPI/OC No.186/2023-24 19th December 2023')])
add('2023-UPI-186',2,[('31% January’ 2024','31st January’ 2024')])
add('2025-OC-193A',1,[('10" September 2024','10th September 2024'),('28" March 2024','28th March 2024')])
add('2025-OC-193A',2,[('NPCHUPIOG No. 193/2023-24','NPCI/UPI/OC No. 193/2023-24')])
add('2025-OC-208B',1,[('NPCIJ/UPIV/OC 208B/2025-26','NPCI/UPI/OC 208B/2025-26'),('03" Oct 2024','03rd Oct 2024'),('30" Jun 2025','30th Jun 2025')])
add('2023-Product-Compliance-PCOMP-Q4',1,[('13" April, 2023','13th April, 2023'),('12\'" January 2021','12th January 2021'),('31% May','31st May')])
table='''| Sr No | Product | General Compliance |
|---|---|---|
| 1 | General Compliance | Member organization should be compliant/Certified to ISO27001 standard. Kindly provide the date of compliance letter/certificate in Date Column |
| 2 | General Compliance | Member should have Business Continuity Management (BCM) Policy/Disaster Recovery Policy |
| 3 | General Compliance | Member should have Cyber Security Policy. |
| 4 | General Compliance | Member organization should be compliant/Certified to PCI DSS standard. Kindly provide the date of certificate in Date Column |
| 5 | General Compliance | Member organization should be compliant to RBI SAR (System Audit Report) & Data Localization requirements. Kindly provide the date of Compliance in Date Column |
| 6 | General Compliance | Member organization should be compliant to RBI Csite/Cyber Security framework compliance. Kindly provide the date of Compliance in Date Column. |
| 7 | General Compliance | Member organization as an AUA/KUA (or sub-AUA/sub-KUA) should be compliant to the UIDAI compliance requirement. Kindly provide the date of Compliance in Date Column. |
| 8 | General Compliance | Member organization should be compliant to RBI Oversight framework requirements. Kindly provide the date of Compliance in Date Column. |'''
old=next(p['text'] for p in pages if p['document_id']=='2023-Product-Compliance-PCOMP-Q4' and p['source_page']==3)
start=old.index('Sr Product General Compliance')
add('2023-Product-Compliance-PCOMP-Q4',3,[(old[start:].rstrip(),table)])
doc='2023-UPI-160';old=next(p['text'] for p in pages if p['document_id']==doc)
start=old.index('Dispute /Adjustment Type Dispute /Adjustment Type');end=old.index('Disabling of Interchange fee')
table='''| S. No | Dispute /Adjustment Type | S. No | Dispute /Adjustment Type |
|---|---|---|---|
| 1 | Wrong Credit Chargeback | 7 | Pre Arbitration Acceptance |
| 2 | Wrong Credit Chargeback Re-Presentment | 8 | Deferred Chargeback Acceptance/ Deemed Acceptance |
| 3 | Chargeback | 9 | Deferred Pre Arbitration Acceptance / Deemed Acceptance |
| 4 | Re-presentment | 10 | RET |
| 5 | Fraud Chargeback | 11 | Credit Adjustment |
| 6 | Fraud Chargeback Re-Presentment | | |
'''
add(doc,1,[(old[start:end],table),('28" December, 2022','28th December, 2022'),('10" Mar 2021','10th Mar 2021'),('1" January 2023','1st January 2023'),('1* January 2023','1st January 2023'),('1° January 2023','1st January 2023')])
(HERE/'corrections.json').write_bytes((json.dumps(dict(review='AI visual comparison with PDF images; independent review pending',pages=edits),ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
