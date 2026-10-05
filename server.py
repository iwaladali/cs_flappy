import http.server, socketserver, webbrowser, mimetypes
mimetypes.add_type('application/wasm', '.wasm')
mimetypes.add_type('text/javascript', '.js')
PORT = 8000
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store'); super().end_headers()
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), H) as s:
    print(f"Open http://localhost:{PORT}  (Ctrl+C to stop)")
    webbrowser.open(f"http://localhost:{PORT}")
    s.serve_forever()
