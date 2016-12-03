t = int(input())
for _ in range(t):
    n = int(input())
    N = input().split()
    f = int(input())
    F = input().split()
    ans = True
    for i in range(len(N)):
        if N[i:i+f] == F:
            print('Yes')
            ans = False
            break
    if ans:
        print('No')
