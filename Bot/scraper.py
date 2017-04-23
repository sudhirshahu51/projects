import csv
from bs4 import BeautifulSoup
import urllib.request
import time
import datetime


def amount(s):
    t = s.find('(')
    return s[t+1:-1]


def vol(s):
    t = s.find('(')
    return s[0:t]


def data(writer, url='http://www.bitcoinrates.in/'):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent}
    request = urllib.request.Request(url, None, headers)
    source_code = urllib.request.urlopen(request)
    soup = BeautifulSoup(source_code, 'html.parser')
    t = soup.find_all('table')[1]
    t = t.find('tbody')
    for i in t.find_all('tr'):
        if 'CoinSecure' in str(i):
            td = i.find_all('td')
            if len(td) == 6:
                print('exchange:', td[0].get_text(),
                      'buy:', vol(td[4].get_text()), amount(td[4].get_text()),
                      'sell:', vol(td[5].get_text()), amount(td[5].get_text()))
                writer['coinsecure'].writerow([vol(td[4].get_text()), amount(td[4].get_text()),
                                               vol(td[5].get_text()), amount(td[5].get_text()),
                                               datetime.datetime.now()])
        if 'LocalBitcoins' in str(i):
            td = i.find_all('td')
            if len(td) == 6:
                print('exchange:', td[0].get_text(),
                      'buy:', vol(td[4].get_text()), amount(td[4].get_text()),
                      'sell:', vol(td[5].get_text()), amount(td[5].get_text()))
                writer['localbitcoin'].writerow([vol(td[4].get_text()), amount(td[4].get_text()),
                                               vol(td[5].get_text()), amount(td[5].get_text()),
                                                 datetime.datetime.now()])
        if 'Unocoin' in str(i):
            td = i.find_all('td')
            if len(td) == 6:
                print('exchange:', td[0].get_text(),
                      'buy:', vol(td[4].get_text()), amount(td[4].get_text()),
                      'sell:', vol(td[5].get_text()), amount(td[5].get_text()))
                writer['unocoin'].writerow([vol(td[4].get_text()), amount(td[4].get_text()),
                                               vol(td[5].get_text()), amount(td[5].get_text()),
                                            datetime.datetime.now()])
        if 'Zebpay' in str(i):
            td = i.find_all('td')
            if len(td) == 6:
                print('exchange:', td[0].get_text(),
                      'buy:', vol(td[4].get_text()), amount(td[4].get_text()),
                      'sell:', vol(td[5].get_text()), amount(td[5].get_text()))
                writer['zebpay'].writerow([vol(td[4].get_text()), amount(td[4].get_text()),
                                               vol(td[5].get_text()), amount(td[5].get_text()),
                                           datetime.datetime.now()])
        if 'Bitxoxo' in str(i):
            td = i.find_all('td')
            if len(td) == 6:
                print('exchange:', td[0].get_text(),
                      'buy:', vol(td[4].get_text()), amount(td[4].get_text()),
                      'sell:', vol(td[5].get_text()), amount(td[5].get_text()))
                writer['bitxoxo'].writerow([vol(td[4].get_text()), amount(td[4].get_text()),
                                               vol(td[5].get_text()), amount(td[5].get_text()),
                                            datetime.datetime.now()])


if __name__ == "__main__":
    try:
        writer = {}
        coinsecure = open('coinsecure.csv', 'a', newline='')
        writer['coinsecure'] = csv.writer(coinsecure)
        localbitcoin = open('localbitcoin.csv', 'a', newline='')
        writer['localbitcoin'] = csv.writer(localbitcoin)
        unocoin = open('unocoin.csv', 'a', newline='')
        writer['unocoin'] = csv.writer(unocoin)
        zebpay = open('zebpay.csv', 'a', newline='')
        writer['zebpay'] = csv.writer(zebpay)
        bitxoxo = open('bitxoxo.csv', 'a', newline='')
        writer['bitxoxo'] = csv.writer(bitxoxo)
        try:
            while True:
                data(writer)
                time.sleep(60)
        except (KeyboardInterrupt, SystemExit, SystemError):
            coinsecure.close()
            localbitcoin.close()
            unocoin.close()
            zebpay.close()
            bitxoxo.close()
    except Exception as e:
        print(e)
