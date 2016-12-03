def fib(n):
    global look_up
    if n <= 1:
        look_up[n] = n
    elif look_up[n] is None:
        look_up[n] = fib(n - 1) + fib(n - 2)
    return look_up[n]


def subset(s):
    new = []
    for i in range(len(s)):
        for j in range(1, len(s)-i+1):
            tmp = s[:i]
            tmp.append(s[i+j-1])
            new.append(tmp)
    return f(new)


def f(s):
    for i in s:
        su = 0
        total = 0
        su = sum(i)
        total += fib(su)
        return total % 1000000007


look_up = [None]*( 100000000 + 1)
n, m = map(int, input().split())
a = list(map(int, input().split()))
for _ in range(m):
    c, x, y = input().split()
    x, y = int(x), int(y)
    subset(a[x-1:y])
    if c == 'C':
        a[x] = y
        print(a)
    if c == 'Q':
        print()