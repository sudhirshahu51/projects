class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None
        self.visited = 0


class CircularLinkedList:
    k = 1

    def __init__(self, node):
        self.head = node
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

    def append(self, data):
        self.k += 1
        ke = self.k
        new_node = Node(ke, data)
        self.last.next = new_node
        self.last = new_node
        self.last.next = self.head
        self.count += 1

t = int(input())
while t:
    no_nodes = int(input())
    edges = list(map(int, input().split()))
    start, end = map(int, input().split())
    li = CircularLinkedList(Node(0, edges[0]))
    for i in range(1, no_nodes):
        li.append(edges[i])
    for i in range(no_nodes):
        if i == 0:
            print(li.head.key)
        else:
            st = li.head
            for j in range(i):
                tmp = st.next
                st = st.next
                print(tmp.key)