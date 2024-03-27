from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, world!")

# Create an HTTP server
httpd = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
print("http Server started on port 8000...")
httpd.serve_forever()
