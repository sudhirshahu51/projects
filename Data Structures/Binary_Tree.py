class Node:
    nodes = 0       # To count the size of tree
    lst = {}

    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key
        Node.nodes += 1
        # self.sub = 0          # To define the value of the subtrees under the node

    def insert_right(self, key):
        if key is None:
            return
        if isinstance(key, Node):
            self.right = key
            Node.lst[key.val] = key
        elif self.right is None:
            tmp = Node(key)
            self.right = tmp
            Node.lst[key] = tmp
            del tmp

        else:
            print('The position is taken')

    def insert_left(self, key):
        if key is None:
            return
        if isinstance(key, Node):
            self.left = key
            Node.lst[key.val] = key
        elif self.left is None:
            tmp = Node(key)
            self.left = tmp
            Node.lst[key] = tmp
            del tmp
        else:
            print('The position is taken')

    def get_node(self, key):
        if key in Node.lst.keys():
            return Node.lst[key]

    def print_in_order(self, l):
        if self is None:
            return
        # First recur on the left child then print data then right child
        # Gives non - decreasing order for BST
        if self.left is not None:
            self.left.print_in_order(l)
        l.append(self.val)
        if self.right is not None:
            self.right.print_in_order(l)

    def print_pre_order(self, l):
        if self is None:
            return
        # First print data then left child then right child
        # To create copy of the tree
        l.append(self.val)
        if self.left is not None:
            self.left.print_pre_order(l)
        if self.right is not None:
            self.right.print_pre_order(l)

    def print_post_order(self, l):
        if self is None:
            return
        # First recur on the left tree then right tree then print data
        # To delete tree
        if self.left is not None:
            self.left.print_pre_order(l)
        if self.right is not None:
            self.right.print_pre_order(l)
        l.append(self.val)

    def size_tree(self):
        return Node.nodes

    def height(self):
        if self is None:
            return 0
        else:
            if self.right is not None and self.left is not None:
                return max(self.right.height(), self.left.height()) + 1
            elif self.left is not None:
                return self.left.height() + 1
            elif self.right is not None:
                return self.right.height() + 1
            else:
                return 1


if __name__ == '__main__':
    root = Node(2)
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
    print(Node.lst.keys())
