t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    avg = 0.0
    if k == 0:
        s = sum(l)
        avg = s/len(l)
    else:
        new = l[k:-k]
        s = sum(new)
        avg = s/len(new)
    print('%.6f'%avg)
