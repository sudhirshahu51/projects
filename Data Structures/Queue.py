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
    def __init__(self, data, pr):
        self.data = data
        self.next = None
        self.pr = pr


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):            # to print the data of the linked list starting from head
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


class PriorityQueue:        # Data structure of priority queue used in scheduling in O.S
    def __init__(self):
        self.item = LinkedList()
        self.size = 0

    def enqueue(self, data, pri):
            if self.item.head is None or pri > self.item.head.pr:
                new_node = Node(data, pri)
                tmp = self.item.head
                new_node.next = tmp
                self.item.head = new_node
                del tmp

            else:
                tmp = self.item.head
                new_node = Node(data, pri)
                while tmp.next is not None and tmp.next.pr > pri:
                    tmp = tmp.next
                new_node.next = tmp.next
                tmp.next = new_node
            self.size += 1

    def is_empty(self):
        return self.item.head is None

    def de_queue(self):
        self.item.head = self.item.head.next
        self.size -= 1

    def front(self):
        return self.item.head.data

    def rare(self):
        tmp = self.item.head
        while tmp.next is not None:
            tmp = tmp.next
        return tmp.data
