def zero_one_knapsack(wt, limit, val):
    if not isinstance(wt, list) and isinstance(val, list) and isinstance(limit, int):
        return
    T = [[0 for _ in range(limit+1)] for _ in range(len(val))]
    for i in range(len(val)):
        for j in range(limit+1):
            if j < wt[i]:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(val[i]+T[i-1][j-wt[i]], T[i-1][j])
    return T[-1][-1]


t = int(input())
for _ in range(t):
    limit, no_bag = map(int, input().split())
    wt = [0]*no_bag
    val = [0]*no_bag
    for i in range(no_bag):
        wt[i], val[i] = map(int, input().split())
    print('Hey stupid robber, you can get %s.' % zero_one_knapsack(wt, limit, val))
