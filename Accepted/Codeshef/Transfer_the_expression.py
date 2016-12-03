# To convert infix expression to postfix expressions
class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
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


def is_operand(ch):
    return ('a' <= ch <= 'z') or ('A' <= ch <= 'Z')


def pre(ch):
    d = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    if ch in d.keys():
        return d[ch]
    else:
        return -1


def infix_to_postfix(ch):
    ch = list(ch)
    stack = Stack()
    out = []
    for token in ch:
        if is_operand(token):
            out.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            top_token = stack.pop()
            while top_token != '(':
                out.append(top_token)
                top_token = stack.pop()
        else:
            while (not stack.empty()) and pre(stack.peek()) >= pre(token):
                out.append(stack.pop())
            stack.push(token)
    while not stack.empty():
        out.append(stack.pop())
    return ''.join(out)

n = int(input())
for _ in range(n):
    t = input()
    print(infix_to_postfix(t))
