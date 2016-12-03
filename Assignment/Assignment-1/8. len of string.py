# To find the no. of characters in the given string
print('hello user')
ch = input(str('enter the string\n'))
new = ch.split()
n = len(new)
b = []
for i in range(n):
    a = new[i]
    c = list(a)
    b.extend(c)
print(len(b))
input('press enter to exit')