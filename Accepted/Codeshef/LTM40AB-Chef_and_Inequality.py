t = int(input())
while t:
    ans = 0
    a, b, c, d = map(int, input().split())
    if a <= b and c <= d:
        no_x = b - a + 1
        no_y = d - c + 1
        if b < c:
            ans += no_x * no_y
            print(ans)
        elif a <= c and b <= d:
            common = b - c + 1
            ans += (no_x - common) * no_y
            for i in range(no_y-1, no_y-common-1, -1):
                ans += i
            print(ans)
        elif a <= c and b >= d:
            common = no_y
            ans += len(range(a, c)) * common
            for i in range(no_y-1, 0, -1):
                ans += i
            print(ans)
        elif a > c and b > d:
            common = d - a + 1
            for i in range(common-1, 0, -1):
                ans += i
            print(ans)
        else:
            common = no_x
            ans += no_x*len(range(d, b, -1))
            for i in range(no_x-1, 0, -1):
                ans += i
            print(ans)
    t -= 1
