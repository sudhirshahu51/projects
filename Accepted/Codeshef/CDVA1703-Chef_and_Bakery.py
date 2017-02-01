t = int(input())
while t:
    n, x = map(int, input().split())
    tmp = n % x
    if tmp != 0:
        print(tmp)
    else:
        print(x)
    t -= 1
