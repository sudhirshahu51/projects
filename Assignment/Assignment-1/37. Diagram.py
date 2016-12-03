# to make a diagram
n = int(input('Enter the string'))
y = 0
for i in range(-n, 0):
    j = -i
    print(j*' ', end = '')
    y += 1
    for k in range(y, n-y):
        print(k, end='')
    print('\n', end='')