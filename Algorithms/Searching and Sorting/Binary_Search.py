# To search for a value in a sorted array.
def binary__search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary__search(arr, l, mid - 1, x)
        else:
            return binary__search(arr, mid + 1, r, x)
    else:
        return -1


def binary_search(arr, x):
    y = binary__search(arr, 0, len(arr) - 1, x)
    return y



