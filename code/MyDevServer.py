import cgi
from sys import argv
from jinja2 import Template
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        aSelf = self
        from server import paths,args
        for path in paths:
            if(str(aSelf.path) == path):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(Template(open(paths[path], "r").read()).render(**args[paths[path]]),"UTF-8"))
    
    def do_POST(self):
        self.send_response(500)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        form = cgi.FieldStorage(fp=self.rfile,headers=self.headers,environ={'REQUEST_METHOD': 'POST'})
        aSelf = self
        from server import postPaths,postArgs
        for path in postPaths:
            if(str(aSelf.path) == path):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(Template(open(postPaths[path], "r").read()).render(**postArgs[postPaths[path]]),"UTF-8"))

if __name__ == "__main__":
    if argv[1] == "serve":
        from server import host, port
        print("\033[31mWARNING: THIS IS A DEVELOPMENT SERVER\033[0m")
        webServer = HTTPServer((host, port), MyServer)
        print("Server started http://%s:%s" % (host, port))

        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass

        webServer.server_close()
        print("Server stopped.")
        exit(0)