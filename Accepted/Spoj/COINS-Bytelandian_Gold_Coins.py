# implementing dynamic programing to find the maximum
import sys


def coin(a):
    global table
    if not isinstance(a, int):
        return
    if a < 1:
        return 0
    if a in table:
        return table[a]
    else:
        table[a] = max((coin(a//2) + coin(a//3) + coin(a//4)), a)
        return table[a]


table = {}      # Dictionary
lines = sys.stdin.readlines()
for i in lines:
    print(coin(int(i)))
