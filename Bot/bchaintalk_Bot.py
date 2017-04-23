import requests
from bs4 import BeautifulSoup


session_requests = requests.session()
login_url = "http://www.bchaintalk.org/login"
URL = "http://www.bchaintalk.org/"

payload = {
    'username': "henry2",
    'password': "21wallstreet",
}
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent': user_agent, 'referer': login_url}
with session_requests as session:
    

    result = session.post(login_url, data=payload, headers={'User-Agent': user_agent, 'referer': login_url})
    print(result.headers)
    print(result.status_code)
    print(result.url)
    print(dir(result))
    print(result.cookies.items())
    soup = BeautifulSoup(result.content, 'html.parser')
    #print(soup.prettify())
    url = 'http://www.bchaintalk.org'
    result = session.get(url, headers={'User-Agent': user_agent, 'referer': url})
    soup = BeautifulSoup(result.content, 'html.parser')
    t = soup.find_all('form')
    '''print(len(t))
    for i in t:
        print('\n\n\n\n\n')
        print(i.prettify())
'''