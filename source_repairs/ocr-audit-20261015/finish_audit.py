"""Save page-image evidence and final review status; no source-content inference."""
import hashlib,json,shutil
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
def sha(data):return hashlib.sha256(data).hexdigest()
sample=json.loads((HERE/'sample.json').read_text(encoding='utf-8'))
notes={
'2024-OC-107A':'Corrected three OCR date suffixes. Printed RRN strings, 100 million and approximately 1000 Billion retained.',
'2023-UPI-186':'Corrected header reference/date and January deadline. Historical Rs.500 threshold, initiation mode 06, NFC Type 2 and liability wording retained.',
'2025-OC-193A':'Corrected dates and attached OC193 reference. Printed 35 digits and attached 35 characters (alphanumeric) retained as written; no harmonisation. October 1, 2024 and remitter/beneficiary conditions unchanged.',
'2025-OC-208B':'Corrected circular-reference OCR and referenced date suffixes. August 20, 2025 go-live unchanged.',
'2023-Product-Compliance-PCOMP-Q4':'Corrected page-1 dates and transcribed page-3 table with all eight rows. Recovered ISO27001 certificate-date instruction and RBI Oversight wording. Page-2 action numbers 3 and 4 are printed that way and remain unchanged.',
'2023-UPI-160':'Restored complete 11-entry two-column dispute table, including Re-presentment and RET; repaired date suffixes. No reversal before January 1, 2023 and zero report values retained.'}
(HERE/'images').mkdir(exist_ok=True)
for s in sample['sample']:
    s.update(review_status='AI_visual_review_complete_independent_review_pending',review_notes=notes[s['document_id']],page_images=[])
    for n in range(1,s['pages']+1):
        name=f"{s['document_id']}-{n}.png";src=ROOT/'tmp/ocr-audit-20261015'/name
        shutil.copy2(src,HERE/'images'/name)
        s['page_images'].append(dict(page=n,path='images/'+name,sha256=sha(src.read_bytes())))
(HERE/'sample.json').write_bytes((json.dumps(sample,indent=2,ensure_ascii=False)+'\n').encode('utf-8'))
# Restore Markdown table block boundaries in the two reflowed reading copies.
# This only changes surrounding whitespace, not the indexed candidate text.
record=json.loads((HERE/'repair_record.json').read_text(encoding='utf-8'))
for entry in record['legacy_files']:
    path=Path(entry['path']);raw=path.read_bytes()
    if path.name not in ('2023-04-13_2023-Product-Compliance-PCOMP-Q4.md','2022-12-28_2023-UPI-160.md'):continue
    if sha(raw)!=entry['after_sha256']:raise ValueError('Reading Markdown changed since repair')
    text=raw.decode('utf-8')
    for marker in ('| Sr No | Product |','| S. No | Dispute /Adjustment Type |'):
        if marker in text:text=text.replace(marker,'\n\n'+marker,1)
    updated=text.encode('utf-8');path.write_bytes(updated)
    entry.update(after_sha256=sha(updated),formatting_note='Blank lines added before reconstructed Markdown table; words and values unchanged.')
(HERE/'repair_record.json').write_bytes((json.dumps(record,indent=2,ensure_ascii=False)+'\n').encode('utf-8'))
