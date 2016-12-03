from math import floor

x = str(input('Enter the decimal no. to be converted'))
b = int(input('Enter the maximum no. of digits after decimal'))


def binary(y, c):
    y = text(y)
    l = []
    e = y.find('.')
    i = int(y[:e])
    d = float(y[e:])
    while i != 0:
        if i % 2 == 0:
            l.append('0')
        else:
            l.append('1')
        i //= 2
    l.reverse()
    l.append('.')
    a = 0
    while d < 1:
        a += 1
        d *= 2
        f = floor(d)
        if d != f:
            l.append(str(f))
            d -= f
        else:
            l.append(str(f))
            break
        if a > c:
            break
    l = ''.join(l)
    if int(float(y)) == float(y):
        print(l[:l.find('.')])
    else:
        print(l)


def octa(y, c):
    y = text(y)
    l = []
    e = y.find('.')
    i = int(y[:e])
    d = float(y[e:])
    while i != 0:
        temp = i % 8
        l.append(str(temp))
        i //= 8
    l.reverse()
    l.append('.')
    a = 0
    while True:
        a += 1
        d *= 8
        f = floor(d)
        if d != f:
            l.append(str(f))
            d -= f
        else:
            l.append(str(f))
            break
        if a > c:
            break
    l = ''.join(l)
    if int(float(y)) == float(y):
        print(l[:l.find('.')])
    else:
        print(l)


def hexa(y, c):
    dic = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    y = text(y)
    l = []
    e = y.find('.')
    i = int(y[:e])
    d = float(y[e:])
    while i != 0:
        temp = i % 16
        temp = dic[temp]
        l.append(temp)
        i //= 16
    l.reverse()
    l.append('.')
    a = 0
    while True:
        a += 1
        d *= 16
        f = floor(d)
        if d != f:
            l.append(dic[f])
            d -= f
        else:
            l.append(dic[f])
            break
        if a > c:
            break
    l = ''.join(l)
    if int(float(y)) == float(y):
        print(l[:l.find('.')])
    else:
        print(l)


def text(z):
    if z.find('.') == -1:
        z += str('.0')
    elif z[0] == '.':
        z = str('0') + z
    return z

binary(x, b)
octa(x, b)
hexa(x, b)
