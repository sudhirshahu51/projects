def gcd(x, y):
    if x == 0:
        return y
    else:
        return gcd(y % x, x)


n = int(input())
for _ in range(n):
    f2 = 0
    f5 = 0
    a = input()
    if a.find('.') == -1:
        print('1')
    else:
        n = len(a) - a.find('.') - 1
        a1 = int(a[:int(a.find('.'))] + a[int(a.find('.') + 1):])
        j = gcd(10**n, a1)
        print(10**n//j)
