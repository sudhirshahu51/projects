class BinarySearchTree:
    items = {}

    def __init__(self):
        self.root = None

    def __len__(self):      # Builtin length function returns this value
        return self.length()

    def __getitem__(self, item):       # a = BinarySearchTree[key] will return the node of that key
        # To lookup or search a node by the key
        try:
            return BinarySearchTree.items[item]
        except KeyError:
            return None

    def __contains__(self, item):       # Builtin function of in can be used
        if self.__getitem__(item):
            return True
        else:
            return False

    def __iter__(self):                 # to iterate in loops
        return iter(BinarySearchTree.items.values())

    def __setitem__(self, k, v):        # dictionary implementation can be used
            self.put(k, v)

    def __delitem__(self, k):           # del function can be used
        self.delete_key(k)

    def get(self, item):
        return self.__getitem__(item)

    def length(self):
        return len(BinarySearchTree.items)

    def put(self, k, v):
        if self.root:
            self._put(k, v, self.root)
        else:
            self.root = Node(k, v)
            BinarySearchTree.items[k] = self.root

    def _put(self, k, v, current):
        if k > current.key:
            if current.right is None:
                current.right = Node(k, v)
                current.right.parent = current
                BinarySearchTree.items[k] = current.right
            else:
                self._put(k, v, current.right)
        else:
            if current.left is None:
                current.left = Node(k, v)
                current.left.parent = current
                BinarySearchTree.items[k] = current.left
            else:
                self._put(k, v, current.left)
    
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
                BinarySearchTree.items.pop(tmp.key)
                return
            elif tmp.left is None and tmp.right is not None:
                self.root = tmp.right
                self.root.parent = None
                BinarySearchTree.items.pop(tmp.key)
            elif tmp.right is None and tmp.left is not None:
                self.root = tmp.left
                self.root.parent = None
                BinarySearchTree.items.pop(tmp.key)
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
                BinarySearchTree.items.pop(succ.key)
        elif tmp.left is None and tmp.right is None:
            par = tmp.parent
            if par.left == tmp:
                par.left = None
            else:
                par.right = None
            BinarySearchTree.items.pop(tmp.key)
        elif tmp.right is None and tmp.left is not None:
            par = tmp.parent
            tmp.left.parent = par
            if par.left == tmp:
                par.left = tmp.left
            else:
                par.right = tmp.left
            BinarySearchTree.items.pop(tmp.key)
        elif tmp.left is None and tmp.right is not None:
            par = tmp.parent
            tmp.right.parent = par
            if par.left == tmp:
                par.left = tmp.right
            else:
                par.right = tmp.right
            BinarySearchTree.items.pop(tmp.key)
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
            BinarySearchTree.items.pop(succ.key)


class Node:
    def __init__(self, k, v=0):       # k is the key of node and v is the value of node with default v value is 0
        self.val = v
        self.right = None
        self.left = None
        self.key = k
        self.parent = None

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
    t = BinarySearchTree()
    t[5] = 'a'
    t[3] = 'b'
    t[8] = 'c'
    t[7] = 'd'
    t.put(0, 'e')
    t.put(2, 'f')
    t.put(1, 'g')
    t[4] = 'er'
'''
        5
     /     \
    3      8
   / \    /
  0   4  7
   \
    2
   /
  1
'''
