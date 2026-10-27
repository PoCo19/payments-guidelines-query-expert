"""Verify a portable candidate before running it; optional local index/model checks."""
import argparse,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))

def main():
    p=argparse.ArgumentParser();p.add_argument('--models',action='store_true');p.add_argument('--index',action='store_true');a=p.parse_args()
    manifest=json.loads((ROOT/'PACKAGE_MANIFEST.json').read_text())
    for name,expected in manifest['files'].items():
        path=(ROOT/name).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
            raise ValueError('Missing or changed packaged file: '+name)
    candidate=json.loads((ROOT/'ENGINEERING_CANDIDATE.json').read_text())
    if a.models:
        from model_transport import local_json
        config=json.loads((ROOT/'config.json').read_text())
        installed={m['name']:m['digest'] for m in local_json(config['ollama_url']+'/api/tags',timeout=10)['models']}
        for name,digest in candidate['model_digests'].items():
            if installed.get(name)!=digest:raise ValueError('Missing or changed model weights: '+name)
    if a.index:
        from app import Engine
        from tools.document_pipeline import validate_engine
        from graph_context import graph_status
        engine=Engine();result=validate_engine(engine)
        if result['fingerprint']!=candidate['corpus_fingerprint'] or graph_status(engine)['fingerprint']!=candidate['graph_sha256']:
            raise ValueError('Rebuilt corpus or graph differs from the candidate')
    print(json.dumps(dict(files_verified=len(manifest['files']),models_checked=a.models,index_checked=a.index,independent_acceptance='pending')))

if __name__=='__main__':main()
