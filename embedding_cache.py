"""Content-addressed, resumable local embedding cache and snapshot builder."""
import array,hashlib,json,sqlite3,time
from pathlib import Path

def embedding_input(part):return part['title']+'\n'+(part['section_heading']+'\n' if part.get('section_heading') else '')+part['text']
def cache_key(model,digest,text):return hashlib.sha256(json.dumps([model,digest,text],ensure_ascii=False).encode()).hexdigest()
def build_cached(engine):
 from app import ROOT
 if not engine.store:raise ValueError('Cached builds require Chroma')
 model=engine.config['embedding_model'];digest=engine.model_digest()
 if not digest:raise ValueError('Installed embedding model not found')
 start=time.perf_counter();cache=Path(engine.config['embedding_cache']);cache=cache if cache.is_absolute() else ROOT/cache
 cache.parent.mkdir(parents=True,exist_ok=True)
 db=sqlite3.connect(cache);db.execute('CREATE TABLE IF NOT EXISTS embeddings (key TEXT PRIMARY KEY, dimension INTEGER NOT NULL, vector BLOB NOT NULL)')
 vectors=[];computed=0;hits=0;dimension=None
 try:
  for offset in range(0,len(engine.parts),16):
   batch=engine.parts[offset:offset+16];texts=[embedding_input(p) for p in batch];keys=[cache_key(model,digest,t) for t in texts];cached={}
   for key in keys:
    row=db.execute('SELECT dimension,vector FROM embeddings WHERE key=?',(key,)).fetchone()
    if row:
     a=array.array('d');a.frombytes(row[1])
     if len(a)!=row[0]:raise ValueError('Corrupt embedding cache entry')
     cached[key]=engine.unit(list(a))
   missing=list(dict.fromkeys(k for k in keys if k not in cached))
   if missing:
    reply=engine.ollama('/api/embed',{'model':model,'input':[texts[keys.index(k)] for k in missing],'truncate':False})
    if len(reply.get('embeddings',[]))!=len(missing):raise ValueError('Embedding batch count mismatch')
    for key,v in zip(missing,reply['embeddings']):
     v=engine.unit(v);cached[key]=v;db.execute('INSERT OR REPLACE INTO embeddings VALUES (?,?,?)',(key,len(v),array.array('d',v).tobytes()))
    db.commit();computed+=len(missing)
   hits+=len(batch)-len(missing)
   for key in keys:
    v=cached[key]
    if dimension is None:dimension=len(v)
    if len(v)!=dimension:raise ValueError('Cache/model dimensions differ')
    vectors.append(v)
   if offset%256==0 or len(vectors)==len(engine.parts):print(f'Prepared {len(vectors)}/{len(engine.parts)} vectors; computed {computed}, cache hits {hits}',flush=True)
  if engine.model_digest()!=digest:raise ValueError('Embedding model changed during build')
  engine.store.build(vectors,digest);engine.registry.persist(engine.data_dir/'registry');engine.vector_status=engine.store.status
  report=dict(chunks=len(vectors),computed=computed,cache_hits=hits,dimension=dimension,model=model,model_digest=digest,fingerprint=engine.fingerprint,elapsed_seconds=round(time.perf_counter()-start,2))
  (engine.data_dir/'embedding_build.json').write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps(report),flush=True)
 finally:db.close()
