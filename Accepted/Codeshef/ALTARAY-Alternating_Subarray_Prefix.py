t = int(input())
for _ in range(t):
    n = int(input())
    l = input().split()
    final = [1]*n
    for i in range(n - 1):
        if (l[i][0] == '-' and l[i+1][0] != '-') or (l[i+1][0] == '-' and l[i][0] != '-'):
            final[i] += 1
    for j in range(len(final)):
        if final[-(j+1)] == 2 and final[-j] > 1:
            final[-(j+1)] += final[-j] - 1
    for k in range(len(final)):
        print(final[k], ' ', end='')