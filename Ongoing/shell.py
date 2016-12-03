import random
lst = []
ls = []
n = int(input())
m = int(input())
for i in range(n):
    ls.append(str(random.randint(1, 1000000)))
print('1')
print(n, m)
print(' '.join(ls))
for i in range(m):
    a = (random.randint(1, n))
    b = (random.randint(1, n))
    if a > b:
        a, b = b, a
    lst.append([str(random.randint(0, 1)), str(a), str(b)])
for i in lst:
    print(' '.join(i))