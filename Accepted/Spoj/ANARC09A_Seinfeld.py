match = {'{': '}', '}': '{'}
x = input()
count = 1
while x.find('-') == -1:
    stack = []
    for i in range(len(x)):
        if x[i] == '{':
            stack.append(x[i])
        elif x[i] == '}':
            if len(stack) != 0:
                if stack[len(stack) - 1] == match[x[i]]:
                    stack.pop()
                else:
                    stack.append(x[i])
            else:
                stack.append(x[i])
    o = stack.count('{')
    c = stack.count('}')
    print(stack, o, c)
    ans = 0
    if o % 2 == 0:      # if one is even the other will be even also
        ans = len(stack)//2
    else:
        ans = (o-1)//2 + (c-1)//2 + 2
    print(count, '. ', ans, sep='')
    count += 1
    x = input()