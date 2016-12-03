# To maximize the profit by buying and selling k maximum stocks for given days
# You're given stock prices on certain days
# You can only do maximum k transactions on a particular day
# Before selling a stock you've to buy that stock before that day


def buy_sell_slow(table, k):
    if not isinstance(table, list) and isinstance(k, int):
        print('Wrong input')
        return
    t = [[0 for j in range(len(table))] for i in range(k+1)]
    for i in range(len(t)):
        t[i][0] = 0
    for i in range(len(table)):
        t[0][i] = 0
    for i in range(1, k+1):
        for j in range(1, len(table)):
            tmp = [table[j] - table[m] + t[i-1][m] for m in range(j)]
            t[i][j] = max(t[i][j-1], max(tmp))
    return t


def buy_sell_optimized(table, k):
    if not isinstance(table, list) and isinstance(k, int):
        print('Wrong input')
        return
    t = [[0 for j in range(len(table))] for i in range(k+1)]
    for i in range(len(t)):
        t[i][0] = 0
    for i in range(len(table)):
        t[0][i] = 0
    for i in range(1, k+1):
        max_diff = t[i][0] - table[0]
        for j in range(1, len(table)):
            max_diff = max(max_diff, t[i-1][j-1] - table[j])
            t[i][j] = max(t[i][j-1], table[j] + max_diff)
    return t


def k_transactions(table, k, t):
    if not isinstance(table, list) and isinstance(k, int) and isinstance(t, list):
        print('OOh! somethings not right')
        return
    i, j = k, len(table)-1
    transactions = []
    current = t[i][j]
    while not (i == 0):
        if current != t[i][j-1]:
            transactions.append('sell on day %s' % j)
            profit = current - table[j]
            for k in range(j, 0, -1):
                if t[i-1][k] - table[k] == profit:
                    transactions.append('buy on day %s' % k)
            i -= 1
            j -= k
            current = t[i][j]
        else:
            while current == t[i][j-1]:
                j -= 1
            transactions.append('sell on day %s' % j)
            profit = current - table[j]
            for k in range(j, -1, -1):
                if t[i-1][k] - table[k] == profit:
                    transactions.append('buy on day %s' % k)
            i -= 1
            j -= k
            current = t[i][j]
    return transactions.reverse()


if __name__ == '__main__':
    '''
    k = int(input('Maximum transactions'))
    print('Enter the values of stock on particular days starting from 0 with space')
    day = list(map(int, input().split()))
    '''
    t = [2, 5, 7, 1, 4, 3, 1, 3]
    k_transactions(t, 3, buy_sell_optimized(t, 3))
