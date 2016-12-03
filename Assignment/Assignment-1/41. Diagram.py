# To make the diagram
n = int(input('enter the no. of lines'))
k = 2*n-1
a = 0
for i in range(1,n+1):
    k = k-2
    if i != n:
        print(i*'*' + k*' ' + i*'*', end='')

    else :
        a = 2*i - 1
        print(a*'*')

    print('\n', end='')
input('press enter to continue')