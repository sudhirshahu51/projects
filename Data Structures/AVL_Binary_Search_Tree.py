class AVLBinarySearchTree:
    items = {}

    def __init__(self):
        self.root = None

    def __len__(self):                  # Built in length function returns this value
        return self.length()

    def __getitem__(self, item):        # a = AVLBinarySearchTree[key] will return the node of that key
        # To lookup or search a node by the key
        try:
            return AVLBinarySearchTree.items[item]
        except KeyError:
            return None

    def __contains__(self, item):       # Built in function of in can be used
        if self.__getitem__(item):
            return True
        else:
            return False

    def __iter__(self):                 # to iterate in loops
        return iter(AVLBinarySearchTree.items.values())

    def __setitem__(self, k, v):        # dictionary implementation can be used
            self.put(k, v)

    def __delitem__(self, k):           # delete function can be used
        self.delete_key(k)

    def get(self, item):
        return self.__getitem__(item)

    def length(self):
        return len(AVLBinarySearchTree.items)

    def put(self, k, v):
        if self.root is not None:
            self._put(k, v, self.root)
        else:
            self.root = Node(k, v)
            AVLBinarySearchTree.items[k] = self.root

    def _put(self, k, v, current):
        if k > current.key:
            if current.right is None:
                current.right = Node(k, v)
                current.right.parent = current
                AVLBinarySearchTree.items[k] = current.right
                current = current.right
                self.find_pivot(current)
            else:
                self._put(k, v, current.right)
        elif k < current.key:
            if current.left is None:
                current.left = Node(k, v)
                current.left.parent = current
                AVLBinarySearchTree.items[k] = current.left
                current = current.left
                self.find_pivot(current)
            else:
                self._put(k, v, current.left)
        else:
            print('Duplicate keys')
    
    def find_pivot(self, current):
        lst = []
        while current is not None:
            un = self.unbalanced_node(current)
            if -1 <= un <= 1:
                lst.append(current)
            else:
                self.pivot(current, lst, un)
                lst = []
            current = current.parent

    def pivot(self, current, lst, unbalanced):
        if len(lst) < 2:
            print('Somethings not right')
            return
        if current.left in lst:
            child = current.left
        else:
            child = current.right
        if child.left in lst:
            grand_child = child.left
        else:
            grand_child = child.right
        if unbalanced > 1:
            if child.left == grand_child:
                self.right_rotation(current)
            elif child.right == grand_child:
                self.left_rotation(child)
                self.right_rotation(current)
            else:
                print('left cases')
        elif unbalanced < -1:
            if child.left == grand_child:
                self.right_rotation(child)
                self.left_rotation(current)
            elif child.right == grand_child:
                self.left_rotation(current)
            else:
                print('right cases')

    def unbalanced_node(self, current):
        if current.left is not None:
            l = self.height(current.left)
        else:
            l = 0
        if current.right is not None:
            r = self.height(current.right)
        else:
            r = 0
        current.balance = l - r
        return current.balance
    
    def height(self, current):
        if current.left is not None:
            l_height = self.height(current.left)
        else:
            l_height = 0
        if current.right is not None:
            r_height = self.height(current.right)
        else:
            r_height = 0
        if l_height > r_height:
            return l_height + 1
        else:
            return r_height + 1

    def right_rotation(self, current):
        left_node = current.left
        par = current.parent
        if self.root != current:
            if par.left == current:
                par.left = left_node
            else:
                par.right = left_node
            
        else:
            self.root = left_node
        left_node.parent = par
        current.parent = left_node
        if left_node.right is not None:
            current.left = left_node.right
            left_node.right = current
            current.left.parent = current
        else:
            left_node.right = current
            current.left = None
    
    def left_rotation(self, current):
        right_node = current.right
        par = current.parent
        if self.root != current:
            if par.left == current:
                par.left = right_node
            else:
                par.right = right_node
        else:
            self.root = right_node
        right_node.parent = par
        current.parent = right_node
        if right_node.left is not None:
            current.right = right_node.left
            right_node.left = current
            current.right.parent = current
        else:
            right_node.left = current
            current.right = None
    
    def min_value(self):            # To find the node with minimum value of key
        if self.root is None:
            print('No nodes')
            return self
        else:
            current = self.root
            while current.left is not None:
                current = current.left
            return current

    def max_value(self):            # To find the node with maximum value of key0
        if self.root is None:
            print('No nodes')
            return self
        else:
            current = self.root
            while current.right is not None:
                current = current.right
            return current

    def print(self, l, order='inorder'):
        if order == 'inorder':
            self.print_in_order(l, self.root)
        elif order == 'preorder':
            self.print_pre_order(l, self.root)
        elif order == 'postorder':
            self.print_post_order(l, self.root)
        print(l)

    def print_in_order(self, l, current):
        if current is None:
            return
        # First recur on the left child then print data then right child
        # Gives non - decreasing order for BST
        if current.left is not None:
            self.print_in_order(l, current.left)
        l.append(current.key)
        if current.right is not None:
            self.print_in_order(l, current.right)

    def print_pre_order(self, l, current):
        if self is None:
            return
        # First print data then left child then right child
        # To create copy of the tree
        l.append(current.key)
        if current.left is not None:
            self.print_in_order(l, current.left)
        if current.right is not None:
            self.print_in_order(l, current.right)

    def print_post_order(self, l, current):
        if self is None:
            return
        # First recur on the left tree then right tree then print data
        # To delete tree
        if current.left is not None:
            self.print_in_order(l, current.left)
        if current.right is not None:
            self.print_in_order(l, current.right)
        l.append(current.key)

    def delete_key(self, k):      # To delete the node by searching key
        if self.root is None:
            return self
        tmp = self.get(k)
        if tmp is None:
            print('key is not present in the binary search tree')
        elif tmp.parent is None:
            print('Root node is to be deleted')
            if tmp.left is None and tmp.right is None:
                self.root = None
                AVLBinarySearchTree.items.pop(tmp.key)
                return
            elif tmp.left is None and tmp.right is not None:
                self.root = tmp.right
                self.root.parent = None
                AVLBinarySearchTree.items.pop(tmp.key)
            elif tmp.right is None and tmp.left is not None:
                self.root = tmp.left
                self.root.parent = None
                AVLBinarySearchTree.items.pop(tmp.key)
            else:
                succ = tmp.right
                while succ.left is not None:
                    succ = succ.left
                tmp.key, succ.key = succ.key, tmp.key
                tmp.val, succ.val = succ.val, tmp.val
                par = succ.parent
                if succ.right is None:
                    if par.left == succ:
                        par.left = None
                    else:
                        par.right = None
                else:
                    if par.left == succ:
                        par.left = succ.right
                    else:
                        par.right = succ.right
                self.find_pivot_del(par)
                AVLBinarySearchTree.items.pop(succ.key)
        elif tmp.left is None and tmp.right is None:
            par = tmp.parent
            if par.left == tmp:
                par.left = None
            else:
                par.right = None
            AVLBinarySearchTree.items.pop(tmp.key)
            self.find_pivot_del(par)
        elif tmp.right is None and tmp.left is not None:
            par = tmp.parent
            tmp.left.parent = par
            if par.left == tmp:
                par.left = tmp.left
            else:
                par.right = tmp.left
            AVLBinarySearchTree.items.pop(tmp.key)
            self.find_pivot_del(par)
        elif tmp.left is None and tmp.right is not None:
            par = tmp.parent
            tmp.right.parent = par
            if par.left == tmp:
                par.left = tmp.right
            else:
                par.right = tmp.right
            AVLBinarySearchTree.items.pop(tmp.key)
            self.find_pivot_del(par)
        elif tmp.left is not None and tmp.right is not None:
            succ = tmp.right
            while succ.left is not None:
                succ = succ.left
            tmp.key, succ.key = succ.key, tmp.key
            tmp.val, succ.val = succ.val, tmp.val
            par = succ.parent
            if succ.right is None:
                if par.left == succ:
                    par.left = None
                else:
                    par.right = None
            else:
                if par.left == succ:
                    par.left = succ.right
                else:
                    par.right = succ.right
            self.find_pivot_del(par)
            AVLBinarySearchTree.items.pop(succ.key)

    def find_pivot_del(self, current):
        print('o', current.key)
        while current is not None:
            un = self.unbalanced_node(current)
            if -1 <= un <= 1:
                pass
            else:
                print('happened')
                self.pivot_del(current, un)
            current = current.parent

    def pivot_del(self, current, unbalanced):
        child = self.larger_child(current)
        grand_child = self.larger_child(child)
        if unbalanced > 1:
            if child.left == grand_child:
                self.right_rotation(current)
            elif child.right == grand_child:
                self.left_rotation(child)
                self.right_rotation(current)
            else:
                print('left cases')
        elif unbalanced < -1:
            if child.left == grand_child:
                self.right_rotation(child)
                self.left_rotation(current)
            elif child.right == grand_child:
                self.left_rotation(current)
            else:
                print('right cases')

    def larger_child(self, current):
        if current.left is not None:
            l = self.height(current.left)
        else:
            l = 0
        if current.right is not None:
            r = self.height(current.right)
        else:
            r = 0
        if l > r:
            return current.left
        else:
            return current.right


class Node:
    def __init__(self, k, v=0):       # k is the key of node and v is the value of node with default v value is 0
        self.val = v
        self.right = None
        self.left = None
        self.key = k
        self.parent = None
        self.balance = 0
    
    def replace(self, k, v, lc=None, rc=None):        # k is key v is value lc is left child and rc is right child
        self.key = k
        self.val = v
        self.right = rc
        self.left = lc
        if self.right is not None:
            self.right.parent = self
        if self.left is not None:
            self.left.parent = self

if __name__ == '__main__':
    t = AVLBinarySearchTree()
    t[5] = '5'
    t[3] = '3'
    t[6] = '6'
    t[2] = '2'
    t[1] = '1'
    t[0] = '0'
    t[7] = '8'
    e = []
    t.print(e, 'inorder')
    t.delete_key(0)
    print(t.root.right.right.key)
