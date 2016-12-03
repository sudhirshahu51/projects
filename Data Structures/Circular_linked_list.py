class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self,):
        self.head = None
        self.last = self.head
        self.count = 1

    def print_list(self):
        if self.head is None:
            return
        else:
            tmp = self.head
            for _ in range(self.count):
                print(tmp.data)
                tmp = tmp.next

    def push(self, data):
        tmp = self.head
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        for _ in range(self.count - 2):
            tmp = tmp.next
        self.last = tmp
        self.last.next = self.head

    def append(self, data):
        new_node = Node(data)
        self.last.next = new_node
        self.last = new_node
        self.last.next = self.head
        self.count += 1

    def delete(self, node):
        if self.head.next is None:
            self.count -= 1
            self.head = None
        elif self.head == node:
            tmp = self.head
            self.last.next = tmp.next
            self.head = tmp.next
            self.count -= 1
            del tmp
        elif self.last == node:
            tmp = self.head
            for _ in range(self.count - 2):
                tmp = tmp.next
            tmp.next = node.next
            self.count -= 1
            del tmp
        else:
            tmp = self.head
            while tmp.next != node:
                tmp = tmp.next
            tmp.next = node.next
            self.count -= 1
            del tmp


h = CircularLinkedList()
h.head = Node(1)
h.append(10)
h.append(14)