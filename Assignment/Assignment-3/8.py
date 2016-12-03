# To merge two sorted arrays
def merge(a, b):
    assert isinstance(a, list), 'The entered sample are not array'
    assert isinstance(b, list), 'The entered sample are not array'
    p = 0
    r = 0
    q = len(a)
    s = len(b)
    final = []
    while p < q and r < s:
        if a[p] < b[r]:
            final.append(a[p])
            p += 1
        else:
            final.append(b[r])
            r += 1
    while p < q:
        final.append(a[p])
        p += 1
    while r < s:
        final.append(b[r])
        r += 1
    return final


x = list(map(int, input('Enter the first array').split()))
y = list(map(int, input('Enter the second array').split()))
print(merge(x, y))
