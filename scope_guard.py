"""Conservative checks for explicit monetary Markdown tables, independent of issuer.

This catches category/column leakage, not all semantic entailment. Unsupported
table shapes remain the model checker's responsibility; no legal precedence is inferred.
"""
import re
from decimal import Decimal

AMOUNT=re.compile(r'(?:₹|\bRs\.?|\bINR)\s*(\d[\d,]*(?:\.\d+)?)\s*(lakh|lac|crore|million|billion)?|\b(\d[\d,]*(?:\.\d+)?)\s*(lakh|lac|crore|million|billion)\b',re.I)

def monetary_values(text):
    scales={'':1,'lakh':100000,'lac':100000,'crore':10000000,'million':1000000,'billion':1000000000}
    return {Decimal((m.group(1) or m.group(3)).replace(',',''))*scales[(m.group(2) or m.group(4) or '').lower()]
            for m in AMOUNT.finditer(text)}

def monetary_support_issue(claim,sources):
    """Explicit currency/unit expressions cannot borrow digits from boilerplate.

    Unitless table cells still require semantic/table review; this guard only
    establishes absence when cited text contains explicit monetary expressions.
    """
    expected=monetary_values(claim)
    available=monetary_values(' '.join(s['text'] for s in sources))
    if available and expected-available:
        return 'A monetary amount and its unit are absent from the cited evidence; unrelated digits are not support.'
    return None

def scope_acronyms(text):
    """Plural wording must not evade the same attribution checks as singular."""
    return set(re.findall(r'\b([A-Z][A-Z0-9]{1,})(?:s)?\b',text))

def scope_term_present(term,text,related_terms=()):
    """Literal scope hint, allowing case-boundary joins in imported OCR text.

    This only avoids a deterministic rejection; the semantic support check still
    decides whether the passage establishes the claim. Never repair source text.
    """
    if re.search(r'\b'+re.escape(term)+r'\b',text,re.I):return True
    # OCR may join words as UPIbasedASBAIPO. Do not match RDS inside CARDS or
    # ordinary lower-case words; retain literal capitalisation and a start edge.
    if len(term)>=3 and re.search(r'(?:\b|(?<=[a-z0-9]))'+re.escape(term)+r'(?=[A-Za-z0-9]|\b)',text):return True
    # Two separately named acronyms can also be joined, e.g. ASBA + IPO.
    # Require the other acronym to occur in the claim, rather than accepting
    # every uppercase substring (which would confuse RDS with CARDS).
    return any(len(other)>=3 and other!=term and
               (scope_term_present(other+term,text) or scope_term_present(term+other,text))
               for other in related_terms)

def attribution_scope_issue(claim,sources):
    """Reject borrowing an explicit acronym scope from an unnamed second circular.

    This is deliberately narrow: it neither interprets all prose nor guesses
    source authority. A comparison naming both circulars still gets semantic review.
    """
    # Attribute each sentence separately: naming the right circular later must
    # not legitimise a wrong attribution in an earlier sentence.
    segments=re.split(r';\s*|(?<=[.!?])\s+(?=[A-Z])',claim)
    if len(segments)>1:
        return next((issue for segment in segments if (issue:=attribution_scope_issue(segment,sources))),None)
    named=[];scope_text=claim
    for source in sources:
        number=str(source.get('circular_number') or '').strip()
        reference=r'\b(?:OC\s*(?:no\.?\s*)?[-–:]?\s*|circular\s+(?:no\.?\s*)?)'+re.escape(number)+r'\b'
        if number and re.search(reference,claim,re.I):
            named.append(source)
            # A compact reference (OC185B) is an identifier, not a product scope.
            # Remove only references matched to cited metadata; continue checking
            # the original claim's amounts and every other acronym normally.
            scope_text=re.sub(reference,' ',scope_text,flags=re.I)
    if not named:return None
    named_text=' '.join(' '.join(str(s.get(k) or '') for k in ('text','title','series','issuer')) for s in named)
    # A monetary statement attributed to one named circular must not borrow its
    # amount from another citation. Sentence splitting above keeps ownership local.
    if len({s.get('document_id',s.get('circular_number')) for s in named})==1:
        missing=amounts(claim)-amounts(named_text)
        if missing and not re.search(r"\b(?:does not|doesn't|cannot|not established|not specified)\b",claim,re.I):
            return 'A monetary amount is absent from the circular explicitly named in this statement. Do not borrow amounts from another cited source.'
    identifiers={str(s.get('circular_number') or '').upper() for s in named}
    terms=scope_acronyms(scope_text)-{'OC','INR','RS','NA','NO','FY'}-identifiers
    for acronym in terms:
        # Explicitly saying a general table does NOT establish a specific rule
        # must not force that specific scope to appear in the table itself.
        if re.search(r"\b(?:does not|doesn't|cannot|can not|not)\b[^.;]{0,80}\b"+re.escape(acronym)+r's?\b',claim,re.I):continue
        if not scope_term_present(acronym,named_text,terms):
            return 'The specific scope ('+acronym+') is not established by the circular explicitly named in this claim. Attribute this rule to a source that actually states it.'
    return None

