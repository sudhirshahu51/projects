import pickle

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


t1 = pickle.load(open('q1.p', 'rb'))
t2 = pickle.load(open('q2.p', 'rb'))
t3 = pickle.load(open('post.p', 'rb'))


print(t1.items)
print(t2.items)
for i, v in t3.items():
    print(i, v, sep=': ')
    print()
