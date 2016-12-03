class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        self.pre = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):             # to insert at the end of list
        new_node = Node(data)
        previous = None
        current = self.head
        while current:
            previous = current
            current = current.next
        previous.next = new_node
        new_node.pre = previous

    def print_list(self):           # to insert at the beginning of the list
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next

    def push(self, data):
        new_node = Node(data)
        temp = self.head
        temp.pre = new_node
        self.head = new_node
        new_node.next = temp

    def insert_after(self, pre_node, data):
        new_node = Node(data)
        if pre_node.next is None:
            pre_node.next = new_node
            return
        temp = pre_node.next
        new_node.pre = pre_node
        new_node.next = pre_node.next
        pre_node.next = new_node
        temp.pre = new_node
        del temp

    def delete_list(self, node):
        if node.pre is None:
            temp = self.head
            self.head = self.head.next
            self.head.pre = None
            del temp
        elif node.next is None:
            temp = node
            previous = temp.pre
            previous.next = None
            del temp
        else:
            previous = node.pre
            nex = node.next
            previous.next = nex
            nex.previous = previous

    def reverse(self):
        pre = None
        current = self.head
        nex = Node
        while current:
            nex = current.next
            current.next = pre
            current.pre = nex
            pre = current
            current = nex
        self.head = pre


t = DoubleLinkedList()
t.head = Node(1)
t.append(3)
t.append(2)
t.append(0)
t.print_list()
print('\n')
print(t.head.next.next)
t.print_list()