def fib(n):
    global look_up
    if n <= 1:
        look_up[n] = n
    elif look_up[n] is None:
        look_up[n] = fib(n - 1) + fib(n - 2)
    return look_up[n]


look_up = [None]*1000000
test = int(input())
for _ in range(test):
    a, b = map(int, input().split())
