"""Experimental contextual BM25; original excerpts/vectors remain untouched."""

def lexical_text(part, enabled=False):
    original=(part['title']+' ')*2+part['text']
    if not enabled:
        return original
    # Metadata only: no synthetic rule summaries or inferred effective dates.
    fields=('issuer','document_type','series','circular_number','section_heading','clause_label')
    context=' '.join(str(part.get(k) or '') for k in fields)
    return context+' '+original
