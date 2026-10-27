"""Exclude known-corrupt source passages from model use without rewriting the corpus."""
import hashlib
import json
from pathlib import Path

FLAGS=Path(__file__).with_name('source_quality_flags.json')


def gate_sources(engine,sources,flags_path=FLAGS):
    flags=json.loads(Path(flags_path).read_text(encoding='utf-8'))
    if flags.get('schema_version')!=1:raise ValueError('Unsupported source-quality flag schema')
    marked=[];usable=[];warnings=[]
    for source in sources:
        issues=[]
        for flag in flags['flags']:
            if source.get('document_id')!=flag['document_id'] or source.get('page')!=flag['page']:continue
            page=getattr(engine,'page_lookup',{}).get((flag['document_id'],flag['page']))
            current=hashlib.sha256(page['text'].encode('utf-8')).hexdigest() if page else None
            # A source repair is released only for its exact reviewed text hash.
            # Historical/unknown versions still retain the original protection.
            if current and current==flag.get('repaired_page_sha256'):
                continue
            stale=current!=flag['page_sha256']
            if stale or flag['unsafe_quote'] in ' '.join(source['text'].split()):
                issues.append(dict(id=flag['id'],reason=flag['reason'],review_status=flag['review_status'],flag_stale=stale))
        if issues:
            source=dict(source,generation_eligible=False,source_quality_issues=issues)
            warnings.append(source['citation']+': known source-quality issue; excluded from model drafting and support checks. Inspect the original PDF. '+('The source flag needs re-review after a text change.' if any(i['flag_stale'] for i in issues) else ''))
        else:
            usable.append(source)
        marked.append(source)
    allowed={s['citation'] for s in usable}
    usable=[dict(s,citation_companions=[c for c in s['citation_companions'] if c in allowed]) if s.get('citation_companions') else s for s in usable]
    return marked,usable,warnings
