# To change the lower case alphabets into upper case alphabets
k = str(input('Enter the string\n'))
l = list(k)
for i in range(len(l)):
    if ord(l[i]) in range(65,91):
        x = ord(l[i])
        x=x+32
        l[i] = chr(x)
    else:
        continue
j = ''.join(l)
print(j)
input('press enter to exit')
