"""Loopback-only launch workspace. Run: python launch_app.py [--port 8766]."""
import argparse
import json
import logging
import threading
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from launch_orchestrator.core import Store, Conflict, clean
from launch_orchestrator.demo import create_feature_demo
from launch_orchestrator.generation import Worker

ROOT=Path(__file__).resolve().parent


class Application:
    def __init__(self, database=None, config=None):
        self.config=config or json.loads((ROOT/'config.json').read_text(encoding='utf-8-sig'))
        self.store=Store(database or ROOT/'data/launches/launches.sqlite3')
        self.worker=Worker(self.store,self.config)
        self.engine=None; self.engine_lock=threading.Lock()

    def evidence(self, query=None, chunk_id=None):
        with self.engine_lock:
            if self.engine is None:
                from app import Engine
                # This V1 picker is lexical: avoid opening Chroma or rewriting its
                # derived registry merely to import an attributed passage.
                self.engine=Engine(config={**self.config,'vector_backend':'json'})
            if chunk_id:
                result=self.engine.parts_by_id.get(chunk_id)
                if not result: raise ValueError('Evidence passage not found')
                return result
            return self.engine.search(clean(query,2000),method='bm25',series='UPI',k=6)


def handler_for(app):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            logging.info(fmt,*args)

        def send(self, value, status=200, content_type='application/json; charset=utf-8'):
            raw=json.dumps(value,ensure_ascii=False).encode() if content_type.startswith('application/json') else value.encode() if isinstance(value,str) else value
            self.send_response(status)
            self.send_header('Content-Type',content_type)
            self.send_header('Content-Length',str(len(raw)))
            self.send_header('Cache-Control','no-store')
            self.send_header('X-Content-Type-Options','nosniff')
            self.send_header('Content-Security-Policy',"default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'")
            self.end_headers(); self.wfile.write(raw)

        def valid_request(self):
            port=self.server.server_port
            allowed={f'127.0.0.1:{port}',f'localhost:{port}'}
            if self.headers.get('Host') not in allowed: raise PermissionError('Only local hosts are allowed')
            origin=self.headers.get('Origin')
            if origin and origin not in {'http://'+h for h in allowed}: raise PermissionError('Cross-origin requests are not allowed')

        def route(self, post=False):
            try:
                self.valid_request()
                parsed=urllib.parse.urlparse(self.path); path=parsed.path
                parts=path.strip('/').split('/')
                if not post:
                    static={'/':('index_v2.html','text/html; charset=utf-8'),'/app.js':('app_v2.js','text/javascript; charset=utf-8'),'/style.css':('style_v2.css','text/css; charset=utf-8')}
                    if path in static:
                        file,mime=static[path]; return self.send((ROOT/'web/launch'/file).read_bytes(),content_type=mime)
                    if path=='/api/launches': return self.send(app.store.list())
                    if path=='/api/health':
                        available=False; models=[]
                        try:
                            with urllib.request.urlopen(app.config['ollama_url'].rstrip('/')+'/api/tags',timeout=3) as r:
                                models=[m['name'] for m in json.load(r).get('models',[])]; available=app.config['generation_model'] in models
                        except Exception: pass
                        return self.send({'model':app.config['generation_model'],'available':available,'models':models,'version':'2.0.0','local_only':True})
                    if path=='/api/evidence':
                        q=urllib.parse.parse_qs(parsed.query).get('q',[''])[0]
                        return self.send(app.evidence(query=q))
                    if len(parts)==3 and parts[:2]==['api','launches']: return self.send(app.store.get(parts[2]))
                    if len(parts)==4 and parts[:2]==['api','launches'] and parts[3]=='export':
                        return self.send(app.store.export(parts[2]),content_type='text/markdown; charset=utf-8')
                    return self.send({'error':'Not found'},404)
                if self.headers.get('Content-Type','').split(';')[0]!='application/json': raise ValueError('Send application/json')
                size=int(self.headers.get('Content-Length','0'))
                limit=7*1024*1024 if path=='/api/extract-document' else 131072
                if not 0<size<=limit: raise ValueError('The request is too large. Use a smaller file or source excerpt.')
                payload=json.loads(self.rfile.read(size))
                if not isinstance(payload,dict): raise ValueError('Expected a JSON object')
                if path=='/api/extract-document':
                    from launch_orchestrator.documents import extract_document
                    return self.send(extract_document(payload))
                if path=='/api/launches': return self.send(app.store.create(payload),201)
                if path=='/api/demo':
                    from launch_orchestrator.core import actor, permitted
                    name,role=actor(payload); permitted(role)
                    return self.send(create_feature_demo(app.store,name),201)
                if len(parts)==4 and parts[:2]==['api','launches']:
                    key=parts[2]; action=parts[3]
                    if action=='delete':return self.send(app.store.delete(key,payload))
                    if action=='prepare':
                        ids=app.store.enqueue_all(key,payload);app.worker.wake.set();return self.send({'job_ids':ids},202)
                    if action=='actions': return self.send(app.store.mutate(key,payload))
                    if action=='jobs':
                        job=app.store.enqueue(key,payload); app.worker.wake.set()
                        return self.send({'job_id':job},202)
                    if action=='evidence':
                        p=app.evidence(chunk_id=clean(payload.get('chunk_id'),200))
                        payload.update(action='source_add',title=p['title']+' · '+p['document_id']+' · p'+str(p['page']),scope='shared',kind='public',text=p['text'],provenance={'document_id':p['document_id'],'chunk_id':p['id'],'page':p['page'],'source_url':p.get('source_url') or '', 'issue_date':p.get('issue_date') or ''})
                        return self.send(app.store.mutate(key,payload))
                self.send({'error':'Not found'},404)
            except PermissionError as exc: self.send({'error':str(exc)},403)
            except Conflict as exc: self.send({'error':str(exc)},409)
            except (ValueError,TypeError,KeyError,UnicodeDecodeError) as exc: self.send({'error':str(exc)},400)
            except Exception:
                logging.exception('Launch request failed'); self.send({'error':'Request failed. Check the server log; no successful update has been reported.'},500)

        def do_GET(self): self.route()
        def do_POST(self): self.route(True)
    return Handler


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--port',type=int,default=8766); parser.add_argument('--db',type=Path)
    args=parser.parse_args(); logging.basicConfig(level=logging.INFO)
    app=Application(args.db)
    # Bind before recovering jobs so a second process cannot interrupt the active worker.
    server=ThreadingHTTPServer(('127.0.0.1',args.port),handler_for(app)); app.worker.start()
    print(f'UPI Feature Workspace V2: http://127.0.0.1:{args.port}',flush=True)
    try: server.serve_forever()
    except KeyboardInterrupt: pass
    finally: server.server_close(); app.worker.stop()


if __name__=='__main__': main()
