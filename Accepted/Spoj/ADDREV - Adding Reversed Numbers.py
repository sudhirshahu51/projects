def reverse(x):
    x = str(x)
    x = list(x)
    x.reverse()
    x = ''.join(x)
    x = int(x)
    return x


n = int(input())
for _ in range(n):
    [a, b] = str(input()).split()
    [a, b] = [int(a), int(b)]
    c = reverse(a) + reverse(b)
    c1 = reverse(str(c))
    print(c1)

