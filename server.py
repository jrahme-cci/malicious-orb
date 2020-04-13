from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

PORT = 5253

FILENAME = "h4ck3d_v4rs"

class Handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        with open(FILENAME, "w") as f:
            f.write(body.decode("utf-8"))

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        with open(FILENAME, 'r') as f:
            self.wfile.write(bytes(f.read(), 'utf-8'))
    def do_HEAD(self):
        self.send_response(200)

httpd = HTTPServer(('127.0.0.1', PORT), Handler)
httpd.serve_forever()
