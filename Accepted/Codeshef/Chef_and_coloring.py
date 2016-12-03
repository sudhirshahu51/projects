t = int(input())
for _ in range(t):
    n = int(input())
    c = input()
    r = c.count('R')
    g = c.count('G')
    b = c.count('B')
    result = len(c) - max(r, g, b)
    print(result)