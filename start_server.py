#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.request import urlopen

host = "localhost"
port = 8000

class TimetableHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="site", **kwargs)

    def do_GET(self):
        if self.path.startswith("/qvpublic"):
            self.send_response(200)
            self.end_headers()
            self.copyfile(urlopen("https://qutvirtual3.qut.edu.au" + self.path), self.wfile)
        else:
            # Serve directory
            super().do_GET()

httpd = HTTPServer((host, port), TimetableHandler)
print(f"Serving HTTP on {httpd.server_name} port {httpd.server_port} (http://{httpd.server_name}:{httpd.server_port}/) ...")
httpd.serve_forever()
