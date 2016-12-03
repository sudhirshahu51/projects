m = []
for i in range(5):
    m.append([])
    for j in range(5):
        m[i].append('0')
for i in range(5):
    m[i][i] = '0'
    for j in range(4, i, -1):
        m[i][j] = '1'
    for j in range(i):
        m[i][j] = '-1'
for _ in range(5):
    print(m[_])
