"""Local model HTTP requests with a connection-wide deadline.

The timer closes the actual socket, including stalled headers/body reads. It
cannot run while the OS suspends the process; late results are still rejected.
"""
import http.client
import json
import socket
import threading
import time
from urllib.parse import urlsplit


def local_json(url, payload=None, timeout=30):
    parsed=urlsplit(url)
    if (parsed.scheme!='http' or parsed.hostname not in ('127.0.0.1','localhost','::1')
            or parsed.username or parsed.password or parsed.fragment):
        raise ValueError('Local HTTP model endpoints only')
    if timeout<=0:raise TimeoutError('Model request budget exhausted')
    started=time.monotonic();expired=threading.Event()
    connection=http.client.HTTPConnection(parsed.hostname,parsed.port or 80,timeout=timeout)
    timer=None
    try:
        connection.connect()
        transport=connection.sock
        def cancel():
            expired.set()
            try:transport.shutdown(socket.SHUT_RDWR)
            except OSError:pass
            transport.close()
        remaining=timeout-(time.monotonic()-started)
        if remaining<=0:raise TimeoutError('Model connection exceeded its time budget')
        timer=threading.Timer(remaining,cancel);timer.daemon=True;timer.start()
        body=None if payload is None else json.dumps(payload).encode('utf-8')
        target=parsed.path or '/'
        if parsed.query:target+='?'+parsed.query
        connection.request('GET' if payload is None else 'POST',target,body,{'Content-Type':'application/json'})
        response=connection.getresponse()
        data=response.read()
        if expired.is_set() or time.monotonic()-started>timeout:
            raise TimeoutError('Model request exceeded its time budget')
        if response.status>=400:
            raise OSError(f'Local model HTTP {response.status}')
        return json.loads(data)
    except Exception as exc:
        if expired.is_set():raise TimeoutError('Model request exceeded its time budget') from exc
        raise
    finally:
        if timer is not None:
            timer.cancel();timer.join()
        connection.close()
