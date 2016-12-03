m, n = map(int, input('Enter the no. of row and col of the first matrix').split())
p, q = map(int, input('Enter the no. of row and col of the second matrix').split())
if n != p:
    print('Multiplication not possible')
else:
    m1 = []
    m2 = []
    m3 = []
    for i in range(m):
        print('Enter the %d line of the first matrix' % (i+1))
        m1.append([])
        for j in range(n):
            m1[i].append(int(input()))
    for i in range(p):
        print('Enter the %d line of the second matrix' % (i+1))
        m2.append([])
        for j in range(q):
            m2[i].append(int(input()))
    for i in range(m):
        m3.append([])
        for j in range(q):
            m3[i].append(0)
            for k in range(n):
                m3[i][j] += m1[i][k]*m2[k][j]
    for i in range(m):
        print(m3[i])
