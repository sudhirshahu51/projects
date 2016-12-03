def coin_change(coins, total):
    T = [[0 for x in range(total+1)] for x in range(len(coins)+1)]
    for k in range(total+1):
        T[0][k] = int(k/coins[0])
    for i in range(1, len(coins)+1):
        for j in range(total+1):
            if j < coins[i-1]:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = min(T[i-1][j], T[i][j-coins[i-1]]+1)
    return T[len(coins)][total], coin_used(coins, T)


def coin_used(coins, T):
    used = []
    i = len(coins)
    j = total
    while T[i][j] != 0:
        if T[i][j] == T[i-1][j]:
            i -= 1
        else:
            used.append(coins[i-1])
            j -= coins[i-1]
    return used


coins = list(map(int, input('Enter the coins').split()))
total = int(input('Enter the amount'))
print(coin_change(coins, total))
