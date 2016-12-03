# To sort a list by insertion sort


def insertion_sort(mylist):
    my = mylist[:]
    for i in range(1, len(my)-1):
        key = my[i+1]
        j = i
        while j > 0 and key < my[j]:
            my[j+1] = my[j]
            j -= 1
        my[j+1] = key
    return my
