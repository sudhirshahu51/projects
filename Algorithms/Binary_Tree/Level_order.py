class Queue:
    def __init__(self):
        self.items = []

    def __contains__(self, item):
        return item in self.items

    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.insert(0, data)

    def de_queue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def front(self):
        return self.items[-1]

    def rare(self):
        return self.items[0]


class Node:
    nodes = 0

    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key
        Node.nodes += 1
        # self.sub = 0          # To define the value of the subtrees under the node

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
        print(self.val, end=' ')
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
        print(self.val, end=' ')

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


def print_level_order(r):
    if not isinstance(r, Node):
        print('OOPS! WRONG INPUT')
        return
    q = Queue()
    q.enqueue(r)
    while not q.is_empty():
        tmp = q.de_queue()
        if tmp.left is not None:
            q.enqueue(tmp.left)
        if tmp.right is not None:
            q.enqueue(tmp.right)
        print(tmp.val, end=' ')


if __name__ == '__main__':
    root = Node(2)
    root.right = Node(5)
    root.left = Node(7)
    root.right.right = Node(3)
    root.right.left = Node(0)
    root.left.right = Node(9)
    root.left.left = Node(8)
    root.left.left.right = Node(23)
    root.right.left.right = Node(10)
    '''
             2
           /   \
          7     5
         / \   / \
        8  9  0   3
       / \   /
         23 10
    '''
    print_level_order(root)
