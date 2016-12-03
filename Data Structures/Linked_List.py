class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SortLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None or data < self.head.data:
            new_node = Node(data)
            tmp = self.head
            new_node.next = tmp
            self.head = new_node
            del tmp
        else:
            tmp = self.head
            new_node = Node(data)
            while tmp.next is not None and tmp.next.data < data:
                tmp = tmp.next
            new_node.next = tmp.next
            tmp.next = new_node

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):            # to print the data of the linked list starting from head
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):                     # to insert a new node at the beginning
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):     # to insert new node in middle
        if prev_node is None:
            print('The given previous node must be linked in')
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):                 # to insert a new node in the last
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def delelte_node(self, node):
        node.data = node.next.data
        tmp = node.next
        node.next = tmp.next
        del tmp

    def delete_data(self, node_value):          # to delete the node containing the given data
        previous = self.head
        if previous.data == node_value:
            self.head = self.head.next
        else:
            while previous.data != node_value:
                previous = previous.next
                if previous is None:
                    return
            temp = previous.next
            previous.next = temp.next
            del temp

    def delete_position(self, position):        # to delete node of given index
        temp = self.head
        if position == 0:
            self.head = self.head.next
        else:
            for _ in range(position):
                prev = temp
                temp = temp.next
                if temp is None:
                    return
            prev.next = temp.next
            del temp

    def delete_list(self):              # to delete the whole linked list data
        current = self.head
        while current:
            nex = current.next
            del current
            current = nex
        self.head = None

    def length(self, node):             # To find the length of the linked list
        count = 0
        temp = node
        while temp:
            count += 1
            temp = temp.next
        return count
    '''
    def length(self, node):         # making recursive loop to find out the length
        if not node:
            return 0
        else:
            return 1 + self.length(node.next)
    '''

    def search(self, key):          # To search if the data exist in the linkedlist
        temp = self.head
        while temp.data != key:
            temp = temp.next
            if temp is None:
                return False
        if temp is not None:
            return True

    def swap(self, x, y):           # to swap data from nodes
        x_prev = None
        y_prev = None
        x_current = self.head
        y_current = self.head
        if x == y:
            return
        while x_current and x_current.data != x:        # searching for the x key
            x_prev = x_current
            x_current = x_current.next
        while y_current and y_current.data != y:         # searching for the y key
            y_prev = y_current
            y_current = y_current.next
        if x_current is None and y_current is None:         # if either key is not present
            return
        if x_prev is not None:                      # if x is not head of the linked list
            x_prev.next = y_current
        else:
            self.head = y_current
        if y_prev is not None:                      # if y is not head of the linked list
            y_prev.next = x_current
        else:
            self.head = x_current
        temp = x_current.next                       # swapping the x and y
        x_current.next = y_current.next
        y_current.next = temp

    def get_n(self, node):                      # To return the data at given index of node
        count = 0
        temp = self.head
        while temp:
            if count == node:
                return temp.data
            count += 1
            temp = temp.next

    def middle(self):                   # To find the middle of the linked list
        temp = self.head
        temp1 = self.head
        while temp1 and temp1.next:
            temp1 = temp1.next.next
            temp = temp.next
        return temp.data

    def get_n_last(self, n):            # To return the data at given index from last of node
        temp = self.head
        l = self.length(temp)
        if n > self.length(temp):
            return
        if n == 0:
            return
        for i in range(l - n):
            temp = temp.next
        return temp.data

    def count(self, key):               # to count the no. of times the data exist in list
        temp = self.head
        c = 0
        while temp:
            if temp.data == key:
                c += 1
            temp = temp.next
        return c

    def reverse(self):              # To reverse the linked list
        previous = None
        current = self.head
        while current:
            nex = current.next
            current.next = previous
            previous = current
            current = nex
        self.head = previous

    def detect_loop(self):          # to detect if their is a loop bet the nodes of list
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

    def create_loop(self, x):       # To creat a loop between the nodes
        x_temp = self.head
        last = self.head
        for _ in range(x):
            if x_temp is None:
                break
            x_temp = x_temp.next
        for _ in range(self.length(self.head)):
            if last is None:
                break
            prev = last
            last = last.next
        prev.next = x_temp

    def seletction_data(self):
        tmp = self.head
        while tmp.next is not None:
            q = tmp.next
            while q is not None:
                if tmp.data > q.data:
                    tmp1 = tmp.data
                    tmp.data = q.data
                    q.data = tmp1
                q = q.next
            tmp = tmp.next

    def selection_links(self):
        tmp = self.head
        r = tmp
        while tmp.next is not None:
            q = tmp.next
            s = q
            while q is not None:
                if tmp.data > q.data:
                    tmp1 = tmp.next
                    tmp.next = q.next
                    q.next = tmp1
                    if tmp != self.head:
                        r.next = q
                        s.next = tmp
                    if tmp == self.head:
                        self.head = q
                    tmp2 = tmp
                    tmp = q
                    q = tmp2
                s = q
                q = q.next
            r = tmp
            tmp = tmp.next

    def bubble_data(self):
        end = None
        while end != self.head.next:
            p = self.head
            while p.next != end:
                q = p.next
                if p.data > q.data:
                    tmp = p.data
                    p.data = q.data
                    q.data = tmp
                p = p.next
            end = q

    def bubble_links(self):
        end = None
        while end != self.head.next:
            p = self.head
            r = p
            while p.next != end:
                q = p.next
                if p.data > q.data:
                    p.next = q.next
                    q.next = p
                    if p != self.head:
                        r.next = q
                    else:
                        self.head = q
                    tmp = p
                    p = q
                    q = tmp
                p = p.next
            end = q


t = LinkedList()
t.head = Node(1)
t.append(8)
t.append(3)
t.append(5)
t.append(25)
t.append(10)
t.append(9)
t.print_list()
print('\n')
t.bubble_links()
t.print_list()

