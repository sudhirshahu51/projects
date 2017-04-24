'''Import Statements'''
from twitter import *
from bs4 import BeautifulSoup
import urllib.request
import time
import oauth2
import _thread
import pickle
import sys


class Queue:
    def __init__(self):
        self.items = []

    def __contains__(self, item):
        return item in self.items

    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.insert(0, data)

    def de_queue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def front(self):
        return self.items[-1]

    def rare(self):
        return self.items[0]


class TwitterAccount:
    def __init__(self, name, acc_key, acc_secret, cons_key, cons_secret, tag_acc=[], via_acc=[], sec=0):
        self.access_token = acc_key
        self.access_token_secret = acc_secret
        self.consumer_key = cons_key
        self.consumer_key_secret = cons_secret
        self.tag_acc = tag_acc
        self.via_acc = via_acc
        self.name = name
        self.sec = sec

    def post(self, text):
        if isinstance(text, str):
            pass
        else:
            print('text entered is not valid')
            return False
        t = Twitter(auth=OAuth(self.access_token, self.access_token_secret, self.consumer_key, self.consumer_key_secret))
        try:
            reply = t.statuses.update(status=text)
            post_id = reply['id']
            print('Tweet Successful from', self.name)
            return post_id
        except Exception as e:
            print(self.name, '\n', e)
            return False

    def like(self, post_id, post_body=''):
        url = 'https://api.twitter.com/1.1/favorites/create.json?id=' + str(post_id).strip()
        consumer = oauth2.Consumer(key=self.consumer_key, secret=self.consumer_key_secret)
        token = oauth2.Token(key=self.access_token, secret=self.access_token_secret)
        client = oauth2.Client(consumer, token)
        try:
            client.request(url, method="POST", body=post_body.encode('utf-8'), headers=None)
            print('like successful ', self.name)
        except Exception as e:
            print(self.name, '\n', e)

    def re_tweet(self, post_id, post_body=''):
        url = 'https://api.twitter.com/1.1/statuses/retweet/%s.json' % str(post_id).strip()
        consumer = oauth2.Consumer(key=self.consumer_key, secret=self.consumer_key_secret)
        token = oauth2.Token(key=self.access_token, secret=self.access_token_secret)
        client = oauth2.Client(consumer, token)
        try:
            client.request(url, method="POST", body=post_body.encode('utf-8'), headers=None)
            print('retweet succesfull ', self.name,)
        except Exception as e:
            print(self.name, '\n', e)

    def content(self, tup):
        link, title = tup[0], tup[1]
        title_1 = title.lower()
        post_tag = []           # those are really going to be in the tweet
        post_via = []
        for i in tag:
            if i in title_1:
                post_tag.append(i)
        for i in via:
            if i.lower in title_1:
                post_via.append(i)
        # tags are included accordingly
        tmp = ' '
        for i in range(len(post_tag)):
            tmp += ' #'+post_tag[i]
        tmp1 = ''
        for i in self.tag_acc:
            if i not in tmp:
                tmp1 += ' #'+i
        tmp += tmp1
        for i in range(len(post_via)):
            tmp += ' @'+post_via[i]
        tmp1 = ''
        for i in self.via_acc:
            if i not in tmp:
                tmp1 += ' @'+i
        tmp += tmp1
        final = title + '. ' + link + tmp
        if len(title + '. ' + tmp) + 27 <= 140:
            pass
        else:
            title_1_list = title_1.split()
            title_list = title.split()
            for i in range(len(title_1_list)):
                if title_1_list[i] in tag:
                    title_list[i] = '#'+title_1_list[i]
            title = ' '.join(title_list)
            tmp = ' '
            for i in self.tag_acc:
                if i not in title:
                    tmp += ' #' + i
            for i in self.via_acc:
                if i not in title:
                    tmp += ' @' + i
            final = title + '. ' + link + tmp
        return final


def thread(acc, func, que, lock, file, post):
    while thread_running[acc.name] == 'start':
        if func == 'tweet':
            time.sleep(acc.sec)
            try:
                lock.acquire(1)
                try:
                    queue = pickle.load(open(file, "rb"))
                except Exception as e:
                    print('error in loading post')
                    print(e)
                    queue = que
                lock.release()
                thread_dic.acquire(1)
                try:
                    post_dic = pickle.load(open('post.p', "rb"))
                except Exception as e:
                    print('error in loading post')
                    print(e)
                    post_dic = post
                thread_dic.release()
                if queue.size() != 0:
                    tmp_id = queue.de_queue()
                    lock.acquire(1)
                    try:
                        pickle.dump(queue, open(file, "wb"))
                    except Exception as e:
                        print('error in dumbing', queue)
                        print(e)
                        pass
                    lock.release()
                    tmp_post = post_dic[tmp_id]
                    acc.post(acc.content(tmp_post))
                else:
                    pass
            except (KeyboardInterrupt, SystemExit):
                break
        elif func == 'retweet':
            time.sleep(acc.sec)
            try:
                lock.acquire(1)
                try:
                    queue = pickle.load(open(file, "rb"))
                except Exception as e:
                    print('error in loading post')
                    print(e)
                    queue = que
                lock.release()
                if queue.size() != 0:
                    tmp_id = queue.de_queue()
                    lock.acquire(1)
                    try:
                        pickle.dump(queue, open(file, "wb"))
                    except Exception as e:
                        print('error in dumbing', queue)
                        print(e)
                        pass
                    lock.release()
                    acc.re_tweet(tmp_id)
                else:
                    pass
            except (KeyboardInterrupt, SystemExit):
                break
    thread_running[acc.name] = 'end'


