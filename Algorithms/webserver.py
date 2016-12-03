from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi


class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/hello'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = '<html><bodye>'
                output += 'hello'
                output += "<form method='POSt' enctype='multipart/form-data' action='/hello'>" \
                          "<h2> What would you like me to say?</h2><input name='message' type='text'>" \
                          "<input type='submit' value='Submit' </form>"
                output += "</body></html>"
                self.wfile.write(output.encode('utf-8'))
                print(output)
                return
            if self.path.endswith('/hola'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = '<html><body>'
                output += 'hello'
                output += "<form method='POSt' enctype='multipart/form-data' action='/hello'>" \
                          "<h2> What would you like me to say?</h2><input name='message' type='text'>" \
                          "<input type='submit' value='Submit' </form>"
                output += "</body></html>"
                self.wfile.write(output.encode('utf-8'))
                print(output)
                return
        except IOError:
            self.send_error(404, 'file not found')

    def do_POST(self):
        self.send_response(301)
        self.end_headers()
        ctype, pdict = cgi.parse_header(self.headers['content-type'])
        pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
        if ctype == 'multipart/form-data':
            fields = cgi.parse_multipart(self.rfile, pdict)
            messagecontent = fields.get('message')
        output = "<html><body>"
        output += "<h1>how about this<h1>"
        output += "<h1> %s <h2>" % messagecontent[0].decode('utf-8')
        output += "<form method='POSt' enctype='multipart/form-data' action='/hello'><h2>" \
                  " What would you like me to say?</h2><input name='message' type='text'>" \
                  "<input type='submit' value='Submit' </form>"
        self.wfile.write(output.encode('utf-8'))
        print(output)
def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print('HTTP Server started')
        server.serve_forever()
    except KeyboardInterrupt:
        print('server is closed')
        server.socket.close()


if __name__ == '__main__':
    main()
