t = int(input())
arr = []
for _ in range(t):
    arr.append(int(input()))
d = {}
for i in arr:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
for i in d.keys():
    for j in range(d[i]):
        print(i)
