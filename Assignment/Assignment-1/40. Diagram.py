# To make the diagram
n = int(input('Enter the no. of lines'))
k = n
for i in range(n):
    print(i*' ', end='')
    k -= 1
    for j in range(1, k):
        print(j, end='')
    for l in range(-k, 0):
        m = -l
        print(m, end='')
    print('\n')
input('Press enter to exit')