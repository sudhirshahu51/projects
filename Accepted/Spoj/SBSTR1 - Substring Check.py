def sub_string(x, y):
    flag = 0
    if isinstance(x, str) and isinstance(y, str):
        x += '0'
        x = list(x)
        y = list(y)
        for i in range(5):
            if x[i:5 + i] == y:
                flag += 1
            else:
                continue
    return flag


for _ in range(24):
    l = str(input()).split()
    a = str(l[0])
    b = str(l[1])
    if len(a) == 10 and len(b) == 5:
        if sub_string(a, b) > 0:
            print('1')
        elif sub_string(a, b) == 0:
            print('0')
    else:
        break

