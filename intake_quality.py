"""Conservative extraction triage. Flags are not OCR corrections or certification."""
import hashlib
import re


def inspect_pages(document_id, pages):
    results = []
    for number, text in pages:
        findings = []
        def flag(code, severity, detail):
            findings.append(dict(code=code, severity=severity, detail=detail))
        if not text.strip():
            flag('empty_page', 'review', 'No extracted text; compare with the original page.')
        elif len(text.split()) < 15:
            flag('thin_page', 'review', 'Very little text; check whether content was lost.')
        if '\ufffd' in text:
            flag('replacement_characters', 'blocking', 'Unicode replacement characters indicate lost character information.')
        rows = [line.strip() for line in text.splitlines() if line.strip()]
        width = None
        for i, line in enumerate(rows):
            if '|' not in line:
                width = None
                continue
            cells = [c.strip() for c in line.strip('|').split('|')]
            if len(cells) > 1 and all(re.fullmatch(r':?-{3,}:?', c) for c in cells):
                width = len(cells)
                previous = rows[i-1] if i else ''
                if len(previous.strip('|').split('|')) != width:
                    flag('table_header_mismatch', 'blocking', 'Table header and separator have different column counts.')
            elif width and len(cells) != width:
                flag('table_row_mismatch', 'blocking', 'A table row has a different number of cells from its header.')
        if re.search(r'(?:₹|\bINR\b|\bRs\.?|\blakhs?\b|\bcrores?\b)', text, re.I):
            flag('monetary_values', 'review', 'Verify amounts, units and table categories against the original.')
        if re.search(r'\b(?:effective|deadline|on or before|supersede|amend|annexure)\b', text, re.I):
            flag('qualifications_or_dates', 'review', 'Check dates, amendment scope, annexures and exceptions.')
        if '|' in text:
            flag('table_layout', 'review', 'Compare row ownership, merged cells and footnotes with the original page.')
        findings = list({f['code']: f for f in findings}.values())
        results.append(dict(document_id=document_id, page=number,
                            text_sha256=hashlib.sha256(text.encode()).hexdigest(), findings=findings))
    return results


def reviewed_blockers(pages, reviews):
    """An operator acknowledgement binds to exact page text; it never edits text."""
    if not isinstance(reviews, list):
        raise ValueError('quality_reviews must be a list')
    by_page = {p['page']: p for p in pages}
    accepted = set()
    for review in reviews:
        if not isinstance(review, dict) or type(review.get('page')) is not int:
            raise ValueError('Quality review requires a page number')
        page = by_page.get(review['page'])
        if not page or review.get('text_sha256') != page['text_sha256']:
            raise ValueError('Quality review page hash is stale or missing')
        if any(not isinstance(review.get(k), str) or not review[k].strip() for k in ('reviewer', 'reason')):
            raise ValueError('Quality review requires reviewer and reason')
        accepted.add(review['page'])
    return [p['page'] for p in pages if any(f['severity']=='blocking' for f in p['findings']) and p['page'] not in accepted]
