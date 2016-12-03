def p(l):
    for i in range(len(l)):
        print(l[i])


def subset_sum(st, total):
    n = len(st)
    T = [[False for _ in range(total+1)] for _ in range(n+1)]
    for i in range(n):
        T[i][0] = True
    T[1][st[0]] = True
    for i in range(1, n+1):
        for j in range(1, total + 1):
            if st[i-1] > j:
                T[i][j] = T[i-1][j]
            elif T[i-1][j] is True:
                T[i][j] = True
            else:
                T[i][j] = T[i-1][j-st[i-1]]
    return T[n][total], get_used(st, total, n, T)


def get_used(st, total, n, T):
    i = n
    j = total
    used = []
    while j != 0 and i >= 0:
        if T[i][j] == T[i-1][j]:
            i -= 1
        else:
            used.append(st[i-1])
            j -= st[i-1]
            i -= 1
    return used


st = list(map(int, input('Enter the positive integers with spaces bet them').split()))
total = int(input('Enter teh total sum'))
print(subset_sum(st, total))