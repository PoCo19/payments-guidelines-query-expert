"""Read-only triage of the active source snapshot; never repairs or certifies text."""
import collections
import csv
import hashlib
import json
from pathlib import Path
import re
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from intake_quality import inspect_pages


def main():
    config=json.loads((ROOT/'config.json').read_text(encoding='utf-8'))
    data=Path(config['data_dir'])
    docs={d['id']:d for d in json.loads((data/'index.json').read_text(encoding='utf-8'))}
    pages=[json.loads(line) for line in (data/'all_circular_pages.jsonl').read_text(encoding='utf-8').split('\n') if line.strip()]
    lookup={(p['document_id'],p['source_page']):p for p in pages}
    graph_path=ROOT/config['evidence_graph_path'];graph=json.loads(graph_path.read_text(encoding='utf-8'))
    stale=[];graph_pages=set()
    for node in graph['nodes']:
        key=(node['document_id'],node['page']);graph_pages.add(key);page=lookup.get(key)
        if not page or hashlib.sha256(page['text'].encode()).hexdigest()!=node['page_sha256'] or ' '.join(node['quote'].split()) not in ' '.join(page['text'].split()):
            stale.append(node['id'])
    rows=[]
    for p in pages:
        d=docs[p['document_id']];number=p['source_page'];text=p['text']
        review=inspect_pages(d['id'],[(number,text)])[0]
        codes={f['code'] for f in review['findings']}
        if re.search(r'\b(?:response\s*codes?|purpose\s*codes?|MCC)\b',text,re.I):codes.add('operational_codes')
        if (d['id'],number) in graph_pages:codes.add('graph_anchor_page')
        if not codes:continue
        if not d.get('issue_date'):codes.add('unknown_issue_date')
        weights={'replacement_characters':8,'empty_page':8,'table_header_mismatch':7,'table_row_mismatch':7,
                 'monetary_values':4,'table_layout':3,'qualifications_or_dates':2,'unknown_issue_date':2,
                 'operational_codes':3,'thin_page':3,'graph_anchor_page':2}
        rows.append(dict(document_id=d['id'],page=number,priority_score=sum(weights.get(c,1) for c in codes),
            signals='; '.join(sorted(codes)),title=d.get('subject') or d.get('listing_title',''),
            original_url=d.get('source_pdf') or '',markdown_file=d.get('markdown_file') or '',
            text_sha256=review['text_sha256'],recorded_extraction_status=p.get('review_status',''),
            reviewer='',review_result='',original_evidence='',correction_record=''))
    rows.sort(key=lambda r:(-r['priority_score'],r['document_id'],r['page']))
    out=ROOT/'evaluation/readiness_review_20261018';out.mkdir(parents=True,exist_ok=True)
    with (out/'source_review_queue.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    gaps=[dict(document_id=d['id'],availability=d['availability'],title=d.get('subject') or d.get('listing_title',''),source_url=d.get('source_pdf') or '') for d in docs.values() if d['availability']!='converted']
    metadata=[dict(document_id=d['id'],title=d.get('subject') or d.get('listing_title',''),source_url=d.get('source_pdf') or '',
                   issue='Unknown issue date; verify original header rather than listing date.',reviewer='',verified_date='',evidence='')
              for d in docs.values() if d['availability']=='converted' and not d.get('issue_date')]
    if metadata:
        with (out/'metadata_review_queue.csv').open('w',encoding='utf-8-sig',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=list(metadata[0]));writer.writeheader();writer.writerows(metadata)
    (out/'unavailable_documents.json').write_text(json.dumps(gaps,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    result=dict(pages_inspected=len(pages),pages_queued=len(rows),documents_queued=len({r['document_id'] for r in rows}),
        unavailable_documents=len(gaps),unknown_issue_date_documents=len(metadata),graph_anchors_checked=len(graph['nodes']),stale_graph_anchors=stale,
        graph_relationship_status=dict(collections.Counter(e['review_status'] for e in graph['edges'])),
        signals=dict(collections.Counter(c for r in rows for c in r['signals'].split('; '))),
        fingerprints={name:hashlib.sha256((data/name).read_bytes()).hexdigest() for name in ('index.json','all_circular_pages.jsonl')},
        graph_sha256=hashlib.sha256(graph_path.read_bytes()).hexdigest(),
        limitation='Priority signals are not confirmed errors. No source text, metadata or vectors modified. Reviewer fields intentionally blank. Original URL availability has not been checked live.')
    (out/'source_review_summary.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
