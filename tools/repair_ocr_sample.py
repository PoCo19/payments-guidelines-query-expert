"""Replay the 2026-10-15 PDF-checked edits into a new immutable source release.

Only explicit replacements are permitted; PDF and page hashes protect replay.
Historical releases/raw OCR remain intact. Build and activate through document_pipeline.
"""
import json
import re
import shutil
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.document_pipeline import read,write,sha,stamp,input_hashes,verify_sources,release_path

AUDIT=ROOT/'source_repairs/ocr-audit-20261015'
RELEASE='payments-ocr-audit-20261015'


def apply_edits(text, edits, allow_reflow=False):
    for edit in edits:
        if allow_reflow and text.count(edit['before'])==0:
            pattern=r'\s+'.join(re.escape(word) for word in edit['before'].split())
            matches=list(re.finditer(pattern,text))
            if len(matches)!=1:raise ValueError('Reflowed Markdown anchor is absent or ambiguous')
            match=matches[0]
            replacement=edit['after']
            if replacement.startswith('|'):replacement='\n\n'+replacement.rstrip()+'\n\n'
            text=text[:match.start()]+replacement+text[match.end():]
            continue
        if text.count(edit['before']) != 1:
            raise ValueError('Correction anchor is absent or ambiguous: '+repr(edit['before'][:80]))
        text=text.replace(edit['before'],edit['after'],1)
    return text


def main():
    config_path=ROOT/'config.json';config=read(config_path);base=Path(config['data_dir'])
    plan=read(AUDIT/'corrections.json');sample=read(AUDIT/'sample.json')
    dest=release_path(RELEASE)
    if dest.exists():raise ValueError('Release exists; resume build without rewriting it.')
    if str(base)!=sample['baseline']:raise ValueError('Baseline changed; re-review before replay.')
    verify_sources(base)
    docs=read(base/'index.json')
    pages=[json.loads(line) for line in (base/'all_circular_pages.jsonl').open(encoding='utf-8-sig') if line.strip()]
    records=[];legacy_updates=[];markdown_outputs={}
    for sampled in sample['sample']:
        if sha(Path(sampled['pdf']).read_bytes())!=sampled['pdf_sha256']:raise ValueError('PDF changed')
        doc=next(d for d in docs if d['id']==sampled['document_id'])
        edits=[e for e in plan['pages'] if e['document_id']==doc['id']]
        legacy=Path(config['source_pack'])/sampled['markdown']
        legacy_bytes=legacy.read_bytes();legacy_text=legacy_bytes.decode('utf-8-sig').replace('\r\n','\n')
        for edit in edits:
            page=next(p for p in pages if p['document_id']==doc['id'] and p['source_page']==edit['page'])
            if sha(page['text'].encode('utf-8'))!=edit['before_page_sha256']:raise ValueError('Page changed')
            old=page['text'];fixed=apply_edits(old,edit['replacements'])
            legacy_text=apply_edits(legacy_text,edit['replacements'],allow_reflow=True)
            record=dict(document_id=doc['id'],page=edit['page'],pdf_sha256=sampled['pdf_sha256'],
                before_page_sha256=edit['before_page_sha256'],after_page_sha256=sha(fixed.encode('utf-8')),
                replacements=edit['replacements'],review='AI visual PDF comparison; independent review pending')
            page.update(text=fixed,raw_extracted_text=page.get('raw_extracted_text',old),
                review_status='targeted_pdf_checked_transcription',source_repair=record)
            records.append(record)
        selected=sorted((p for p in pages if p['document_id']==doc['id']),key=lambda p:p['source_page'])
        md='\n\n'.join(f"<!-- Page {p['source_page']} -->\n\n{p['text'].strip()}" for p in selected)+'\n'
        relative='corrections/'+doc['id']+'_20261015.md'
        markdown_outputs[relative]=md.encode('utf-8')
        doc.update(markdown_file='sources/'+relative,markdown_sha256=sha(md.encode('utf-8')),
                   source_repair=dict(audit='ocr-audit-20261015',pages=[e['page'] for e in edits]))
        for page in selected:
            page.update(source_markdown=doc['markdown_file'],markdown_sha256=doc['markdown_sha256'])
        legacy_updates.append((legacy,legacy_bytes,legacy_text.encode('utf-8')))
    # All assertions run before any mutation of source files.
    dest.mkdir(parents=True);shutil.copytree(base/'sources',dest/'sources')
    for name in ('review_annotations.json','feature_rules.json'):shutil.copy2(base/name,dest/name)
    manifest=read(base/'source_manifest.json')
    for relative,contents in markdown_outputs.items():
        (dest/'sources'/relative).parent.mkdir(parents=True,exist_ok=True)
        (dest/'sources'/relative).write_bytes(contents);manifest['hashes'][relative]=sha(contents)
        (AUDIT/'corrected').mkdir(exist_ok=True)
        (AUDIT/'corrected'/Path(relative).name).write_bytes(contents)
    write(dest/'source_manifest.json',manifest);write(dest/'index.json',docs)
    (dest/'all_circular_pages.jsonl').write_bytes(''.join(json.dumps(p,ensure_ascii=False)+'\n' for p in pages).encode('utf-8'))
    corpus=read(base/'corpus.json');corpus.update(release=RELEASE,baseline=str(base),status='candidate',source_repair_audit='ocr-audit-20261015')
    write(dest/'corpus.json',corpus)
    write(dest/'candidate_config.json',dict(config,data_dir=str(dest)));write(dest/'previous_config.json',config)
    write(dest/'intake_state.json',dict(status='prepared',created_at=stamp(),active_config=str(config_path),
        previous_config_sha256=sha(config_path.read_bytes()),baseline=str(base),baseline_inputs=input_hashes(base),
        candidate_inputs=input_hashes(dest),candidate_config_sha256=sha((dest/'candidate_config.json').read_bytes()),
        previous_config_copy_sha256=sha((dest/'previous_config.json').read_bytes()),
        actions=[dict(id=s['document_id'],action='transcription_corrected',pages=s['pages']) for s in sample['sample']]))
    (AUDIT/'original_markdown').mkdir(exist_ok=True)
    for legacy,old,new in legacy_updates:
        (AUDIT/'original_markdown'/legacy.name).write_bytes(old)
        # A failure here leaves the immutable candidate available to inspect/recover.
        legacy.write_bytes(new)
    write(AUDIT/'repair_record.json',dict(created_at=stamp(),release=RELEASE,baseline=str(base),pages=records,
        legacy_files=[dict(path=str(p),before_sha256=sha(old),after_sha256=sha(new)) for p,old,new in legacy_updates]))
    print(dest)


if __name__=='__main__':main()
