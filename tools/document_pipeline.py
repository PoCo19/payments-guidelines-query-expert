"""Local, staged document intake. No downloads and no implicit live activation."""
import argparse
import datetime as dt
import hashlib
import io
import json
import os
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
INPUTS = ('index.json', 'all_circular_pages.jsonl', 'review_annotations.json', 'feature_rules.json', 'source_manifest.json', 'intake_quality.json', 'reference_graph.json', 'evidence_graph.json')


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def write(path, value):
    path = Path(path)
    temp = path.with_suffix(path.suffix + '.next')
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.replace(temp, path)


def stamp():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def resolve_data(config):
    return (ROOT / config.get('data_dir', 'data')).resolve()


def release_path(name):
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]{2,70}', name):
        raise ValueError('Release name: 3–71 lowercase letters, digits or hyphens.')
    return ROOT / 'data' / 'releases' / name


def input_hashes(directory):
    return {name: sha((directory / name).read_bytes()) for name in INPUTS if (directory / name).exists()}


def verify_sources(directory):
    manifest = read(directory / 'source_manifest.json')
    base = (directory / 'sources').resolve()
    for relative, expected in manifest['hashes'].items():
        source = (base / relative).resolve()
        if not source.is_relative_to(base) or not source.is_file() or sha(source.read_bytes()) != expected:
            raise ValueError('Source copy missing or changed: ' + relative)


def extract(raw, suffix):
    """PDF page numbers are physical; unpaginated Markdown uses one logical page."""
    if suffix == '.pdf':
        from pypdf import PdfReader
        pdf = PdfReader(io.BytesIO(raw))
        if pdf.is_encrypted:
            raise ValueError('Encrypted PDF: supply an accessible source copy.')
        return [(i + 1, p.extract_text() or '') for i, p in enumerate(pdf.pages)], 'pypdf', True
    if suffix != '.md':
        raise ValueError('Only .md and text-readable .pdf sources are supported.')
    text = raw.decode('utf-8-sig')
    markers = list(re.finditer(r'<!--\s*Page\s+(\d+)\s*-->', text, re.I))
    if not markers:
        return [(1, text.strip())], 'markdown_logical_page', False
    if text[:markers[0].start()].strip():
        raise ValueError('Move substantive Markdown preamble inside page 1; it cannot be silently discarded.')
    numbers = [int(m[1]) for m in markers]
    if numbers != list(range(1, len(numbers) + 1)):
        raise ValueError('Markdown page markers must be unique and sequential, starting at 1.')
    return [(n, text[m.end():markers[i+1].start() if i+1 < len(markers) else len(text)].strip())
            for i, (n, m) in enumerate(zip(numbers, markers))], 'imported_markdown', False


