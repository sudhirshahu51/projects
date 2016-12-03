# To sort an array considering it as a nearly complete binary tree and then sorting it using max heapify


def max_heapify(mh, idx):
    left = (idx << 1) + 1
    right = (idx + 1) << 1
    largest = idx
    if left < len(mh) and mh[left] > mh[largest]:
        largest = left
    if right < len(mh) and mh[right] > mh[largest]:
        largest = right
    if largest != idx:
        mh[idx], mh[largest] = mh[largest], mh[idx]
        max_heapify(mh, largest)


def build_max_heap(mh):
    n = len(mh)//2
    for i in range(n, -1, -1):
        max_heapify(mh, i)


def heap_sort(mh):
    y = []
    while len(mh) > 0:
        n = len(mh) - 1
        build_max_heap(mh)
        mh[0], mh[n] = mh[n], mh[0]
        y.append(mh[n])
        mh.pop(n)
        max_heapify(mh, 0)
    return y

