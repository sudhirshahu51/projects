class Person:
    def __init__(self, n):
        self.name = n
        self.knows = {self}
        self.frnd = {self}
        self.tr = {n}
        self.group = None

    def know(self, nbr):            # To add the nbr in knows list of the person where nbr is Person
        self.knows.add(nbr)

    def friend(self, nbr):          # To add nbr as the friend of self
        self.frnd.add(nbr)


def friends(a, b):
    if not isinstance(a, Person) and isinstance(b, Person):
        return
    if a in b.knows:
        b.friend(a)
    else:
        for x in b.frnd:
            if a in x.knows:
                b.friend(a)
                break


def true(a, b):
    if not isinstance(a, Person) and isinstance(b, Person):
        return
    if a in b.frnd and b in a.frnd:
        b.tr.add(a.name)
        a.tr.add(b.name)


for _ in range(int(input())):
    n = []
    d = {}
    y = int(input())
    for j in range(y):
        d[j+1] = Person(j+1)
    for i in range(y):
        c = 0
        for k in list(input()):
            if k == 'Y':
                d[i+1].know(d[c+1])
            c += 1
    for i in range(y):
        c = 0
        for k in range(y):
            friends(d[i+1], d[k+1])
    for i in range(y):
        c = 0
        for k in range(y):
            true(d[i+1], d[k+1])
    for i, v in d.items():
        tup = []
        for j in v.tr:
            tup += [d[j].tr]
        print(tup)
        print('he',d[i].tr.intersection(*tup))
