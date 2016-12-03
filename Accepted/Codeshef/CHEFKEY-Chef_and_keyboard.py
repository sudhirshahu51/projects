def factors(x):
    fact = []
    i = 1
    while i < (x//2)+1:
        if x % i == 0:
            fact.append((i, x//i))
        i += 1
    fact.append((x, 1))
    return fact


t = int(input())
while t:
    n, m, c = map(int, input().split())
    fact = factors(c)
    count = 0
    for i in fact:
        if i[0] <= n and i[1] <= m:
            count += 1
    print(count)
    t -= 1