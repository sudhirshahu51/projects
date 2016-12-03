# true is {([])()} and false if {[(}


def match(ch):
    d = {'{': '}', '[': ']', '(': ')', '}': '{', ']': '[', ')': '('}
    return d[ch]


stack = []
x = str(input())
if x[0] == '}' or x[0] == ']' or x[0] == ')':
    print('Parentheses are not balanced')
    exit()
for i in range(len(x)):
    if x[i] == '{' or x[i] == '[' or x[i] == '(':
        stack.append(x[i])
    elif x[i] == '}' or x[i] == ']' or x[i] == ')':
        if stack[len(stack) - 1] == match(x[i]):
            stack.pop()
        else:
            print('Parentheses are not balanced')
            exit()
if len(stack) == 0:
    print('Parentheses are balanced')
else:
    print('Parentheses are not balanced')