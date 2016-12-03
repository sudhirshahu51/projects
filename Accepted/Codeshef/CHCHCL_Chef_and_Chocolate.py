def odd(x):
    if x % 2 == 0:
        return False
    else:
        return True


def even(x):
    if x % 2 == 0:
        return True
    else:
        return False


x = int(input())
while x:
    n, m = map(int, input().split())
    if odd(n) and odd(m):
        print('No')
    else:
        print('Yes')
    x -= 1
