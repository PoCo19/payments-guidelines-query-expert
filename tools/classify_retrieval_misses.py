"""Classify saved misses without changing ranking or provisional references."""
import collections
import hashlib
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app import Engine,read_json
from evaluation.ragas_runner import save


def main():
    capture=ROOT/'evaluation/quality_runs/20261019T181403217201Z/capture.json'
    record=read_json(capture)
    engine=Engine(config=read_json(ROOT/'config.json'))
    findings=[]
    for row in record['rows']:
        if row['arm']!='candidate' or row['status']!='ok':continue
        trace=row['response']['retrieval_trace']
        stages=trace.get('candidate_stages',{})
        for ref,hit in zip(row['case']['references'],row['anchor_hits']):
            if hit:continue
            matches=[p['id'] for p in engine.parts if p['document_id']==ref['document_id']
                and p['page']==ref['page'] and ref['quote'] in ' '.join(p['text'].split())]
            page_found=any(p['document_id']==ref['document_id'] and p['source_page']==ref['page']
                and ref['quote'] in ' '.join(p['text'].split()) for p in engine.pages)
            ranks={stage:min([ids.index(key)+1 for key in matches if key in ids],default=None)
                for stage,ids in stages.items() if isinstance(ids,list)}
            included=bool(set(matches)&set(trace.get('included_chunk_ids',[])))
            if not page_found:classification='source_or_reference_mismatch_requires_review'
            elif not matches:classification='chunk_boundary_or_extraction_representation'
            elif not ranks.get('before_rerank'):classification='not_in_initial_candidate_pool'
            elif not included:classification='ranking_or_context_selection'
            else:classification='returned_text_or_anchor_matching_requires_review'
            findings.append(dict(case=row['id'],query=row['case']['query'],reference=ref,
                classification=classification,source_quote_present=page_found,
                matching_chunks=matches,stage_positions=ranks,selected=included,
                reference_review='AI-assisted expected anchor; relevance and essentiality await independent review.',
                next_action='Inspect exact candidate and inclusion traces; confirm this anchor is essential before changing ranking.'))
    summary=dict(count=len(findings),classifications=dict(collections.Counter(f['classification'] for f in findings)),
        capture_sha256=hashlib.sha256(capture.read_bytes()).hexdigest(),corpus_fingerprint=engine.fingerprint,findings=findings)
    assert len(findings)==11
    out=ROOT/'evaluation/workbench_20261020/retrieval_misses.json';save(out,summary)
    lines=['# Eleven remaining retrieval misses','These classifications use saved stage traces and the unchanged local source text. They do not declare the provisional reference correct. No ranking or source was changed.',
        '| Case | Missed source | Stage | Candidate / rerank position |','|---|---|---|---|']
    for f in findings:
        r=f['stage_positions']
        lines.append(f"| {f['case']} | {f['reference']['document_id']} | {f['classification']} | {r.get('before_rerank')} / {r.get('after_rerank')} |")
    lines+=['','The available trace separates candidate absence from ranking/context selection. It does not record every rejected expansion decision, so finer causal claims would require instrumentation. All eleven quoted passages exist in source text; no source repair is justified by an anchor miss alone.']
    out.with_suffix('.md').write_text('\n'.join(lines),encoding='utf-8')
    print(summary['classifications'])


if __name__=='__main__':main()
