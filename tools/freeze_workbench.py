"""Freeze the reviewed local inputs for the 27 October colleague code handoff.

Operator-only; preserves the active configuration and existing archives.
"""
import json,sys,zipfile,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app import Engine
from tools.handoff import read,sha,safe_name,verify_package
from tools.document_pipeline import verify_sources
from graph_context import graph_status

def main():
 config=read(ROOT/'config.json');source=ROOT/config['data_dir']
 verify_sources(source)
 target=ROOT/'handoff/workbench-20261027'
 if target.exists():raise ValueError('Frozen output already exists; never overwrite it.')
 engine=Engine(config=dict(config,vector_backend='json'))
 status=graph_status(engine)
 if status['status']!='active':raise ValueError('Active maintained graph required')
 members={}
 for name in ['index.json','all_circular_pages.jsonl','review_annotations.json','feature_rules.json','source_manifest.json','corpus.json']:
  members[name]=(source/name).read_bytes()
 for name in read(source/'source_manifest.json')['hashes']:
  safe_name(name);members['sources/'+name]=(source/'sources'/name).read_bytes()
 # Keep the already-frozen official acquisition provenance; no new scraping.
 with zipfile.ZipFile(ROOT/'handoff/payments-20261010/sources.zip') as old:
  for name in old.namelist():
   if name.startswith('provenance/'):members[name]=old.read(name)
 portable=dict(config,data_dir='data/releases/payments-workbench-20261027',source_pack='data/source-originals',
               embedding_cache='data/embedding_cache.sqlite3',reranker_path='models/reranker')
 portable['evidence_graph_path']=Path(config['evidence_graph_path']).as_posix()
 (ROOT/'config.workbench.json').write_text(json.dumps(portable,indent=2)+'\n',encoding='utf-8')
 with urllib.request.urlopen(config['ollama_url']+'/api/tags',timeout=10) as r:installed=json.load(r)
 models={m['name']:m['digest'] for m in installed['models']}
 target.mkdir(parents=True)
 with zipfile.ZipFile(target/'sources.zip','w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for name,raw in sorted(members.items()):
   info=zipfile.ZipInfo(name,(2026,10,27,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,raw)
 pinned=['config.workbench.json','requirements-lock.txt','requirements-acquisition.txt','models/reranker/manifest.json',
         portable['evidence_graph_path'],'source_quality_flags.json','query_policies.json']
 manifest=dict(schema_version=1,release='payments-workbench-20261027',
  review_status='Engineering handoff; independent payments acceptance pending.',
  corpus_fingerprint=engine.fingerprint,registry_fingerprint=engine.registry.fingerprint,
  graph_sha256=status['fingerprint'],model_digests={config[k]:models[config[k]] for k in ['generation_model','embedding_model']},
  archive_sha256=sha((target/'sources.zip').read_bytes()),
  files={name:dict(sha256=sha(raw),bytes=len(raw)) for name,raw in sorted(members.items())},
  reproducibility_files={name:sha((ROOT/name).read_bytes()) for name in pinned})
 (target/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
 verify_package(target)
 print(json.dumps(dict(files=len(members),archive_bytes=(target/'sources.zip').stat().st_size,
                      fingerprint=engine.fingerprint,graph=status['status'])))

if __name__=='__main__':main()
