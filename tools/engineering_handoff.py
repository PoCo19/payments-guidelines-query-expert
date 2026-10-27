"""Stage and hash a portable engineering candidate without changing the live app."""
import argparse,hashlib,json,shutil,sqlite3,sys,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.document_pipeline import INPUTS,verify_sources
from model_transport import local_json

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def write(path,value):path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def copy(source,target):
    target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)

def stage(destination):
    destination=destination.resolve()
    if destination.exists():raise ValueError('Use a new staging directory; existing work is never replaced.')
    config=json.loads((ROOT/'config.json').read_text());source=ROOT/config['data_dir']
    verify_sources(source);destination.mkdir(parents=True)
    for pattern in ('*.py','*.cmd','*.ps1','requirements*.txt','*.md','query_policies.json','source_quality_flags.json','config.example.json'):
        for p in ROOT.glob(pattern):copy(p,destination/p.name)
    copy(ROOT/'.gitignore',destination/'.gitignore')
    for directory in ('web','tools','tests','docs','evaluation','models/reranker','launch_orchestrator','source_repairs','pilot'):
        for p in (ROOT/directory).rglob('*'):
            if p.is_file() and '__pycache__' not in p.parts and p.suffix not in ('.pyc','.sqlite3','.zip'):
                copy(p,destination/p.relative_to(ROOT))
    # Small legacy corpora remain only for regression fixtures. No workflow DBs.
    for directory in ('data','data/all-products-v1'):
        for p in (ROOT/directory).glob('*'):
            if p.is_file() and p.suffix in ('.json','.jsonl') and p.name not in ('embeddings.json',):copy(p,destination/p.relative_to(ROOT))
    corpus=destination/'data/corpus';corpus.mkdir(parents=True)
    for name in (*INPUTS,'corpus.json'):
        if (source/name).exists():copy(source/name,corpus/name)
    shutil.copytree(source/'sources',corpus/'sources')
    graph=ROOT/config['evidence_graph_path'];copy(graph,corpus/'evidence_graph.json')
    originals=ROOT/config['source_pack'];copied=0;missing=[]
    for doc in json.loads((source/'index.json').read_text()):
        relative=doc.get('local_pdf')
        if relative and doc.get('local_pdf_root')!='corpus':
            path=(originals/relative).resolve()
            if path.is_relative_to(originals.resolve()) and path.is_file():
                copy(path,destination/'data/source-originals'/relative);copied+=1
            else:missing.append(doc['id'])
    config.update(data_dir='data/corpus',source_pack='data/source-originals',embedding_cache='data/embedding_cache.sqlite3',
        evidence_graph_path='data/corpus/evidence_graph.json',reranker_path='models/reranker')
    write(destination/'config.json',config)
    products=json.loads((ROOT/'config.products.json').read_text()) if (ROOT/'config.products.json').exists() else dict(config)
    products.update(data_dir='data/all-products-v1',source_pack='data/source-originals',reranker_path='models/reranker')
    write(destination/'config.products.json',products)
    cache=ROOT/json.loads((ROOT/'config.json').read_text())['embedding_cache']
    with sqlite3.connect(f'{cache.as_uri()}?mode=ro',uri=True) as src,sqlite3.connect(destination/'data/embedding_cache.sqlite3') as dst:src.backup(dst)
    installed={m['name']:m['digest'] for m in local_json(config['ollama_url']+'/api/tags',timeout=10)['models']}
    write(destination/'ENGINEERING_CANDIDATE.json',dict(status='engineering_candidate',independent_acceptance='pending',
        corpus_fingerprint=json.loads((source/'embedding_build.json').read_text())['fingerprint'],
        model_digests={config[k]:installed[config[k]] for k in ('generation_model','embedding_model')},
        original_pdfs_copied=copied,local_originals_missing=missing,live_source_manifest_sha256=sha(source/'source_manifest.json'),
        graph_sha256=sha(graph),notes='No user workflow records or installed Ollama weights included. Index rebuild uses content-addressed embedding cache.'))
    print(json.dumps(dict(stage=str(destination),originals_copied=copied,originals_missing=len(missing))))

def bundle(stage_path,output):
    stage_path=stage_path.resolve();output=output.resolve()
    if output.exists():raise ValueError('Use a new archive path')
    excluded=('chroma','registry','__pycache__','intake-check','qa-checks','venv')
    files=[p for p in stage_path.rglob('*') if p.is_file() and not any(x in excluded for x in p.relative_to(stage_path).parts)
        and p.name not in ('workflows.sqlite3','workflows.sqlite3-wal','workflows.sqlite3-shm','PACKAGE_MANIFEST.json','embedding_build.json','validation.json')
        and p.relative_to(stage_path).parts[:2]!=('data','releases')
        and (not p.name.endswith(('.sqlite3','.sqlite3-wal','.sqlite3-shm')) or p.relative_to(stage_path).as_posix()=='data/embedding_cache.sqlite3')
        and not p.name.endswith(('.pyc','.next','.pending','.log'))]
    manifest=dict(status='engineering_candidate_not_pilot_approved',files={p.relative_to(stage_path).as_posix():sha(p) for p in files})
    write(stage_path/'PACKAGE_MANIFEST.json',manifest);files.append(stage_path/'PACKAGE_MANIFEST.json')
    output.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
        for p in files:archive.write(p,p.relative_to(stage_path).as_posix())
    with zipfile.ZipFile(output) as archive:
        assert len(archive.namelist())==len(files)
        for name,expected in manifest['files'].items():
            if hashlib.sha256(archive.read(name)).hexdigest()!=expected:raise ValueError('Archive checksum mismatch: '+name)
    write(output.with_suffix('.sha256.json'),dict(sha256=sha(output),bytes=output.stat().st_size,files=len(files),status=manifest['status']))
    print(json.dumps(dict(archive=str(output),bytes=output.stat().st_size,files=len(files))))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('command',choices=['stage','bundle']);p.add_argument('--stage',type=Path,required=True);p.add_argument('--output',type=Path)
    a=p.parse_args()
    if a.command=='stage':stage(a.stage)
    elif not a.output:p.error('--output is required')
    else:bundle(a.stage,a.output)
