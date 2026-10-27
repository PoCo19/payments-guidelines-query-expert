"""Verify that the candidate changes only the reviewed page text and keeps identities."""
import hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from app import Engine
from graph_context import EvidenceGraph
HERE=Path(__file__).resolve().parent
def read(path):return json.loads(path.read_text(encoding='utf-8-sig'))
def rows(path):return [json.loads(line) for line in path.open(encoding='utf-8-sig') if line.strip()]
def sha(text):return hashlib.sha256(text.encode('utf-8')).hexdigest()
sample=read(HERE/'sample.json');plan=read(HERE/'corrections.json')
base=Path(sample['baseline']);candidate=ROOT/'data/releases/payments-ocr-audit-20261015'
before={(p['document_id'],p['source_page']):p for p in rows(base/'all_circular_pages.jsonl')}
after={(p['document_id'],p['source_page']):p for p in rows(candidate/'all_circular_pages.jsonl')}
assert before.keys()==after.keys()
changed={key for key in before if before[key]['text']!=after[key]['text']}
assert changed=={(p['document_id'],p['page']) for p in plan['pages']}
assert {d['id'] for d in read(base/'index.json')}=={d['id'] for d in read(candidate/'index.json')}
for key in changed:
    assert after[key]['raw_extracted_text']==before[key]['text']
assert after[('2025-OC-185B',1)]['text']==before[('2025-OC-185B',1)]['text']
config=read(candidate/'candidate_config.json');config['vector_backend']='json'
engine=Engine(config=config);graph=EvidenceGraph(ROOT/'pilot/upi_extended_graph_v3.json',engine)
queries={'2023-UPI-160':'RET Re-presentment Interchange fee',
         '2023-Product-Compliance-PCOMP-Q4':'ISO27001 compliance letter certificate Date Column',
         '2023-UPI-186':'31st January 2024',
         '2024-OC-107A':'31st May 2024',
         '2025-OC-193A':'TRAN ID 35',
         '2025-OC-208B':'August 20 2025'}
hits={doc:[p['document_id'] for p in engine.search(q,method='bm25',document_ids=[doc],k=2)] for doc,q in queries.items()}
assert all(found and set(found)=={doc} for doc,found in hits.items())
result=dict(passed=True,documents=len(engine.docs),pages=len(engine.pages),chunks=len(engine.parts),
    changed_pages=len(changed),changed_documents=len({d for d,p in changed}),
    replacements=sum(len(p['replacements']) for p in plan['pages']),
    unchanged_page_texts=len(before)-len(changed),identity_preserved=True,previous_OC185B_repair_preserved=True,
    graph_anchors_validated=len(graph.nodes),targeted_retrieval=hits,
    caveat='Integrity and retrieval checks, not independent expert review or corpus-wide OCR certification.')
(HERE/'source_validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
