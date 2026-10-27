"""Real localhost HTTP routing with synthetic evidence, no model or corpus writes."""
import json
import threading
import time
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from app import Handler
from local_jobs import LocalJobs
from tests import test_work_items as fixture


class WorkAPITests(unittest.TestCase):
    def setUp(self):
        fixture.WorkTests.setUp(self)
        class QuietHandler(Handler):
            def log_message(self,*args):pass
        QuietHandler.engine=self.engine
        QuietHandler.work=self.store
        QuietHandler.jobs=LocalJobs(lambda:self.engine,lambda e:None,self.path.parent/'config.json')
        self.server=ThreadingHTTPServer(('127.0.0.1',0),QuietHandler)
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        threading.Thread(target=self.server.serve_forever,daemon=True).start()
        self.base='http://127.0.0.1:'+str(self.server.server_port)

    def request(self,path,payload=None,headers=None):
        raw=None if payload is None else json.dumps(payload).encode()
        req=urllib.request.Request(self.base+path,data=raw,headers=headers or {'Content-Type':'application/json'})
        try:
            with urllib.request.urlopen(req,timeout=5) as r:return r.status,r.read(),r.headers
        except urllib.error.HTTPError as exc:return exc.code,exc.read(),exc.headers

    def test_create_generate_submit_export_http_journey(self):
        code,raw,_=self.request('/api/work-create',dict(query='Who qualifies?'))
        self.assertEqual(code,200);item=json.loads(raw)
        code,raw,_=self.request('/api/work-generate',dict(id=item['id'],revision=item['revision']))
        self.assertEqual(code,202);job=json.loads(raw)
        for _ in range(100):
            _,raw,_=self.request('/api/jobs?id='+job['id']);job=json.loads(raw)
            if job['status'] in ('completed','failed'):break
            time.sleep(.01)
        self.assertEqual(job['status'],'completed')
        item=job['result']
        code,raw,_=self.request('/api/work-review',dict(id=item['id'],revision=item['revision'],decision='submit'))
        self.assertEqual(code,200);self.assertEqual(json.loads(raw)['state'],'Needs review')
        code,raw,headers=self.request('/api/work-export?id='+item['id'])
        self.assertEqual(code,200);self.assertIn('text/markdown',headers['Content-Type'])
        self.assertIn(b'Needs review',raw);self.assertIn(b'[S1]',raw)

    def test_reject_cross_origin_non_json_and_invalid_ids(self):
        for headers,expected in [
            ({'Content-Type':'application/json','Origin':'https://unrelated.example'},403),
            ({'Content-Type':'text/plain'},415),
            ({'Content-Type':'application/json','Host':'unrelated.example'},403)]:
            with self.subTest(headers=headers):
                self.assertEqual(self.request('/api/work-create',dict(query='Who qualifies?'),headers)[0],expected)
        self.assertEqual(self.request('/api/work-item?id=missing')[0],400)
        self.assertEqual(self.request('/api/work-create',['not','object'])[0],400)

    def test_research_handoff_ignores_browser_supplied_evidence(self):
        _,raw,_=self.request('/api/answers',dict(query='Who qualifies?',mode='generate',scope='strict'))
        job=json.loads(raw)
        for _ in range(100):
            _,raw,_=self.request('/api/jobs?id='+job['id']);job=json.loads(raw)
            if job['status'] in ('completed','failed'):break
            time.sleep(.01)
        self.assertEqual(job['status'],'completed')
        code,raw,_=self.request('/api/work-import',dict(job_id=job['id'],text='Forged answer',result={'sources':[]}))
        self.assertEqual(code,200);item=json.loads(raw)
        self.assertIn('Only verified merchants',item['draft']['text'])
        self.assertNotIn('Forged',item['draft']['text'])
        self.assertEqual(item['draft']['origin_request']['scope'],'strict')
        code,raw,_=self.request('/api/work-visibility',dict(id=item['id'],revision=item['revision'],disposition='trash'))
        self.assertEqual(code,200);self.assertEqual(json.loads(raw)['disposition'],'trash')
        self.assertEqual(self.request('/api/work-import',dict(job_id='missing'))[0],400)

    def test_product_routes_and_related_identifier(self):
        for path in ('/work','/work?kind=query','/work?kind=impact','/work.css','/work.js'):
            self.assertEqual(self.request(path)[0],200,path)
        self.engine.by_id['long-id']=dict(id='long-id',availability='converted')
        self.assertEqual(self.request('/api/work-related?id=long-id')[0],200)
        self.assertEqual(self.request('/api/work-related?id=missing')[0],400)


if __name__=='__main__':unittest.main()
