def level(a):
    sum = (a-1)/2*(2*3 + (a-2)*3)
    sum += a*2
    return int(sum % 1000007)

t = int(input())
for _ in range(t):
    print(level(int(input())))