def amounts(text):
    return {(m.group(1) or m.group(3)).replace(',','')+' '+(m.group(2) or m.group(4) or '').lower().replace('lac','lakh') for m in AMOUNT.finditer(text)}

def beyond_ceiling_issue(claim,sources):
    """A within-limit exemption is not evidence for a rule above that limit."""
    extension=r'\b(?:above|beyond) which\b|\bbeyond (?:the|this|that) (?:limit|ceiling)\b'
    if not re.search(extension,claim,re.I):return None
    text=' '.join(s['text'] for s in sources)
    bounded=re.search(r'\bcapped at\b|\bup to\b|\bwithin (?:the|this|that|aforesaid) ceiling\b',text,re.I)
    explicit=re.search(r'\b(?:above|beyond|exceeding)\s+(?:(?:the|this|that)\s+(?:limit|ceiling)|which|(?:Rs\.?|INR|₹)?\s*\d)',text,re.I)
    if bounded and not explicit:
        return 'The sources describe behavior within a ceiling; they do not establish the claimed rule above that ceiling.'
    return None


def notification_phase_issue(claim,sources):
    """Do not transfer a positive notification rule to an absent event phase."""
    if not re.search(r'\bnotif\w*|\bnotice\b|\bmessage\b|\balert\b',claim,re.I):return None
    # Limitations about what a passage does not establish are not positive rules.
    if re.search(r"\b(?:does not|doesn't|cannot)\s+(?:establish|mean|imply|support|demonstrate|infer|conclude)\b|\b(?:not established|not specified)\b",claim,re.I):return None
    from evidence_focus import phases
    wanted=phases(claim)
    present=phases(' '.join(s['text'] for s in sources))
    if wanted and present and wanted-present:
        return 'The cited notification rule concerns a different event phase. A pre-transaction exemption does not establish a post-transaction exemption, or vice versa.'
    return None


def collective_numbers(claim):
    if not re.search(r'\b(?:consistently|each|all|both)\b',claim,re.I):return set()
    if re.search(r'\b(?:respectively|different|whereas)\b',claim,re.I):return set()
    named={x.upper() for x in re.findall(r'\b(?:OC|circular)\s*(?:no\.?\s*)?[-–:]?\s*(\d+[A-Z]*)\b',claim,re.I)}
    return named if len(named)>1 else set()


def collective_attribution_issue(claim,sources):
    """A claim about every named circular needs evidence from every named circular."""
    named=collective_numbers(claim)
    if not named:return None
    represented={str(s.get('circular_number') or '').upper() for s in sources}
    if named-represented:
        return 'The collective statement names circulars without their own supporting evidence. Attribute each rule separately rather than treating the whole series as identical.'
    # Narrow literal category gate for universal claims. A matching amount in
    # another category cannot support "all these circulars". Unmatched synonyms
    # remain uncertain, rather than silently importing a later document's rule.
    categories=re.findall(r'\bfor\s+(?:the\s+)?([a-z][a-z -]{0,60}?)\s+(?:payments?|transactions?|categories)\b',claim,re.I)
    ignored={'the','same','specific','certain','all','each','both','per','single'}
    def terms(value):return {w.rstrip('s') for w in re.findall(r'[a-z]{3,}',value.lower())}-ignored
    for category in categories:
        wanted=terms(category)
        if not wanted:continue
        for number in named:
            own=' '.join(s['text'] for s in sources if str(s.get('circular_number') or '').upper()==number)
            if not wanted<=terms(own):
                return 'The collective category ('+category+') is not explicitly established in each named circular. Separate the rules by source; a shared amount does not establish shared scope.'
    return None

