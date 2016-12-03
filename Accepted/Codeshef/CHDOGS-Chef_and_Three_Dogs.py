t = int(input())
while t:
    s, v = map(int, input().split())
    time = (2.0 * s)/(3.0 * v)
    print(time)
    t -= 1