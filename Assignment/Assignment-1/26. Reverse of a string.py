# To reverse the string
st = str(input('Enter the string whose reverse has to be found'))
s = list(st)
x = len(s)
y = x-1
k = []
for i in range(-y, 1):
    k.append(s[-i])
s = ''.join(k)
print(s)
input('press enter to exit')
