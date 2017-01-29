t = int(input())
while t:
    n, m = map(int, input().split())
    list_n = set(map(int, input().split()))
    list_m = set(map(int, input().split()))
    result = list_n - list_m
    print(len(list_n) - len(result))
    t -= 1
