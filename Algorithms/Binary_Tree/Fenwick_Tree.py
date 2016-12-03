# Binary Indexed Tree or fenwick tree is to find the sum of array upto n index in O(logn)
# Time Another implementation can be done using segmented tree


# For a array of 0 n indexes fenwick tree will have 0 to n+1
# The indices of tree are a little complex
'''
            0
    /    /      \     \
   1    2       4     8
        \      / \   /  \
        3     5  6  9   10
This is created using shifting of the binary representation of the no.
2: 10 if we flick the right most set bit ie 1 to 0 then it becomes 0 so 2 is under 0
8: 1000 if we flick the right most set bit ie 1 to 0 then it becomes 0 so 8 is under 0
10: 1010 if flick the right most set bit ie 1 to 0 then it becomes 1000 ie 8 so 10 is under 8
11:1011 if flick the right most set bit then it becomes 1010 ie 10 so 11 is under 10


For storing we will represent the indices of tree in binary term and see from which array
indices we have to store
arrray: [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
index:  [0, 1, 2,  3, 4, 5, 6,  7, 8, 9, 10]

indices of tree      indices in array           value
1= 0 + 2^0              (0, 0)                  3
2= 0 + 2^1              (0, 1)                  5
3= 2^1 + 2^0            (2, 2)                  -1
4= 0 + 2^2              (0, 3)                  10
5= 2^2 + 2^0            (4, 4)                  5
6= 2^2 + 2^1            (4, 5)                  9
7= 2^2 + 2^1 + 2^0      (6, 6)                  -3
8= 0 + 2^3              (0, 7)                  19
9= 2^3 + 2^0            (8, 8)                  7
10= 2^3 + 2^1           (8, 9)                  9
11= 2^3 + 2^1 + 2^0     (10, 10)                3
z = x + y   i.e starting from index x sum of next y elements will be stored in z

To search the value:
find sum from 0-5:
go to node 6 in the indexed tree then to its parent and then to its parent unless
you come to the root, add all these values
node(6) = 9, parent = 4
node(4) = 10 parent = 0
node(0) = 0
sum = 19 ie the ans

'''


class FenwickTree:
    def __init__(self, arr):
        self.array = [0 for _ in range(len(arr) + 1)]
        self.arr = arr

    def intialize(self):
        for i in range(len(self.arr)):
            self.array[i+1] += self.arr[i]
            tmp = get_next(i+1)
            while tmp < len(self.array):
                self.array[tmp] += self.arr[i]
                tmp = get_next(tmp)

    def get_sum(self, index):
        sum = self.array[index+1]
        tmp = get_parent(index+1)
        while tmp > 0:
            sum += self.array[tmp]
            tmp = get_parent(tmp)
        return sum

    def update(self, index, data):
        change = data - self.arr[index]
        self.array[index+1] += change
        tmp = get_next(index+1)
        while tmp < len(self.array):
            self.array[tmp] += change
            tmp = get_next(tmp)
        self.arr[index] = data


def get_parent(x):   # to get a parent of a node
    '''find 2's complement(flip all the bits and then add 1) and && original
    no. the value resulted is subtracted from original number
    or simply flick the right most set bit
    '''
    comp = int(bin(-x + 2**32), base=2)
    tmp = comp & x
    return x - tmp


def get_next(x):    # to get the next affected node to be changed
    '''find 2's complement and && original no. the value resulted is then added
    tot the original no.'''
    comp = int(bin(-x + 2**32), base=2)
    tmp = comp & x
    return x + tmp


l = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
L = FenwickTree(l)
L.intialize()
L.update(2, 10)
print(L.array)
