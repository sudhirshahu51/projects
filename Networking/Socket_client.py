from socket import *


s = socket(AF_INET, SOCK_STREAM)
s.connect(("www.google.co.in", 80))
print('Connection established')
s.send(b"'GET / HTTP/1.1\r\n''Host: google.com\r\n'"
       b"User-Agent: 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'\r\n'")
print('request send')
data = s.recv(1000)
print('reciving complete')
print(data)
s.close()
