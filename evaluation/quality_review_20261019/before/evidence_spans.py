"""Immutable source excerpts: models select identifiers rather than retype text."""
import re
def source_spans(sources, limit=700):
    anchors={};evidence=[]
    for source in sources:
        spans=[];text=source['text'];offset=0
        while offset<len(text):
            end=min(offset+limit,len(text))
            if end<len(text):
                # Keep sentence/row boundaries when possible. Flattened Markdown
                # tables still retain adjacent pipes between their original rows.
                breaks=list(re.finditer(r'\n|(?<=[.!?])\s+(?=[A-Z])|(?<=\|)\s+(?=\|)',text[offset+limit//2:end]))
                boundary=offset+limit//2+breaks[-1].end() if breaks else text.rfind(' ',offset+limit//2,end)
                if boundary>offset:end=boundary
            key=f"{source['citation']}.{len(spans)+1}"
            quote=text[offset:end]
            anchors[key]=dict(citation=source['citation'],quote=quote)
            spans.append(dict(id=key,text=quote));offset=end
        item={k:source.get(k) for k in ('citation','document_id','title','circular_number','issue_date','issuer','document_type','listed_update_date','applicability')}
        item['excerpts']=spans;evidence.append(item)
    return anchors,evidence
