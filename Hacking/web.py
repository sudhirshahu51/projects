import os
import sys
sys.path.append('/usr/local/lib/python3.4/dist-packages')

from bs4 import BeautifulSoup
import urllib.request


def download_img(url, name):
    f_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, f_name)


def image(url='http://www.doujin-moe.us/g3kmbqn5', fodder='Folder_1', no=1):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent}
    print(url)
    request = urllib.request.Request(url, None, headers)
    source_code = urllib.request.urlopen(request)
    soup = BeautifulSoup(source_code, 'html.parser')
    i = 1
    os.mkdir('/home/devesh/images/%s' % fodder)
    os.chdir('/home/devesh/images/%s' % fodder)
    for gallery in soup.findAll('djm'):
        if i >= no:
            l = gallery.get('file')
            print(l)
            download_img(l, i)
        else:
            pass
        i += 1
u = input('Enter the url')
f = input('Enter the folder name')
p = int(input('Enter the page no.'))
image(u, f, p)

