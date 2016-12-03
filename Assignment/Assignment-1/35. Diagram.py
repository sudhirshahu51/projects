# To draw the diagram
x = int(input('Enter the no. of lines'))
for i in range(1, x+1):
    print('\n')
    for j in range(1,i):
        print(j,  ' ',end ='')
for i in range(-x, 0):
    print('\n')
    for j in range(1,-(i-1)):
        print(j,  ' ',end ='')
input('press enter to exit')