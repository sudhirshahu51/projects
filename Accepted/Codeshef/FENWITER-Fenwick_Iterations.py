def f_down(i): return i & (i + 1)


t = int(input())
while t:
    l1, l2, l3, n = input().split()
    n = int(n)
    l = int(l1 + l2 * n + l3, base=2)
    access = 1
    tmp = f_down(l) - 1
    while tmp >= 0:
        access += 1
        tmp = f_down(tmp) - 1
    print(access)
    t -= 1
