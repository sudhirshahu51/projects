# To make all the double characters delete
l = str(input('enter the string\n'))
x = len(l)
l = list(l)
for j in range(x):
    for i in range(97,123):
        if l.count(chr(i)) > 1:
            l.remove(chr(i))
        else:
            continue
    for i in range(65,91):
        if l.count(chr(i)) > 1:
            for j in range(x):
                l.remove(chr(i))
        else:
            continue
print(l)
input('press enter to exit')