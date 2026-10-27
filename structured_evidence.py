"""Build bounded, verbatim evidence records before question-focused synthesis.

No model-extracted facts are promoted to truth. Table cells retain headers;
ordinary prose stays intact with source ownership. Original evidence is retained.
"""
import hashlib
import json
import re
from scope_guard import tables

SYNTHESIS_GUIDANCE = (
    'The evidence_records are an internal reading aid, not the requested output. '
    'Answer the actual question first in natural language, then explain relevant conditions and differences. '
    'Do not list retrieved chunks or narrate each document unless the question asks for a document-by-document comparison. '
    'Table cells must retain their row category and exact column meaning. Unknown fields remain unknown. '
    'Do not combine amounts, actors, dates or applicability across records into an invented universal rule. '
    'Use the original evidence to check qualifications and cite its source IDs. Context labels are navigation metadata, not quotations. '
    'Use only citation labels from the citation field in the sources array. Never use a document ID, heading or internal record as a citation. '
    'When evidence supports only part of the question, answer that part and identify the specific missing part. '
)


def build_records(question, sources, budget=5000):
    query = set(re.findall(r'[a-z0-9]+', question.lower()))
    candidates = []
    for source in sources:
        if source.get('generation_eligible') is False:
            continue
        text = source['text']
        owner = {k: source.get(k) for k in ('citation', 'document_id', 'page', 'circular_number', 'section_heading')}
        # Parser yields only complete equal-width rows. Cells remain exact source
        # strings, not inferred classifications or legal applicability labels.
        rows = list(tables(text))
        for headers, cells in rows:
            record = dict(owner, kind='table_row', cells=[dict(header=h, value=c) for h,c in zip(headers,cells)],
                          unknowns=['applicability beyond the quoted row', 'effective date unless separately stated'])
            candidates.append((record, ' '.join(cells)))
        # Keep prose boundaries around tables; do not manufacture a flattened row.
        prose = text.split('|', 1)[0] if rows else text
        if prose.strip():
            record = dict(owner, kind='source_passage', quote=prose.strip(),
                          interpretation='unparsed; preserve stated actor, condition, exception and date')
            candidates.append((record, prose))
    candidates.sort(key=lambda r: -len(query & set(re.findall(r'[a-z0-9]+', r[1].lower()))))
    records=[];used=0
    for record, _ in candidates:
        encoded=json.dumps(record,ensure_ascii=False)
        size=len(encoded)
        if used+size>budget or len(records)>=24:continue
        records.append(record);used+=size
    return dict(version=1, purpose='internal_source_reading_aid', records=records,
                omitted_records=len(candidates)-len(records), character_budget=budget,
                source_hashes={s['citation']:hashlib.sha256(s['text'].encode()).hexdigest() for s in sources if s.get('generation_eligible') is not False},
                limitation='Record selection is heuristic; original evidence remains authoritative. Not a complete rule inventory.')
