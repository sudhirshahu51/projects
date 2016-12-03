def counting_sort(arr):
    d = {}
    out = []
    for i in arr:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    for i in d.keys():
        for j in range(d[i]):
            out.append(i)
    return out
