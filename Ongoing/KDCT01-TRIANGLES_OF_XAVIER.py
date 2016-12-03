t, k = map(int, input().split())
count = 0
while t:
    a, b = map(int, input().split())
    a, b = max(a, b), min(a, b)
    a **= 2
    b **= 2
    print(a, b)
    c_max = (a + b)**0.5
    if a != b:
        c_min = (a - b)**0.5
    else:
        c_min = a**0.5
    print(c_max, c_min)
    diff = c_max - c_min
    if diff >= k:
        count += 1
    t -= 1
print(count)

