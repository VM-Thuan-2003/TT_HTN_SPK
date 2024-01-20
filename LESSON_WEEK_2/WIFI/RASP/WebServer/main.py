from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 5050

class Sever(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        if self.path == '/led/1/on':
            print("led 1 on")
            self.path = '/index.html'
        if self.path == '/led/1/off':
            print("led 1 off")
            self.path = '/index.html'
        if self.path == '/led/2/on':
            print("led 2 on")
            self.path = '/index.html'
        if self.path == '/led/2/off':
            print("led 2 off")
            self.path = '/index.html'
        if self.path == '/led/inv':
            print("led inv")
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

def main():
    try:
        server = HTTPServer(('127.0.0.1', PORT), Sever)
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
        
if __name__ == __name__:
    print("__start__")
    main()