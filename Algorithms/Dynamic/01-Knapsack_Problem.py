def zero_one_knapsack(wt, limit, val):
    T = [[0 for _ in range(limit+1)] for _ in range(len(val))]
    for i in range(len(val)):
        for j in range(limit+1):
            if j < wt[i]:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(val[i]+T[i-1][j-wt[i]], T[i-1][j])
    return T[-1][-1], get_used(wt, limit, T)


def get_used(wt, limit, T):
    used = []
    i = len(wt)-1
    j = limit
    while T[i][j] != 0:
        if T[i][j] == T[i-1][j]:
            i -= 1
            pass
        else:
            used.append(wt[i])
            j -= wt[i]
            i -= 1
    return used


print('Enter the weight with space bet them')
wt = list(map(int, input().split()))
print('Enter the val of weight')
val = list(map(int, input().split()))
limit = int(input('Enter the max weight'))
print(zero_one_knapsack(wt, limit, val))
