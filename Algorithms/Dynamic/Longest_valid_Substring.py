# Length of the longest valid substring

x = list(input('Enter the substring'))
s = [-1]
result = 0
for i in range(len(x)):
    print(s)
    if x[i] == '(':
        s.append(i)
    elif x[i] == ')':
        s.pop()
        if len(s) == 0:
            s.append(i)
        if i - s[-1] > result:
            result = i - s[-1]
print(result)
