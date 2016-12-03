def nxt(y):
    l = len(y)
    ys = list(y)
    ysc = ys[:]
    if y in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:       # checking for 1 digit only
        return int(y) + 1
    elif y == '9'*l:                      # checking for 99* terms
        return int('1' + '0'*(len(y) - 1) + '1')
    elif l % 2 != 0:                    # if odd
        m = (l + 1)//2
        ysc[m:] = ys[-(m+1)::-1]
        if int(''.join(ysc)) <= int(''.join(ys)):
            t = 0
            for j in range(m):
                if ysc[m - 1 - j] == '9':
                    ysc[m - 1 - j] = '0'
                    t += 1
            ysc[m - 1 - t] = str(int(ysc[m - 1 - t]) + 1)
            ysc[m:] = ysc[-(m+1)::-1]
        return int(''.join(ysc))
    else:                # if even
        m = l//2
        ysc[m:] = ys[-(m+1)::-1]
        if int(''.join(ysc)) <= int(''.join(ys)):
            t = 0
            for j in range(m):
                if ysc[m - 1 - j] == '9':
                    ysc[m - 1 - j] = '0'
                    t += 1
            ysc[m - 1 - t] = str(int(ysc[m - 1 - t]) + 1)
            ysc[m:] = ysc[-(m+1)::-1]
        return int(''.join(ysc))


def palin(x):
    return x == x[::-1]

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    summ = 0
    while a <= b:
        a1 = nxt(str(a))
        if a1 < b:
            summ += a1
        else:
            break
        a = a1
    print(summ)
