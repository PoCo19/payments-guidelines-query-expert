"""Operator utility: freeze an existing release plus official RBI acquisition snapshots."""
import argparse
import json
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.handoff import sha, read, safe_name
from tools.document_pipeline import verify_sources


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source', type=Path, required=True)
    p.add_argument('--provenance', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    verify_sources(args.source)
    members = {}
    for name in ['index.json', 'all_circular_pages.jsonl', 'review_annotations.json', 'feature_rules.json', 'source_manifest.json', 'corpus.json']:
        members[name] = (args.source / name).read_bytes()
    for name in read(args.source / 'source_manifest.json')['hashes']:
        safe_name(name)
        members['sources/' + name] = (args.source / 'sources' / name).read_bytes()
    for path in sorted(args.provenance.iterdir()):
        if path.is_file() and path.suffix in ('.html', '.md', '.json'):
            members['provenance/rbi-core-20261009/' + path.name] = path.read_bytes()
    args.output.mkdir(parents=True, exist_ok=False)
    archive = args.output / 'sources.zip'
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, raw in sorted(members.items()):
            info = zipfile.ZipInfo(name, (2026, 10, 10, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, raw)
    validation = read(args.source / 'validation.json')
    capture = read(ROOT / 'evaluation/payments_runs/20261010T081610Z/capture.json')
    config = read(ROOT / 'config.handoff.json')
    model_names = [config['generation_model'], config['embedding_model']]
    models = {m['name']: m['digest'] for m in capture['installed_models']['models'] if m['name'] in model_names}
    if set(models) != set(model_names):
        raise ValueError('Capture does not identify both required models')
    pinned = ['config.handoff.json', 'requirements-lock.txt', 'evaluation/requirements-ragas-lock.txt',
              'evaluation/payments_cases_v1.json', 'evaluation/payments_cases_v1.sha256',
              'evaluation/rag_cases.json', 'evaluation/rag_cases.sha256', 'models/reranker/manifest.json']
    manifest = dict(schema_version=1, release='payments-handoff-20261010',
        review_status='Imported official snapshots; existing review annotations preserved. Full independent source and answer review pending.',
        corpus_fingerprint=validation['fingerprint'], registry_fingerprint=validation['registry_fingerprint'],
        archive_sha256=sha(archive.read_bytes()), model_digests=models,
        files={name:dict(sha256=sha(raw), bytes=len(raw)) for name, raw in sorted(members.items())},
        reproducibility_files={name:sha((ROOT/name).read_bytes()) for name in pinned})
    (args.output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(dict(files=len(members), archive_bytes=archive.stat().st_size, archive_sha256=manifest['archive_sha256'])))


if __name__ == '__main__':
    main()
