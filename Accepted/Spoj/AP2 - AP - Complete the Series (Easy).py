for _ in range(int(input())):
    l = []
    [x, y, z] = map(lambda c: int(c), input().split())
    n = (2 * z)//(x + y)
    d = (y - x)//(n - 5)
    a = x - 2 * d
    print(n)
    for i in range(0, n):
        print(a + i * d, end=" ")