def crawler(no):
    url = 'http://www.bchaintalk.org/'
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent}
    request = urllib.request.Request(url+no, None, headers)
    source_code = urllib.request.urlopen(request)
    soup = BeautifulSoup(source_code, 'html.parser')
    t = soup.find_all("link")
    link = t[0].get('href').strip()
    if no not in link:
        return False
    request = urllib.request.Request(link, None, headers)
    source_code = urllib.request.urlopen(request)
    soup = BeautifulSoup(source_code, 'html.parser')
    t = soup.find_all("h1", {'class': 'page-title'})
    title = t[0].text
    return link, title


def cron():
    no = int(input('enter the post no.'))
    while True:
        print('working')
        t = crawler('t'+str(no)+'-')
        if t:
            id_post = bchaintalk.post(bchaintalk.content(t))
            if id_post:
                post_dic[id_post] = t
                if isinstance(id_post, int):
                    thread_dic.acquire(1)
                    pickle.dump(post_dic, open("post.p", "wb"))
                    thread_dic.release()
                q1.enqueue(id_post)
                thread_lock_1.acquire(1)
                pickle.dump(q1, open("q1.p", "wb"))
                thread_lock_1.release()
                q2.enqueue(id_post)
                thread_lock_2.acquire(1)
                pickle.dump(q1, open("q2.p", "wb"))
                thread_lock_2.release()
                q3.enqueue(id_post)
                bchaintalk.like(id_post)
                boy_bitcoin.like(id_post)
                Sumantsinha6.like(id_post)
            no += 1
        else:
            print('sleeping')
        time.sleep(600)


if __name__ == "__main__":
    '''global variables'''
    tag = ['blockchain', 'bitcoin', 'porsche', 'fintech', 'banking', 'swift', 'ponzi', 'hacking', 'burrow', 'scam',
         'hyperledger', 'oscar', 'ibm']
    via = []
    thread_running = {}
    try:
        q1 = pickle.load(open('q1.p', 'rb'))
    except:
        q1 = Queue()
    thread_lock_1 = _thread.allocate_lock()
    try:
        q2 = pickle.load(open('q2.p', 'rb'))
    except:
        q2 = Queue()
    thread_lock_2 = _thread.allocate_lock()
    try:
        q3 = pickle.load(open('q3.p', 'rb'))
    except:
        q3 = Queue()
    try:
        post_dic = pickle.load(open('post.p', 'rb'))
    except:
        post_dic = {}
    thread_dic = _thread.allocate_lock()
    bchaintalk = TwitterAccount(name='bchaintalk', acc_key='852985908446056448-GQM3S51qlNRq0GgBq2fVa5Dl1P74lzv',
                                acc_secret='A8NK57cbHYU2DVVagSbTcUZVHGh7e9q6Gnpho6ckVPZQ4',
                                cons_key='knDNoTeBHbkm773wvRF1OWTdr',
                                cons_secret='r4wsmgc8yaHErCf2tII3QKiGUyGzg0l5TAlYF2FgIJCCkMZwdp',
                                tag_acc=['blockchain'], sec=0)
    boy_bitcoin = TwitterAccount(name='boy_bitcoin', acc_key='823858543610753024-ziDCtVTwcBXt2NsnzNiUPpNYxZrrA7b',
                                acc_secret='HARUAfqC4S650oc9Ce0rJKDG2pqeaafcTpTt3rBfF7XVW',
                                cons_key='kOvFRc1d6pcjJcgjlbqSEr5eq',
                                cons_secret='Kz1ITH7Msrn0mMv7PSspqnafsH1P36cAJXyD6qUBqp2MExcSMH',
                                 tag_acc=['bchaintalk'], via_acc=['BchainTalk'], sec=3)
    Sumantsinha6 = TwitterAccount(name='Sumantsinha6', acc_key='849963540450508801-L3jaoInkjHdJc398IYlojyuHSYTOfNE',
                                acc_secret='RIbgmKT1zn11OgsTvKiYYQavPNPJ8ma4AisN3hh7ukCGR',
                                cons_key='YR6g3BHUcsZALvSh5u6sn02jJ',
                                cons_secret='94xIICOYGvzCch3CB3RHNGIiJoLLYbGG7QS4xv9N4LB3tw1L3F',
                                tag_acc=['blockchain'], via_acc=['BchainTalk'], sec=2)
    try:
        _thread.start_new_thread(thread, (boy_bitcoin, 'tweet', q1, thread_lock_1, "q1.p", post_dic,))
        thread_running[boy_bitcoin.name] = 'start'
        _thread.start_new_thread(thread, (Sumantsinha6, 'retweet', q2, thread_lock_2, "q2.p", post_dic,))
        thread_running[Sumantsinha6.name] = 'start'
        cron()
        while True:
            if 'start' in thread_running.values():
                pass
            else:
                break
    except (KeyboardInterrupt, SystemExit):
        sys.exit()

