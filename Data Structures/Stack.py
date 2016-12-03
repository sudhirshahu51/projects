class TwoStacks:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self, x):
            if self.top1 < self.top2 - 1:
                self.top1 += 1
                self.arr[self.top1] = x
            else:
                print('Stack Overflow')
                exit(1)

    def push2(self, x):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x
        else:
            print('Stack Overflow')
            exit(1)

    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.arr[self.top1] = None
            self.top1 -= 1
            return x
        else:
            print('Stack Underflow')
            exit(1)

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.arr[self.top2] = None
            self.top2 += 1
            return x
        else:
            print('Stack Underflow')
            exit(1)


class Stack:
    def __init__(self):
        self.items = []

    def __contains__(self,item):
        return item in self.items

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def print_stack(self):
        print(self.items)

