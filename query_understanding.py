"""Conservative reference hints and explicit, configurable clarification policies."""
import json
import re
from pathlib import Path

STOP = set('the a an on in of for to and or with what which when how is are was under does do can must should circular no oc rbi npci directions master guidelines payment payments require requirements'.split())


def terms(text):
    return {w for w in re.findall(r'[a-z][a-z0-9]+', text.lower()) if w not in STOP}


def resolve_by_title(query, candidates):
    """Choose only a distinctive title match; ties stay visible to the user."""
    if len(candidates)<2:
        return candidates
    qt=terms(query)
    scored=sorted(((len(qt & terms(d['subject'])),i,d) for i,d in enumerate(candidates)),reverse=True)
    if scored and scored[0][0]>=2 and scored[0][0]>=scored[1][0]+2:
        return [scored[0][2]]
    return candidates


def clarification(engine, query, series='', document_ids=None, numbers=None):
    if series or document_ids or numbers:
        return None
    from product_scope import ALIASES
    if any(re.search(pattern,query,re.I) for pattern in ALIASES.values()):
        return None
    if re.search(r'\b(?:compare|comparison|across|both|all products|different products)\b',query,re.I):
        return None
    # This is a reviewed interaction vocabulary, not inferred applicability.
    path=Path(__file__).parent/'query_policies.json'
    for policy in json.loads(path.read_text(encoding='utf-8')):
        if re.search(policy['pattern'],query,re.I):
            return dict(kind='product_scope', question=policy['question'],
                        options=policy['products'], reason='This feature name is shared across products. Choose the intended product before looking up its rules.')
    return None
