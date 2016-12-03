x = int(input())
while x:
    n = int(input())
    taste = list(map(int, input().split()))
    magic = 0
    l = [False for _ in range(n)]
    for i in range(n):
        visited = l[:]
        start = i
        index = i
        while True:
            visited[index] = True
            index += taste[index] % n + 1
            if index >= n:
                index %= n
            if start == index:
                magic += 1
                break
            elif visited[index]:
                break
    print(magic)
    x -= 1