def validate_item(item):
    if not isinstance(item, dict):
        raise ValueError('Each documents entry must be a JSON object.')
    for field in ('id', 'file', 'title', 'issuer', 'document_type', 'reference', 'source_url', 'retrieved_on'):
        if not isinstance(item.get(field), str) or not item[field].strip():
            raise ValueError('Required nonempty field: ' + field)
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9:._-]{2,160}', item['id']):
        raise ValueError('Invalid stable document id')
    products = item.get('products')
    if not isinstance(products, list) or not products or not all(isinstance(p, str) and p.strip() for p in products) or len(set(products)) != len(products):
        raise ValueError('Supply distinct, nonempty products/topics.')
    url = urlsplit(item['source_url'])
    if url.scheme != 'https' or not url.hostname or url.username or url.password:
        raise ValueError('Supply a public source URL without credentials.')
    for field in ('retrieved_on', 'issue_date', 'updated_on'):
        if item.get(field):
            if not isinstance(item[field], str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', item[field]):
                raise ValueError(field + ' must use YYYY-MM-DD.')
            dt.date.fromisoformat(item[field])
    for field in ('revision_of', 'expected_previous_sha256'):
        if field in item and (not isinstance(item[field], str) or not item[field]):
            raise ValueError(field + ' must be a nonempty string.')
    if item.get('allow_partial') is not None and not isinstance(item['allow_partial'], bool):
        raise ValueError('allow_partial must be a boolean')
    if 'source_notes' in item and (not isinstance(item['source_notes'], list) or not all(isinstance(n,str) and n.strip() for n in item['source_notes'])):
        raise ValueError('source_notes must be a list of nonempty strings')
    if 'applicability' in item:
        scope = item['applicability']
        if (not isinstance(scope, dict) or not isinstance(scope.get('entities'), list) or not scope['entities']
            or not all(isinstance(x,str) and x.strip() and len(x)<=120 for x in scope['entities'])
            or type(scope.get('page')) is not int or scope['page']<1 or not isinstance(scope.get('quote'),str) or not scope['quote'].strip()):
            raise ValueError('applicability requires entities, a source page and an exact source quote.')


def prepare(manifest_path, name, active_path=None):
    active_path = Path(active_path or ROOT / 'config.json').resolve()
    manifest_path = Path(manifest_path).resolve()
    request = read(manifest_path)
    if request.get('schema_version') != 1 or not isinstance(request.get('documents'), list) or not request['documents']:
        raise ValueError('Manifest requires schema_version 1 and a nonempty documents list.')
    config = read(active_path)
    base = resolve_data(config)
    destination = release_path(name)
    if destination.exists():
        raise ValueError('Release already exists. Use build to resume, or choose a new name.')
    baseline = input_hashes(base)
    verify_sources(base)
    docs = read(base / 'index.json')
    pages = [json.loads(line) for line in (base / 'all_circular_pages.jsonl').read_text(encoding='utf-8-sig').split('\n') if line.strip()]
    by_id = {d['id']: d for d in docs}
    source_hashes = read(base / 'source_manifest.json')['hashes'].copy()
    additions, actions = [], []
    from intake_quality import inspect_pages, reviewed_blockers
    quality_records = read(base / 'intake_quality.json').get('pages', []) if (base / 'intake_quality.json').exists() else []
    submitted = set()
    for item in request['documents']:
        validate_item(item)
        key = item['id']
        if key in submitted:
            raise ValueError('Repeated manifest id: ' + key)
        submitted.add(key)
        path = (manifest_path.parent / item['file']).resolve()
        raw = path.read_bytes()
        digest = sha(raw)
        original_raw = None
        if 'original_pdf' in item:
            if path.suffix.lower() != '.md' or not isinstance(item['original_pdf'], str) or not item['original_pdf'].strip():
                raise ValueError('original_pdf is a nonempty file path for a Markdown intake item')
            original_raw = (manifest_path.parent / item['original_pdf']).resolve().read_bytes()
            if not original_raw.startswith(b'%PDF-'):
                raise ValueError('Original companion is not a PDF')
        if key in by_id:
            existing = by_id[key]
            if existing.get('availability') != 'archived_snapshot' and existing.get('intake_metadata') == item and existing.get('source_sha256') == digest and existing.get('original_pdf_sha256') == (sha(original_raw) if original_raw is not None else None):
                actions.append(dict(id=key, action='unchanged'))
                continue
            raise ValueError('Existing id has different content or metadata. Use a new id and revision_of: ' + key)
        duplicate = next((d for d in docs if digest in (d.get('source_sha256'), d.get('markdown_sha256'))), None)
        if duplicate:
            raise ValueError('Identical file already registered as ' + duplicate['id'])
        previous = item.get('revision_of')
        conflicts = [d for d in docs if d.get('source_pdf') == item['source_url'] and d.get('availability') != 'archived_snapshot']
        if conflicts and (len(conflicts) != 1 or conflicts[0]['id'] != previous):
            raise ValueError('Source URL already registered. Declare revision_of for a reviewed new snapshot: ' + key)
        if previous:
            old = by_id.get(previous)
            if not old or not item.get('expected_previous_sha256') or item['expected_previous_sha256'] != (old.get('source_sha256') or old.get('markdown_sha256')):
                raise ValueError('revision_of requires an existing id and its exact expected_previous_sha256.')
            if old.get('issuer', 'NPCI') != item['issuer']:
                raise ValueError('Revision issuer must match the previous snapshot.')
            if old.get('availability') == 'archived_snapshot':
                raise ValueError('Replace the current snapshot, not an already archived one.')
        try:
            extracted, method, physical = extract(raw, path.suffix.lower())
        except Exception as exc:
            raise ValueError('Extraction failed for ' + key + ': ' + str(exc)) from exc
        if not extracted:
            raise ValueError('Document has no pages: ' + key)
        if item.get('applicability'):
            scope = item['applicability']
            page_text = dict(extracted).get(scope['page'], '')
            if ' '.join(scope['quote'].split()) not in ' '.join(page_text.split()):
                raise ValueError('Applicability quote does not match its source page: ' + key)
        page_quality = inspect_pages(key, extracted)
        blocked_pages = reviewed_blockers(page_quality, item.get('quality_reviews', []))
        original_pdf = None
        if original_raw is not None:
            from pypdf import PdfReader
            original_pages = len(PdfReader(io.BytesIO(original_raw)).pages)
            if method != 'imported_markdown' or len(extracted) != original_pages:
                raise ValueError('Companion PDF requires sequential Markdown page markers matching its physical page count')
            original_pdf = 'intake/' + sha(key.encode())[:24] + '-original.pdf'
            source_hashes[original_pdf] = sha(original_raw)
            additions.append((original_pdf, original_raw))
            physical = True  # verifies page count only, not text accuracy
        quality_records.extend(page_quality)
        empty = [n for n, text in extracted if not text.strip()]
        thin = [n for n, text in extracted if len(text.split()) < 15]
        partial = bool(thin)
        searchable = any(text.strip() for _, text in extracted) and (not partial or item.get('allow_partial') is True) and not blocked_pages
        if previous and not searchable:
            raise ValueError('A quarantined revision cannot replace a searchable snapshot. Repair/review the extraction first.')
        if previous:
            by_id[previous]['availability'] = 'archived_snapshot'
            by_id[previous]['replaced_by_snapshot'] = key
        relative = 'intake/' + sha(key.encode())[:24] + path.suffix.lower()
        source_hashes[relative] = digest
        local = 'sources/' + relative
        d = dict(id=key, subject=item['title'], listing_title=item['title'], series=item['products'][0],
                 product_memberships=item['products'], circular_number=item['reference'], reference_label=item['reference'],
                 issuer=item['issuer'], document_type=item['document_type'], issue_date=item.get('issue_date'),
                 listed_update_date=item.get('updated_on'), source_archive_retrieved_on=item['retrieved_on'],
                 source_pdf=item['source_url'], source_root='intake', local_pdf=local if path.suffix.lower()=='.pdf' else None,
                 local_pdf_root='corpus', source_file=local, source_sha256=digest, intake_metadata=item,
                 availability='converted' if searchable else 'needs_source_review', related_circulars=[], family='',
                 metadata_quality='operator_supplied_not_independently_verified', page_count=len(extracted),
                 source_coverage=dict(total_pages=len(extracted), empty_pages=empty, thin_pages=thin, page_count_verified=physical,
                                      page_basis='physical_pdf' if physical else 'markdown_markers' if method=='imported_markdown' else 'logical_markdown'),
                 notes=['Snapshot replacement is a local indexing decision, not a legal supersession determination.'] if previous else [],
                 revision_of=previous)
        if original_pdf:
            d['local_pdf'] = 'sources/' + original_pdf
            d['original_pdf_sha256'] = source_hashes[original_pdf]
        d['intake_quality'] = dict(blocked_pages=blocked_pages, pages=page_quality,
            reviews=item.get('quality_reviews', []), basis='heuristic_triage_not_source_certification')
        if any(p['findings'] for p in page_quality):
            d['notes'].append('Extraction quality flags require original-source review: ' + ', '.join(sorted({f['code'] for p in page_quality for f in p['findings']})))
        d['notes'].extend(item.get('source_notes', []))
        if partial:
            d['notes'].append('Empty/thin pages require source review.' + (' Partial extraction explicitly accepted for indexing.' if searchable else ' Excluded from retrieval.'))
        if item.get('applicability'):
            d['applicability'] = dict(item['applicability'], basis='operator_labels_with_source_quote_not_independently_verified')
        docs.append(d)
        by_id[key] = d
        for n, text in extracted:
            pages.append(dict(document_id=key, source_page=n, text=text, method=method,
                              review_status='intake_text_not_verified', needs_priority_review=n in thin or bool(next(p['findings'] for p in page_quality if p['page']==n)),
                              source_text_status='empty' if n in empty else 'thin' if n in thin else 'unverified', source_file=local, source_sha256=digest))
        additions.append((relative, raw))
        actions.append(dict(id=key, action=d['availability'], pages=len(extracted), thin_pages=thin, blocked_quality_pages=blocked_pages, revision_of=previous))
    if all(a['action'] == 'unchanged' for a in actions):
        return dict(status='unchanged', actions=actions)
    destination.mkdir(parents=True)
    write(destination / 'intake_state.json', dict(status='preparing', created_at=stamp()))
    if (base / 'sources').exists():
        shutil.copytree(base / 'sources', destination / 'sources')
    for filename in ('review_annotations.json', 'feature_rules.json'):
        if (base / filename).exists():
            shutil.copy2(base / filename, destination / filename)
    for relative, raw in additions:
        target = destination / 'sources' / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    write(destination / 'intake_quality.json', dict(version=1, pages=quality_records, limitation='Flags are review candidates; no automatic OCR correction.'))
    write(destination / 'index.json', docs)
    (destination / 'all_circular_pages.jsonl').write_text(''.join(json.dumps(p, ensure_ascii=False)+'\n' for p in pages), encoding='utf-8')
    write(destination / 'source_manifest.json', dict(hashes=source_hashes, policy='Immutable source copies; manually supplied provenance.'))
    corpus = read(base / 'corpus.json') if (base / 'corpus.json').exists() else {}
    corpus.update(release=name, baseline=str(base), documents=len(docs), pages=len(pages), status='candidate',
                  snapshot='Local intake ' + stamp()[:10] + '; source-specific retrieval dates retained',
                  window='Mixed source snapshots; inspect issue and update dates per document', intake_actions=actions)
    write(destination / 'corpus.json', corpus)
    from reference_graph import build_release
    write(destination / 'reference_graph.json',build_release(destination,base/'reference_graph.json'))
    # Carry the exact maintained manifest with the candidate; validation below
    # reports stale anchors rather than silently re-approving changed sources.
    if config.get('evidence_graph_path'):
        graph_path=Path(config['evidence_graph_path'])
        if not graph_path.is_absolute():graph_path=ROOT/graph_path
        if graph_path.is_file():
            shutil.copy2(graph_path,destination/'evidence_graph.json')
            config['evidence_graph_path']=str(destination/'evidence_graph.json')
    config['reference_graph_enabled']=False
    config.update(data_dir=str(destination), multi_product=True, vector_backend='chroma',
                  reference_graph_path=str(destination/'reference_graph.json'),
                  embedding_cache=str(ROOT / 'data/embedding_cache.sqlite3'),
                  query_instruction='Given a question about payment guidelines, retrieve relevant passages that answer the question.')
    write(destination / 'candidate_config.json', config)
    write(destination / 'previous_config.json', read(active_path))
    state = dict(status='prepared', created_at=stamp(), active_config=str(active_path),
                 previous_config_sha256=sha(active_path.read_bytes()), baseline=str(base), baseline_inputs=baseline,
                 candidate_inputs=input_hashes(destination), candidate_config_sha256=sha((destination/'candidate_config.json').read_bytes()),
                 previous_config_copy_sha256=sha((destination/'previous_config.json').read_bytes()), actions=actions)
    write(destination / 'intake_state.json', state)
    return state


def check_candidate(directory):
    state = read(directory / 'intake_state.json')
    if state.get('status') not in ('prepared', 'validated', 'active'):
        raise ValueError('Preparation is incomplete; inspect this release and create a new one.')
    if input_hashes(directory) != state['candidate_inputs'] or sha((directory/'candidate_config.json').read_bytes()) != state['candidate_config_sha256']:
        raise ValueError('Candidate changed after preparation. Create a fresh release.')
    verify_sources(directory)
    return state


def build(name):
    from app import Engine
    directory = release_path(name)
    state = check_candidate(directory)
    active_config = Path(state['active_config'])
    if state['status'] == 'active' or (active_config.exists() and resolve_data(read(active_config)) == directory.resolve()):
        raise ValueError('Do not rebuild an active release; prepare a new candidate.')
    engine = Engine(config=read(directory / 'candidate_config.json'))
    if not engine.parts:
        raise ValueError('No searchable passages in candidate.')
    engine.build_vectors()
    result = read(directory / 'embedding_build.json')
    report = validate_engine(engine)
    from graph_context import graph_status
    report['graph_assistance']=graph_status(engine)
    report.update(created_at=stamp(), embeddings=result)
    check_candidate(directory)
    write(directory / 'validation.json', report)
    state['status'] = 'validated'
    write(directory / 'intake_state.json', state)
    return report


def validate_engine(engine):
    if not engine.vector_ready or not engine.store or engine.store.collection.count() != len(engine.parts):
        raise ValueError('Vector index is incomplete.')
    digest = engine.model_digest()
    if not digest or digest != engine.store.collection.metadata.get('model_digest'):
        raise ValueError('Embedding model changed. Rebuild the candidate with the installed model.')
    if len({d['id'] for d in engine.docs}) != len(engine.docs) or len({(p['document_id'], p['source_page']) for p in engine.pages}) != len(engine.pages):
        raise ValueError('Duplicate document or page identity.')
    indexed = {p['document_id'] for p in engine.parts}
    if any(d['availability']=='converted' and d['id'] not in indexed for d in engine.docs):
        raise ValueError('Searchable document has no chunks.')
    for d in engine.docs:
        if d.get('source_root') == 'intake' and d['availability']=='converted':
            hits = engine.search(d['subject'], method='bm25', document_ids=[d['id']], k=1)
            if not hits or hits[0]['document_id'] != d['id']:
                raise ValueError('Document retrieval smoke check failed: ' + d['id'])
    return dict(passed=True, fingerprint=engine.fingerprint, registry_fingerprint=engine.registry.fingerprint,
                model_digest=digest, documents=len(engine.docs), chunks=len(engine.parts),
                limitation='Structural and per-intake-document retrieval checks; not expert answer correctness.')


def activate(name):
    from app import Engine
    directory = release_path(name)
    state = check_candidate(directory)
    if state['status'] != 'validated':
        raise ValueError('Build and validate before activation.')
    active = Path(state['active_config'])
    if sha(active.read_bytes()) != state['previous_config_sha256'] or input_hashes(Path(state['baseline'])) != state['baseline_inputs']:
        raise ValueError('Live config or source/review inputs changed. Prepare a fresh release from the current corpus.')
    config = read(directory / 'candidate_config.json')
    engine = Engine(config=config)
    current = validate_engine(engine)
    from graph_context import graph_status
    current['graph_assistance']=graph_status(engine)
    saved = read(directory / 'validation.json')
    if not saved.get('passed') or any(saved.get(k) != current[k] for k in ('fingerprint','registry_fingerprint','model_digest')):
        raise ValueError('Validation is missing or stale.')
    write(active, config)
    state.update(status='active', activated_at=stamp(), activated_config_sha256=sha(active.read_bytes()))
    write(directory / 'intake_state.json', state)
    return dict(status='active', release=name, graph_assistance=current['graph_assistance'],
                next_step='Restart run.cmd to load this release.')


def rollback(name):
    directory = release_path(name)
    state = read(directory / 'intake_state.json')
    active = Path(state['active_config'])
    if state['status'] != 'active' or sha(active.read_bytes()) != state.get('activated_config_sha256'):
        raise ValueError('Live config no longer matches this activation; refusing to overwrite it.')
    if input_hashes(Path(state['baseline'])) != state['baseline_inputs']:
        raise ValueError('Previous source inputs changed; inspect before restoring.')
    if sha((directory/'previous_config.json').read_bytes()) != state['previous_config_copy_sha256']:
        raise ValueError('Saved rollback configuration changed.')
    write(active, read(directory / 'previous_config.json'))
    state.update(status='rolled_back', rolled_back_at=stamp())
    write(directory / 'intake_state.json', state)
    return dict(status='rolled_back', next_step='Restart run.cmd. Both source releases were retained.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('prepare'); p.add_argument('--manifest', required=True); p.add_argument('--release', required=True)
    for command in ('build', 'activate', 'rollback', 'status'):
        p = sub.add_parser(command); p.add_argument('--release', required=True)
    args = parser.parse_args()
    try:
        if args.command == 'prepare':
            result = prepare(args.manifest, args.release)
        elif args.command == 'status':
            result = read(release_path(args.release) / 'intake_state.json')
        else:
            result = globals()[args.command](args.release)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(1, 'Intake stopped: ' + str(exc) + '\n')


if __name__ == '__main__':
    main()
