"""Single-worker local jobs and staged upload UI over the existing intake pipeline."""
import base64
import copy
import datetime as dt
import hashlib
import io
import json
import os
from pathlib import Path
import queue
import re
import subprocess
import sys
import threading
import time
import uuid
from tools import document_pipeline as pipeline
from request_runtime import PROGRESS


class BusyError(ValueError):pass


class LocalJobs:
    def __init__(self,get_engine,set_engine,config_path):
        self.get_engine=get_engine;self.set_engine=set_engine;self.config_path=Path(config_path).resolve()
        self.jobs={};self.lock=threading.Lock();self.gate=threading.Lock()
        self.upload_root=pipeline.ROOT/'inbox/ui';self.upload_root.mkdir(parents=True,exist_ok=True)

    def start(self,label,operation):
        if not self.gate.acquire(blocking=False):raise BusyError('Another answer or import is running. Wait for it to finish.')
        key=uuid.uuid4().hex
        with self.lock:
            # Bounded process-local history, no user document text in progress logs.
            if len(self.jobs)>=50:
                self.jobs.pop(next(iter(self.jobs)))
            self.jobs[key]=dict(id=key,status='running',stage=label,started=time.time())
        def update(message):
            with self.lock:self.jobs[key]['stage']=str(message)[:300]
        def worker():
            token=PROGRESS.set(update)
            try:
                result=operation(update)
                with self.lock:self.jobs[key].update(status='completed',stage='Completed',result=result)
            except Exception as exc:
                with self.lock:self.jobs[key].update(status='failed',stage='Stopped',error=str(exc))
            finally:
                PROGRESS.reset(token)
                with self.lock:self.jobs[key]['elapsed_seconds']=round(time.time()-self.jobs[key]['started'],2)
                self.gate.release()
        threading.Thread(target=worker,daemon=True).start()
        return dict(id=key,status='running')

    def get(self,key):
        with self.lock:
            if key not in self.jobs:raise ValueError('Job not found. It may belong to an earlier server session.')
            result=copy.deepcopy(self.jobs[key])
        result.setdefault('elapsed_seconds',round(time.time()-result['started'],2))
        return result

    def answer(self,payload):
        return self.start('Finding evidence',lambda update:self.get_engine().answer(payload))

    def upload(self,payload):
        name=payload.get('filename','');suffix=Path(name).suffix.lower()
        if suffix not in ('.md','.pdf'):raise ValueError('Choose a Markdown or text-readable PDF file.')
        try:raw=base64.b64decode(payload['data_base64'],validate=True)
        except (ValueError,KeyError,TypeError) as exc:raise ValueError('Invalid upload encoding') from exc
        if not raw or len(raw)>10*1024*1024:raise ValueError('File must be between 1 byte and 10 MB.')
        if suffix=='.pdf' and not raw.startswith(b'%PDF-'):raise ValueError('File is not a PDF.')
        if suffix=='.pdf':
            from pypdf import PdfReader
            pdf=PdfReader(io.BytesIO(raw))
            if pdf.is_encrypted:raise ValueError('Encrypted PDF: supply an accessible source copy.')
            if len(pdf.pages)>500:raise ValueError('For documents over 500 pages, use the reviewed command-line intake.')
        key=uuid.uuid4().hex
        item=dict(payload.get('metadata') or {})
        item.update(file='source'+suffix)
        item.setdefault('id','intake:'+key)
        item.setdefault('retrieved_on',dt.date.today().isoformat())
        pipeline.validate_item(item)
        if item.get('revision_of') or item.get('expected_previous_sha256'):
            raise ValueError('Reviewed snapshot replacements currently use ingest.cmd; this screen adds new documents.')
        pages,method,physical=pipeline.extract(raw,suffix)
        if len(pages)>500:raise ValueError('For documents over 500 pages, use the reviewed command-line intake.')
        digest=pipeline.sha(raw)
        duplicate=[dict(id=d['id'],title=d['subject']) for d in self.get_engine().docs if digest in (d.get('source_sha256'),d.get('markdown_sha256')) or d['id']==item['id'] or d.get('source_pdf')==item['source_url']]
        thin=[n for n,text in pages if len(text.split())<15]
        target=self.upload_root/key;target.mkdir()
        (target/item['file']).write_bytes(raw)
        preview=dict(token=key,filename=Path(name).name,metadata=item,sha256=digest,page_count=len(pages),
                     physical_pages=physical,method=method,thin_pages=thin,duplicates=duplicate,
                     pages=[dict(page=n,text=text[:5000],characters=len(text)) for n,text in pages[:3]],
                     note='Preview shows up to three pages; extraction is not independently verified. Thin pages require review.')
        pipeline.write(target/'upload.json',preview)
        return preview

    def prepare(self,tokens):
        if not isinstance(tokens,list) or not 1<=len(tokens)<=10 or not all(isinstance(t,str) for t in tokens) or len(set(tokens))!=len(tokens):
            raise ValueError('Select between one and ten distinct reviewed uploads.')
        docs=[]
        for token in tokens:
            if not isinstance(token,str) or not re.fullmatch(r'[a-f0-9]{32}',token):raise ValueError('Invalid upload reference')
            target=self.upload_root/token
            record=pipeline.read(target/'upload.json')
            if pipeline.sha((target/record['metadata']['file']).read_bytes())!=record['sha256']:raise ValueError('Uploaded source changed; upload it again.')
            if record['duplicates']:raise ValueError('Duplicate source: use the command-line revision workflow after review.')
            docs.append(dict(record['metadata'],file=str(target/record['metadata']['file'])))
        name='upload-'+dt.datetime.now(dt.timezone.utc).strftime('%Y%m%d-%H%M%S')+'-'+uuid.uuid4().hex[:8]
        batch=self.upload_root/name;batch.mkdir();pipeline.write(batch/'intake.json',dict(schema_version=1,documents=docs))
        state=pipeline.prepare(batch/'intake.json',name,self.config_path)
        return dict(release=name,state=state,preview=self.preview(name))

    def preview(self,name):
        directory=pipeline.release_path(name);state=pipeline.read(directory/'intake_state.json')
        if Path(state['active_config']).resolve()!=self.config_path:raise ValueError('Release belongs to a different app configuration.')
        docs=pipeline.read(directory/'index.json');added={a['id'] for a in state.get('actions',[])}
        return dict(release=name,status=state['status'],documents=[{k:d.get(k) for k in ('id','subject','availability','page_count','source_coverage','notes')} for d in docs if d['id'] in added],
                    validation=pipeline.read(directory/'validation.json') if (directory/'validation.json').exists() else None)

    def releases(self):
        results=[]
        root=pipeline.ROOT/'data/releases'
        for directory in sorted(root.glob('*/intake_state.json'),key=lambda p:p.stat().st_mtime,reverse=True):
            try:
                state=pipeline.read(directory)
                if Path(state['active_config']).resolve()==self.config_path:
                    is_current=state['status']=='active' and pipeline.sha(self.config_path.read_bytes())==state.get('activated_config_sha256')
                    results.append(dict(release=directory.parent.name,status=state['status'],can_rollback=is_current))
            except (ValueError,KeyError,OSError):continue
        return results[:30]

    def build(self,name,update):
        self.preview(name)
        command=[sys.executable,'-B','-X','utf8',str(pipeline.ROOT/'tools/document_pipeline.py'),'build','--release',name]
        process=subprocess.Popen(command,cwd=pipeline.ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                                 text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW if os.name=='nt' else 0)
        lines=queue.Queue(); tail=[]
        def read():
            for line in process.stdout:lines.put(line)
        reader=threading.Thread(target=read,daemon=True);reader.start();deadline=time.monotonic()+1800
        try:
            while process.poll() is None or reader.is_alive() or not lines.empty():
                if time.monotonic()>deadline:
                    process.kill();process.wait();raise TimeoutError('Build stopped after 30 minutes. Active corpus is unchanged; retry Build to use cached progress.')
                try:line=lines.get(timeout=.2)
                except queue.Empty:continue
                tail.append(line);tail=tail[-30:]
                if line.startswith('Prepared') or line.startswith('Embedded'):update(line.strip())
            if process.returncode:raise ValueError('Index build failed; active corpus unchanged. '+''.join(tail)[-1000:])
        finally:
            if process.poll() is None:process.kill();process.wait()
            process.stdout.close()
        return self.preview(name)

    def activate(self,name):
        preview=self.preview(name)
        if not any(d['availability']=='converted' for d in preview['documents']):raise ValueError('No newly searchable documents. Repair the extraction before activation.')
        from app import Engine
        engine=Engine(config=pipeline.read(pipeline.release_path(name)/'candidate_config.json'))
        result=pipeline.activate(name)
        self.set_engine(engine)
        return dict(result,next_step='The app has loaded the new corpus.',stats=engine.stats())

    def rollback(self,name):
        self.preview(name)
        from app import Engine
        engine=Engine(config=pipeline.read(pipeline.release_path(name)/'previous_config.json'))
        result=pipeline.rollback(name);self.set_engine(engine)
        return dict(result,next_step='The app has loaded the previous corpus.',stats=engine.stats())
