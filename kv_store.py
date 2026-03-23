#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json, threading, time

store = {}
lock = threading.Lock()

def cleanup():
    while True:
        time.sleep(300)
        cutoff = time.time() - 1800
        with lock:
            expired = [k for k, v in store.items() if v.get('_ts', 0) < cutoff]
            for k in expired:
                del store[k]

threading.Thread(target=cleanup, daemon=True).start()

class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_POST(self):
        l = int(self.headers.get('Content-Length', 0))
        b = json.loads(self.rfile.read(l)) if l > 0 else {}
        k, v = b.get('key',''), b.get('value',{})
        if k:
            with lock:
                v['_ts'] = time.time()
                store[k] = v
        self.send_response(200)
        self.send_header('Content-Type','application/json')
        self.end_headers()
        self.wfile.write(b'{"ok":true}')
    def do_GET(self):
        qs = parse_qs(urlparse(self.path).query)
        k = qs.get('key',[''])[0]
        with lock:
            v = store.get(k)
        self.send_response(200)
        self.send_header('Content-Type','application/json')
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()
        if v:
            r = {x:y for x,y in v.items() if x != '_ts'}
            self.wfile.write(json.dumps(r).encode())
        else:
            self.wfile.write(b'{"status":"processing"}')
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin','*')
        self.send_header('Access-Control-Allow-Methods','GET,POST,OPTIONS')
        self.send_header('Access-Control-Allow-Headers','Content-Type')
        self.end_headers()

HTTPServer(('0.0.0.0',3456),H).serve_forever()
