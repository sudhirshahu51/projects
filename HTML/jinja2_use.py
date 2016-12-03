import sys
sys.path.append('/usr/local/lib/python3.4/dist-packages')
import jinja2
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi


template_dir = os.path.join(os.path.dirname(__file__), 'template')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))


class Handler(BaseHTTPRequestHandler):
    def write(self, *a, **kw):
        self.wfile.write(*a, **kw)

    def render_str(self, template, **param):
        t = jinja_env.get_template(template)
        return t.render(param)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