def tables(text):
    """Parse complete Markdown tables even after ingestion collapses whitespace."""
    if '|' not in text:return
    fragments=re.split(r'\|\s*\|',text[text.index('|'):])
    rows=[];headers=None
    for fragment in fragments:
        cells=[c.strip() for c in fragment.strip().strip('|').split('|')]
        if len(cells)>1 and all(re.fullmatch(r':?-{3,}:?',c) for c in cells):
            headers=rows[-1] if rows and len(rows[-1])==len(cells) else None
        elif headers and len(cells)==len(headers):
            yield headers,cells
        rows.append(cells)

def table_scope_issue(claim,sources,_split_measures=True):
    wanted=amounts(claim)
    if not wanted:return None
    parsed=[];prose_amounts=set()
    for source in sources:
        # Prose with an explicit amount can support a statement separately from a table.
        prose=re.sub(r'\|[^\n]*', '', source['text']) if '\n' in source['text'] else source['text'].split('|',1)[0]
        prose_amounts |= amounts(prose)
        parsed.extend(tables(source['text']))
    if not parsed:return None
    words=set(re.findall(r'[a-z]{3,}',claim.lower()))
    stop={'the','and','for','with','including','payments','payment','category','categories','general'}
    # A sentence can state two different measures for one category. Check each
    # amount-bearing clause against its own column, rather than treating both
    # amounts as cumulative merely because "24 hours" appears later.
    categories=set()
    for headers,cells in parsed:
        index=next((i for i,h in enumerate(headers) if re.fullmatch(r'categories|category|product|use case|transaction type',h,re.I)),None)
        if index is not None:
            label=set(re.findall(r'[a-z]{3,}',cells[index].lower()))-stop
            if label and label<=words:categories.add(cells[index])
    if _split_measures and len(categories)==1:
        cuts=[m for m in re.finditer(r'\b(?:while|whereas|and|but)\b|;',claim,re.I)
              if amounts(claim[:m.start()]) and amounts(claim[m.end():])]
        if cuts:
            start=0;clauses=[]
            for cut in cuts:
                clauses.append(claim[start:cut.start()]);start=cut.end()
            clauses.append(claim[start:])
            if sum(bool(amounts(c)) for c in clauses)>1:
                category=next(iter(categories))
                return next((issue for clause in clauses if amounts(clause)
                             and (issue:=table_scope_issue(clause+' ('+category+')',sources,False))),None)
    cumulative=bool(re.search(r'cumulative|24\s*(?:hours?|hrs?)|daily',claim,re.I))
    single=bool(re.search(r'per[- ](?:transaction|payment|mandate)|single (?:transaction|payment|mandate)',claim,re.I))
    for amount in wanted-prose_amounts:
        candidates=[]
        for headers,cells in parsed:
            label_index=next((i for i,h in enumerate(headers) if re.fullmatch(r'categories|category|product|use case|transaction type',h,re.I)),None)
            if label_index is None:continue
            for i,cell in enumerate(cells):
                if amount not in amounts(cell):continue
                label_words=set(re.findall(r'[a-z]{3,}',cells[label_index].lower()))-stop
                label_matches=bool(label_words & words)
                column_matches=True
                if cumulative != single:
                    is_cumulative=bool(re.search(r'cumulative|24\s*(?:hours?|hrs?)|daily',headers[i],re.I))
                    column_matches=is_cumulative if cumulative else not is_cumulative
                candidates.append(label_matches and column_matches)
        if candidates and not any(candidates):
            return 'The table amount is not tied to a matching category and limit type in the claim. Cite the correct row and retain its scope.'
    return None
