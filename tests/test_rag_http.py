import http.client
import json
from http.server import ThreadingHTTPServer
import threading
from types import SimpleNamespace
import unittest
from app import Handler


class HTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        class QuietHandler(Handler):
            def log_message(self,*args):pass
        QuietHandler.engine=SimpleNamespace(stats=lambda:{'documents':0})
        QuietHandler.jobs=SimpleNamespace(answer=lambda payload:{'id':'fixture','status':'running'},
                                          get=lambda key:{'id':key,'status':'completed','result':{'claims':[]}})
        cls.server=ThreadingHTTPServer(('127.0.0.1',0),QuietHandler)
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown();cls.server.server_close();cls.thread.join()

    def request(self,method,path,payload=None,headers=None):
        conn=http.client.HTTPConnection('127.0.0.1',self.server.server_port,timeout=3)
        h={'Content-Type':'application/json'};h.update(headers or {})
        conn.request(method,path,json.dumps(payload) if payload is not None else None,h)
        response=conn.getresponse();body=response.read();status=response.status;conn.close()
        return status,json.loads(body)

    def test_answer_job_and_poll(self):
        self.assertEqual(self.request('POST','/api/answers',{'query':'test'})[0],202)
        status,result=self.request('GET','/api/jobs?id=fixture')
        self.assertEqual(status,200);self.assertEqual(result['status'],'completed')

    def test_cross_origin_intake_blocked(self):
        self.assertEqual(self.request('POST','/api/intake/upload',{}, {'Origin':'https://example.org'})[0],403)

    def test_nonlocal_host_blocked(self):
        self.assertEqual(self.request('GET','/api/stats',headers={'Host':'example.org'})[0],403)

    def test_form_post_not_accepted_as_json(self):
        self.assertEqual(self.request('POST','/api/answers',{}, {'Content-Type':'text/plain'})[0],415)
