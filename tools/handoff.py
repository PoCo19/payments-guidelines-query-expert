"""Restore and verify the frozen colleague source handoff (standard library only)."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import sys
import tempfile
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'handoff/payments-20261010'
DESTINATION = 'data/releases/payments-handoff-20261010'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def safe_name(name):
    path = PurePosixPath(name)
    if not name or '\\' in name or ':' in name or path.is_absolute() or any(p in ('..', '.') for p in name.split('/')):
        raise ValueError('Unsafe archive member: ' + name)
    return path


def verify_package(package=PACKAGE):
    manifest = read(package / 'manifest.json')
    archive = package / 'sources.zip'
    if sha(archive.read_bytes()) != manifest['archive_sha256']:
        raise ValueError('Source archive checksum mismatch')
    for name in manifest['files']:
        safe_name(name)
    with zipfile.ZipFile(archive) as z:
        names = z.namelist()
        if len(names) != len(set(names)) or set(names) != set(manifest['files']):
            raise ValueError('Archive member inventory mismatch')
        for name in names:
            safe_name(name)
            info = z.getinfo(name)
            expected = manifest['files'][name]
            if info.file_size != expected['bytes'] or sha(z.read(name)) != expected['sha256']:
                raise ValueError('Archive member checksum mismatch: ' + name)
    return manifest


def verify_files(destination, manifest):
    for name, expected in manifest['files'].items():
        path = destination / safe_name(name)
        if not path.is_file() or path.is_symlink() or sha(path.read_bytes()) != expected['sha256']:
            raise ValueError('Restored source missing or changed: ' + name)


def restore(destination, package=PACKAGE):
    manifest = verify_package(package)
    if destination.exists():
        verify_files(destination, manifest)
        return manifest  # Idempotent; never overwrite local source edits.
    destination.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='handoff-', dir=destination.parent))
    try:
        with zipfile.ZipFile(package / 'sources.zip') as z:
            for name in manifest['files']:
                path = stage / safe_name(name)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(z.read(name))
        verify_files(stage, manifest)
        os.rename(stage, destination)
    finally:
        if stage.exists():
            shutil.rmtree(stage)
    return manifest


def verify_runtime(destination, manifest):
    sys.path.insert(0, str(ROOT))
    from app import Engine
    from evaluation.payments_eval import validate_anchors
    from evaluation.ragas_runner import load_cases
    from tools.document_pipeline import verify_sources
    verify_files(destination, manifest)
    verify_sources(destination)
    config = read(ROOT / 'config.handoff.json')
    engine = Engine(data_dir=destination, config=dict(config, vector_backend='json'))
    if engine.fingerprint != manifest['corpus_fingerprint'] or engine.registry.fingerprint != manifest['registry_fingerprint']:
        raise ValueError('Reconstructed corpus/registry differs from the frozen handoff')
    cases, _ = load_cases(ROOT / 'evaluation/payments_cases_v1.json')
    validate_anchors(cases, engine)
    for name, expected in manifest['reproducibility_files'].items():
        if sha((ROOT / name).read_bytes()) != expected:
            raise ValueError('Pinned configuration, dependency or dataset changed: ' + name)
    return dict(documents=len(engine.docs), pages=len(engine.pages), chunks=len(engine.parts),
                corpus_fingerprint=engine.fingerprint, registry_fingerprint=engine.registry.fingerprint,
                mixed_source_cases_validated=len(cases), model_calls=0)


def verify_models(manifest):
    config = read(ROOT / 'config.handoff.json')
    # The release uses localhost only; no remote API credentials are required.
    with urllib.request.urlopen('http://127.0.0.1:11434/api/tags', timeout=10) as response:
        installed = {m['name']: m['digest'] for m in json.load(response)['models']}
    for name, expected in manifest['model_digests'].items():
        if installed.get(name) != expected:
            raise ValueError('Missing or different model weights: ' + name)
    reranker = ROOT / config['reranker_path']
    for name, expected in read(reranker / 'manifest.json')['sha256'].items():
        if not (reranker / name).exists() or sha((reranker / name).read_bytes()) != expected:
            raise ValueError('Missing or different reranker asset: ' + name)
    return {'models_match': True, 'reranker_matches': True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['restore', 'verify', 'models'])
    args = parser.parse_args()
    destination = ROOT / DESTINATION
    manifest = restore(destination) if args.command == 'restore' else verify_package()
    result = verify_models(manifest) if args.command == 'models' else verify_runtime(destination, manifest)
    print(json.dumps(dict(status='passed', command=args.command, **result), indent=2))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, zipfile.BadZipFile) as exc:
        print('Handoff check failed: ' + str(exc), file=sys.stderr)
        raise SystemExit(1)
