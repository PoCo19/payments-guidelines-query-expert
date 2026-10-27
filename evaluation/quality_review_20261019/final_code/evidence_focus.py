"""Bounded recovery of literal table categories and requested event phases.

These are retrieval hints, not source interpretations or authority decisions.
No publisher, circular ID, amount or graph topic is hardcoded here.
"""
import re
from scope_guard import tables


def terms(text):
    return {w[:-1] if w.endswith('s') and len(w)>4 else w
            for w in re.findall(r'[a-z0-9]+', text.lower())}


def table_matches(query, candidates, limit=2):
    """Protect full matching category rows, including their original headers."""
    q = terms(query)
    if not q & {'limit','ceiling','maximum','minimum','amount','cap','threshold'}:
        return []
    ignored = {'payment','transaction','category','including','and','for','the','use','case'}
    matches = []
    for rank, part in enumerate(candidates):
        for headers, cells in tables(part['text']):
            column = next((i for i,h in enumerate(headers)
                           if re.fullmatch(r'categories|category|product|use case|transaction type', h, re.I)), None)
            if column is None:
                continue
            label = terms(cells[column]) - ignored
            # Full multiword label match; sharing an MCC or generic word is insufficient.
            if len(label) >= 2 and label <= q:
                matches.append((rank, part)); break
    return [p for _,p in sorted(matches, key=lambda x:(x[0], x[1]['id']))[:limit]]


def phases(text):
    result = set()
    if re.search(r'\bpre[- ](?:transaction|debit)|\b(?:before|prior to|advance)\b[^.;?]{0,35}\b(?:debit|charge|transaction)\b', text, re.I):
        result.add('before')
    if re.search(r'\bpost[- ](?:transaction|debit)|\bafter\b[^.;?]{0,25}\b(?:debit|charge|transaction)\b', text, re.I):
        result.add('after')
    return result


def phase_matches(query, candidates, limit=2):
    """Protect notification clauses demoted by ranking on a narrower topic.

    A candidate must have a notification-phase heading and share a distinctive
    query term in its body. Its neighbouring phase is recovered separately;
    neither a publisher name nor the word 'notification' alone selects a rule.
    """
    if not phases(query) or not re.search(r'\b(?:notif\w*|notices?|messages?|alerts?)\b',query,re.I):
        return []
    generic=set(('the a an on in of to for and or by from with under our it is are was '
                 'be been can could should would must shall may do doe did not no '
                 'what which when how why whether because if than that this these '
                 'before after prior advance pre post transaction debit charge '
                 'notification notice message alert issuer customer user rule '
                 'guideline requirement required exempt exemption omit skip send '
                 'payment bank rbi npci').split())
    focus=terms(query)-generic
    if not focus:return []
    found=[]
    for part in candidates:
        heading=part.get('section_heading','')
        if (phases(heading) and re.search(r'\bnotif\w*|\bnotice\b|\balert\b',heading,re.I)
                and focus & terms(part['text'])):
            found.append(part)
            if len(found)>=limit:break
    return found


def phase_companions(engine, query, seeds, limit=2):
    """Find an adjacent named phase of the same action in an already found document."""
    wanted = phases(query)
    if not wanted or not re.search(r'\b(?:notif\w*|notices?|messages?|alerts?)\b', query, re.I):
        return []
    seen = {p['id'] for p in seeds}; found = []
    for seed in seeds:
        if not re.search(r'\bnotif\w*|\bnotice\b|\balert\b', seed['text'], re.I):
            continue
        for key in ('next_chunk_id','previous_chunk_id'):
            part = engine.parts_by_id.get(seed.get(key))
            if not part or part['document_id'] != seed['document_id'] or part['id'] in seen:
                continue
            heading = part.get('section_heading','')
            if phases(heading) & wanted and re.search(r'\bnotif\w*|\bnotice\b|\balert\b', heading, re.I):
                found.append(part); seen.add(part['id'])
                if len(found) == limit:
                    return found
    return found
