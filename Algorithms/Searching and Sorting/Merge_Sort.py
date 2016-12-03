# To sort a list by merge sort algorithm


def merge(arr, p, q, r):
    final = []
    a, b = p, q+1
    while a <= q and b <= r:
        if arr[a] < arr[b]:
            final.append(arr[a])
            a += 1
        else:
            final.append(arr[b])
            b += 1
    while a <= q:
        final.append(arr[a])
        a += 1
    while b <= r:
        final.append(arr[b])
        b += 1
    a = p
    for i in range(len(final)):
        arr[a] = final[i]
        a += 1


def merge_sort(a):
    ar = a[:]
    merge__sort(ar, 0, len(a)-1)
    return ar


def merge__sort(arr, p, r):
    if p < r:
        q = int((p + r)/2)
        merge__sort(arr, p, q)
        merge__sort(arr, q+1, r)
        merge(arr, p, q, r)
