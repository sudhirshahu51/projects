data = {}
n, q = map(int, input().split())
for i in range(1, n + 1):
    data[i] = 0
for _ in range(q):
    put = input()
    l = put.split()
    l[1], l[2] = int(l[1]), int(l[2])
    if l[0] == 'add':
        data[l[1]] += l[2]
    if l[0] == 'find':
        add = 0
        for i in range(l[1], l[2] + 1):
            add += data[i]
        print(add)
