"""Prepare a versioned, hash-checked OC185B transcription repair, preserving identity.

This is an extraction correction, not a new circular or a legal amendment.
Build/activate the resulting candidate with document_pipeline.py.
"""
import json
import shutil
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.document_pipeline import read,write,sha,stamp,input_hashes,verify_sources,release_path

DOC='2025-OC-185B'
OLD='Tax Payments to 25 lakh.'
NEW='Tax Payments to ₹5 lakh.'
EXPECTED_PAGE='5c2c1e1a1933359c98f58a9b8cdc0d83efa46bad44c319c28dd4453d0ddecc7a'
EXPECTED_PDF='d44d26aeaa594a9693035f2f7054b6a4bb962c3ced94e9523e3c5ac55f8bd127'
RELEASE='payments-oc185b-repair-20261014'


def corrected_page(page):
    if sha(page['text'].encode('utf-8'))!=EXPECTED_PAGE or page['text'].count(OLD)!=1:
        raise ValueError('Source page differs from the visually checked version; re-review required.')
    result=dict(page)
    result['raw_extracted_text']=page['text']
    result['text']=page['text'].replace(OLD,NEW,1)
    result['review_status']='targeted_currency_correction_ai_visual_check'
    result['source_repair']={'id':'oc185b-currency-20261014','before':OLD,'after':NEW,
        'pdf_sha256':EXPECTED_PDF,'review_status':'AI_visual_check_independent_review_pending',
        'scope':'Currency amount only; the rest of this page is not certified word for word.'}
    return result


def main():
    config_path=ROOT/'config.json';config=read(config_path);base=Path(config['data_dir'])
    dest=release_path(RELEASE)
    if dest.exists():raise ValueError('Release already exists; resume build rather than rewriting it.')
    verify_sources(base)
    docs=read(base/'index.json')
    pages=[json.loads(l) for l in (base/'all_circular_pages.jsonl').open(encoding='utf-8-sig') if l.strip()]
    doc=next(d for d in docs if d['id']==DOC)
    pdf=Path(config['source_pack'])/doc['local_pdf']
    if sha(pdf.read_bytes())!=EXPECTED_PDF:raise ValueError('Original PDF changed; re-review required.')
    old_page=next(p for p in pages if p['document_id']==DOC and p['source_page']==1)
    fixed=corrected_page(old_page)
    pages=[fixed if p is old_page else p for p in pages]
    target_pages=sorted((p for p in pages if p['document_id']==DOC),key=lambda p:p['source_page'])
    markdown='\n\n'.join(f"<!-- Page {p['source_page']} -->\n\n{p['text'].strip()}" for p in target_pages)+'\n'
    artifact=ROOT/'source_repairs/oc185b-20261014';artifact.mkdir(parents=True,exist_ok=True)
    (artifact/'OC185B_corrected.md').write_bytes(markdown.encode('utf-8'))
    legacy_md=Path(config['source_pack'])/doc['markdown_file']
    legacy_bytes=legacy_md.read_bytes();legacy_text=legacy_bytes.decode('utf-8-sig')
    if legacy_text.count(OLD)!=1:raise ValueError('Legacy Markdown correction anchor changed.')
    (artifact/'OC185B_legacy_before.md').write_bytes(legacy_bytes)
    record=dict(id='oc185b-currency-20261014',document_id=DOC,source_page=1,before=OLD,after=NEW,
        source_pdf_sha256=EXPECTED_PDF,previous_page_sha256=EXPECTED_PAGE,
        corrected_page_sha256=sha(fixed['text'].encode('utf-8')),
        corrected_markdown_sha256=sha(markdown.encode('utf-8')),
        legacy_markdown=str(legacy_md),legacy_markdown_before_sha256=sha(legacy_bytes),
        review='AI visual comparison with original PDF page 1; independent review pending',
        baseline=str(base),release=RELEASE,created_at=stamp())
    write(artifact/'repair_record.json',record)
    dest.mkdir(parents=True)
    shutil.copytree(base/'sources',dest/'sources')
    for name in ('review_annotations.json','feature_rules.json'):
        shutil.copy2(base/name,dest/name)
    relative='corrections/OC185B_corrected.md'
    (dest/'sources/corrections').mkdir(exist_ok=True)
    (dest/'sources'/relative).write_bytes(markdown.encode('utf-8'))
    manifest=read(base/'source_manifest.json')
    manifest['hashes'][relative]=sha(markdown.encode('utf-8'))
    # Keep the historical import variant intact; explicitly point current text to the repair.
    doc['markdown_file']='sources/'+relative;doc['markdown_sha256']=manifest['hashes'][relative]
    doc['source_repair']=record
    fixed['source_markdown']=doc['markdown_file'];fixed['markdown_sha256']=doc['markdown_sha256']
    write(dest/'source_manifest.json',manifest);write(dest/'index.json',docs)
    (dest/'all_circular_pages.jsonl').write_text(''.join(json.dumps(p,ensure_ascii=False)+'\n' for p in pages),encoding='utf-8')
    corpus=read(base/'corpus.json');corpus.update(release=RELEASE,baseline=str(base),status='candidate',source_repair=record)
    write(dest/'corpus.json',corpus)
    candidate=dict(config,data_dir=str(dest))
    write(dest/'candidate_config.json',candidate);write(dest/'previous_config.json',config)
    write(dest/'intake_state.json',dict(status='prepared',created_at=stamp(),active_config=str(config_path),
        previous_config_sha256=sha(config_path.read_bytes()),baseline=str(base),baseline_inputs=input_hashes(base),
        candidate_inputs=input_hashes(dest),candidate_config_sha256=sha((dest/'candidate_config.json').read_bytes()),
        previous_config_copy_sha256=sha((dest/'previous_config.json').read_bytes()),
        actions=[dict(id=DOC,action='transcription_corrected',pages=2)]))
    # User requested the Markdown itself be corrected for subsequent reuse.
    legacy_md.write_text(legacy_text.replace(OLD,NEW,1),encoding='utf-8')
    print(dest)


if __name__=='__main__':main()
