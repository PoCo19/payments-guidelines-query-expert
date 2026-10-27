"""Deterministic, source-preserving clause segmentation. No LLM metadata inference."""
import re

CHUNKER_VERSION = "clauses-v1"
HEADINGS = re.compile(r"^(?:key guidelines|guidelines|payee psp|payer psp|remitter bank|beneficiary bank|upi application provider|upi application providers|psp banks?|annexure(?:\s+[A-Z0-9IVX.-]+)?|annex(?:\s+[A-Z0-9IVX.-]+)?)\s*:?$", re.I)
CLAUSE = re.compile(r"^(\d{1,2}[.)]|[a-z][.)])\s+", re.I)


def clause_chunks(pages, limit=220, overlap=35):
    """Page-local verbatim word spans; headings/section identity persist across pages.

    A numbered clause or recognized heading starts a new block. Long blocks use
    overlapping word windows. Adjacent page chunks are linked, never concatenated.
    OCR layout is heuristic: section labels are navigation hints, not legal labels.
    """
    if not 0 <= overlap < limit:
        raise ValueError("Require 0 <= overlap < limit")
    section_no, heading = 0, "Document opening"
    result = []
    for page in sorted(pages, key=lambda p: p["source_page"]):
        words, start, cursor, label, ordinal = [], 0, 0, "", 0
        blocks = []
        for line in page["text"].splitlines():
            line = line.strip()
            row = line.split()
            if not row:
                continue
            is_heading = bool(HEADINGS.fullmatch(line) or re.match(r"^#{1,4}\s+\S", line))
            clause = CLAUSE.match(line)
            if (is_heading or clause) and words and not (clause and " ".join(words).lstrip("# ") == heading):
                blocks.append((start, words, section_no, heading, label))
                words = []
            if is_heading:
                section_no += 1
                heading = line.lstrip("# ")
                label = ""
            if clause:
                label = clause[1]
            if not words:
                start = cursor
            words.extend(row)
            cursor += len(row)
        if words:
            blocks.append((start, words, section_no, heading, label))
        for start, words, section, title, clause_label in blocks:
            offset = 0
            while offset < len(words):
                stop = min(offset + limit, len(words))
                ordinal += 1
                result.append(dict(id=f'{page["document_id"]}:p{page["source_page"]}:v3c{ordinal}',
                    document_id=page["document_id"], page=page["source_page"],
                    text=" ".join(words[offset:stop]), start_word=start+offset, end_word=start+stop,
                    section_id=f'{page["document_id"]}:s{section}', section_heading=title,
                    clause_label=clause_label, chunker_version=CHUNKER_VERSION,
                    segmentation_status="heuristic_not_reviewed"))
                if stop == len(words):
                    break
                offset = stop - overlap
    for i, part in enumerate(result):
        part["previous_chunk_id"] = result[i-1]["id"] if i else ""
        part["next_chunk_id"] = result[i+1]["id"] if i+1 < len(result) else ""
    return result
