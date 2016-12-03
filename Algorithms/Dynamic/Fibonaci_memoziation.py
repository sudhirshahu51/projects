def fib(n):
    global look_up
    if n <= 1:
        look_up[n] = n
    elif look_up[n] is None:
        look_up[n] = fib(n - 1) + fib(n - 2)
    return look_up[n]

look_up = [None]*(x + 1)
x = int(input('Enter the integer'))
print(fib(x))
