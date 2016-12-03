# To make the diagram
n = int(input('enter the no. of lines'))
j = 0
for i in range(n):
    j = n-i
    print(i*' ',end='')
    print(j*'* ',end='')
    print('\n',end='')
for i in range(n):
    j = n-i
    print(j*' ',end='')
    print(i*'* ',end='')
    print('\n',end='')
input('Press enter to exit')