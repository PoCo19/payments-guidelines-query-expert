import json
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from model_transport import local_json


class Handler(BaseHTTPRequestHandler):
    def log_message(self,*args):pass
    def do_GET(self):
        if self.path=='/headers':time.sleep(.6)
        try:
            self.send_response(200);self.end_headers()
            if self.path=='/trickle':
                for _ in range(30):
                    self.wfile.write(b' ');self.wfile.flush();time.sleep(.03)
            self.wfile.write(json.dumps({'ok':True}).encode())
        except OSError:pass


class TransportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()
        cls.url=f'http://127.0.0.1:{cls.server.server_port}'
    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown();cls.server.server_close();cls.thread.join()
    def test_normal_response(self):self.assertEqual(local_json(self.url,timeout=2),{'ok':True})
    def test_stalled_headers_and_trickling_body_have_total_deadline(self):
        for path in ('/headers','/trickle'):
            with self.subTest(path=path):
                start=time.monotonic()
                with self.assertRaises((TimeoutError,)):local_json(self.url+path,timeout=.15)
                self.assertLess(time.monotonic()-start,.5)
    def test_failed_request_does_not_block_next_request(self):
        with self.assertRaises(TimeoutError):local_json(self.url+'/trickle',timeout=.1)
        self.assertTrue(local_json(self.url,timeout=2)['ok'])
    def test_rejects_remote_or_credentialed_urls(self):
        for url in ('https://127.0.0.1/','http://example.org/','http://user:secret@localhost/'):
            with self.assertRaises(ValueError):local_json(url)
