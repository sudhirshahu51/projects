m = []
d = {}
p, q = map(int, input('Enter the order of matrix').split())
for i in range(p):
    m.append([])
    print('Enter the %s line of matrix' % i)
    for j in range(q):
        m[i].append((input()))
for i in range(p):
    for j in range(q):
        if m[i][j] in d.keys():
            d[m[i][j]] += 1
        else:
            d[m[i][j]] = 1
for i, v in d.items():
    print('%s   :%s' % (i, v))
