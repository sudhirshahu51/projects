"""Script server based on SimpleHTTPServer

Handles GET and POST requests, in-memory session management,
HTTP redirection

Python scripts are executed in a namespace made of :
- request : for the data received from the query string or the request body. 
            Calling 'http://host/myScript.py?foo=bar' will make 
            request = {'foo':['bar']} available in the namespace of myScript
- headers : the http request headers
- resp_headers : the http response headers
- Session() : a function returning the session object
- HTTP_REDIRECTION : an exception to raise if the script wants to redirect
to a specified URL (raise HTTP_REDIRECTION, url)

A simple templating system is provided, using the Python string substitution
mechanism introduced in Python 2.4 (syntax $name). Template files must have
the extension .tpl

Hello world programs : will print "Hello world !" if called with the query
string ?name=world
- hello.py (Python script) [ http://localhost/hello.py?name=world ]
   print "Hello",request['name'][0],"!"
- hello.tpl (template)  [ http://localhost/hello.tpl?name=world ]
   Hello $name !

Other extensions can be handled by adding methods self.run_(extension)
"""

import sys
import os
import string
import cStringIO
import random
import cgi
import select
import SimpleHTTPServer
import Cookie
