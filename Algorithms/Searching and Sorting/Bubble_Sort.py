# To sort an array in increasing order


def bubble_sort(my):
    mylist = my[:]
    n = len(mylist)
    for i in range(n):
        swap = False
        for j in range(n - i - 1):
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
                swap = True
        if swap is False:
            break
    return mylist
