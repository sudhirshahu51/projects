from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
Data_session = sessionmaker(bind=engine)
session = Data_session()


class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/restaurant'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = '<html><body>'
                output += '<h1>Bellow are the Restaurants</h1>'
                for i in session.query(Restaurant).all():
                    output += '<h3> %s </h3>' % i.name
                    tmp = i.id
                    lis = session.query(MenuItem).filter_by(restaurant_id=tmp)
                    for j in lis:
                        output += '<p> %s </p>' % j.name
                        output += '<p> %s </p>' % j.price
                    output += "<a href='/restaurant/%s/delete'>delete </a>" % tmp
                    output += "<a href='/restaurant/%s/edit'> edit</a>" % tmp
                    output += '\n\n'
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurant'>" \
                          "<h2> Add your restaurant</h2><input name='message' type='text'>" \
                          "<input type='submit' value='Submit'> </form>"
                output += "</body></html>"
                self.wfile.write(output.encode('utf-8'))
                print(output)
                return
            if self.path.endswith('/edit'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                rest_id = self.path.split('/')[2]
                rest_query = session.query(MenuItem).filter_by(restaurant_id=rest_id)
                print(rest_id)
                if rest_query is not []:
                    output = '<html><body>'
                    output += '<h1>New restaurant name </h1>'
                    output += "<form method='POST' enctype='multipart/form-data' " \
                              "action='/restaurant/%s/edit'>" % rest_id
                    output += "<input name= 'restaurant_name' type='text'>" % rest_query
                    output += "<input type='submit' value='Rename'>"
                    output += "</form></body></html>"
                    self.wfile.write(output.encode('utf-8'))
                    print(output)
            if self.path.endswith('/delete'):
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                rest_id = self.path.split('/')[2]
                rest_query = session.query(MenuItem).filter_by(restaurant_id=rest_id)
                print(rest_id)
                output = '<html><body>'
                output += "Are you sure to delete"
                output += "<form method='POSt' enctype='multipart/form-data' action='/restaurant/%s/delete'>"% rest_id
                output += "<h2> Are you sure to delete the restaurant?</h2>" \
                          "<input type='submit' value='Delete' ></form>"
                output += "</body></html>"
                self.wfile.write(output.encode('utf-8'))
                print(output)
                return
        except IOError:
            self.send_error(404, 'file not found')

    def do_POST(self):
        if self.path.endswith('/restaurant'):
            ctype, pdict = cgi.parse_header(self.headers['content-type'])
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')
            print(messagecontent[0])
            session.add(Restaurant(name=messagecontent[0].decode('utf-8')))
            session.commit()
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.send_header('Location', '/restaurant')
            self.end_headers()
        if self.path.endswith('/edit'):
            rest_id = self.path.split('/')[2]
            ctype, pdict = cgi.parse_header(self.headers['content-type'])
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                new_name = fields.get('restaurant_name')
                rest_query = session.query(Restaurant).filter_by(id=rest_id).one()
            print('the query is', rest_id)
            if rest_query is not []:
                rest_query.name = new_name[0].decode('utf-8')
                session.add(rest_query)
                session.commit()
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurant')
                self.end_headers()
        if self.path.endswith('/delete'):
            rest_id = self.path.split('/')[2]
            ctype, pdict = cgi.parse_header(self.headers['content-type'])
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                new_name = fields.get('restaurant_name')
                rest_query = session.query(Restaurant).filter_by(id=rest_id).one()
            print('the query is', rest_id)
            if rest_query is not []:
                session.delete(rest_query)
                session.commit()
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurant')
                self.end_headers()



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
