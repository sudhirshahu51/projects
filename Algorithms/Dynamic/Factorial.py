def fac(n):
    global table
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i - 1] * i
    return table[n]


x = int(input('Enter the integer'))
table = [None]*(x + 1)