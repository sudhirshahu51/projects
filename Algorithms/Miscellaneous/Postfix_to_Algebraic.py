# To convert postfix expressions to algebraic expressions
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
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


def converter(ch):
    d = {'+': 1, '-': 2, '*': 3, '/': 4}
    return d[ch]


def postfix(ch):
    ch = list(ch.split())
    stack = Stack()
    for token in ch:
        if token.isdecimal():
            stack.push(token)
        else:
            pop1 = int(stack.pop())
            pop2 = int(stack.pop())
            if converter(token) == 1:
                stack.push(pop1 + pop2)
            elif converter(token) == 2:
                stack.push(pop2 - pop1)
            elif converter(token) == 3:
                stack.push(pop2 * pop1)
            elif converter(token) == 4:
                stack.push(pop2/pop1)
    return int(stack.pop())


if __name__ == '__main__':
    t = '80 1 + 1 2 + /'
    print(postfix(t))
