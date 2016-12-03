import sys
sys.path.insert(0, "D:\WORK\Python\Main\Data Structures\\")
from Binary_Tree import *


def construct_in_pre(n, p, instart, inend):     # n is the in order list and p is the pre order list
    if not (isinstance(n, list) or isinstance(p, list)):
        print('OOPS! WRONG INPUT')
        return
    if instart > inend:         # If there are no element left bet instart and inend of n list
        return None
    tnode = Node(p[construct_in_pre.ind])       # Making the node of all the elements
    construct_in_pre.ind += 1
    if instart == inend:            # When the recursion completes
        return tnode
    ind_tmp = search(n, instart, inend, tnode.val)  # Searching for the element of p in n
    # Breaking the in order in two left and right
    tnode.insert_left(construct_in_pre(n, p, instart, ind_tmp-1))
    tnode.insert_right(construct_in_pre(n, p, ind_tmp+1, inend))
    return tnode
                    
                
def search(arr, start, end, val):
    for i in range(start, end+1):
        if arr[i] == val:
            return i
        
if __name__ == '__main__':
    root = Node(2)
    print(type(root))
    root.insert_right(5)
    root.insert_left(7)
    root.right.insert_right(3)
    root.right.insert_left(0)
    root.left.insert_right(9)
    root.left.insert_left(8)
    root.left.left.insert_right(23)
    root.right.left.insert_right(10)
    '''
             2
           /   \
          7     5
         / \   / \
        8  9  0   3
       / \   /
         23 10
    '''

    inorder = []
    root.print_in_order(inorder)
    print(inorder)
    preorder = []
    root.print_pre_order(preorder)
    print(preorder)
    construct_in_pre.ind = 0
    roo = construct_in_pre(inorder, preorder, 0, len(inorder)-1)
    t = []
    roo.print_in_order(t)
    print(t)
