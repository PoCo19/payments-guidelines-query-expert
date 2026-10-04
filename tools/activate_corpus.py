"""Activate a validated local corpus, or restore the preserved v0.4 data config."""
import argparse,hashlib,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from app import Engine,read_json

def verify_report(report,engine):
 if not report.get('passed') or report.get('fingerprint')!=engine.fingerprint or report.get('registry_fingerprint')!=engine.registry.fingerprint:
  raise ValueError('Validation is absent, failed or stale. Run evaluation/validate_v05.py first.')
 if not engine.vector_ready:raise ValueError('Candidate vector index is not ready: '+engine.vector_status)
 if engine.store.collection.count()!=len(engine.parts):raise ValueError('Vector count mismatch')
 if engine.model_digest()!=engine.store.collection.metadata.get('model_digest'):raise ValueError('Embedding model changed; rebuild and validate.')

def activate(rollback=False):
 candidate=ROOT/('versions/v0.4.0/config.json' if rollback else 'config.products.json')
 config=read_json(candidate)
 dataset=(ROOT/config.get('data_dir','data')).resolve()
 if not dataset.is_relative_to((ROOT/'data').resolve()):raise ValueError('Dataset must be inside this project data directory')
 engine=Engine(config=config)
 if rollback:
  if not engine.vector_ready:raise ValueError('Preserved index is not ready')
 else:
  verify_report(read_json(ROOT/'reports/v05_validation.json'),engine)
  live=read_json(ROOT/'reports/v05_live_answers.json')
  if not live.get('passed') or live.get('fingerprint')!=engine.fingerprint:raise ValueError('Run the live smoke checks before activation')
  for relative,digest in read_json(dataset/'source_manifest.json')['hashes'].items():
   source=(dataset/'sources'/relative).resolve()
   if not source.is_relative_to((dataset/'sources').resolve()):raise ValueError('Invalid manifest path')
   if hashlib.sha256(source.read_bytes()).hexdigest()!=digest:raise ValueError('Source copy changed: '+relative)
 active=ROOT/'config.json';temp=ROOT/'config.next.json'
 temp.write_text(json.dumps(config,indent=2)+'\n',encoding='utf-8')
 os.replace(temp,active)
 print('Active data directory:',dataset)
 print('Restart the server to use this configuration. No old source data was removed.')

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--rollback',action='store_true');args=parser.parse_args();activate(args.rollback)
