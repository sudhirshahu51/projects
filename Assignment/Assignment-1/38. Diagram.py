# To make the diagram
x = int(input('Press enter to string'))
k = 0
for i in range(-x, 0):
    y = -i
    k += 1
    print(y*' ', end='')
    for j in range(-k, 0):
        e = -j
        print(e,end='')
    print('\n')
input('enter press to exit')