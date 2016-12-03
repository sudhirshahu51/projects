# To make a algorithm for sorting in decreasing order


def selection_sort(my):
    mylist = my[:]
    for i in range(len(mylist)):
        small = i
        for j in range(1 + i, len(mylist)):
            if mylist[j] < mylist[small]:
                small = j
        mylist[i], mylist[small] = mylist[small], mylist[i]
    return mylist
