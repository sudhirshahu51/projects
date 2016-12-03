t = int(input())
while t > 0:
    s1 = input()
    s2 = input()
    i = 0
    s = 0
    d = 0
    for i in range(len(s1)):
        if s1[i] == '?' or s2[i] == '?':
            d += 1
        elif s1[i] != s2[i]:
            s += 1
    min = s
    max = s + d
    print(min, max)
    t -= 1
