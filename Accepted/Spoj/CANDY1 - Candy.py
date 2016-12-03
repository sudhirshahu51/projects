while True:
    x = int(input())
    if x == -1:
        break
    else:
        l = []
        s = 0
        for _ in range(x):
            temp = int(input())
            l.append(temp)
            s += temp
        if s/x != int(s/x):
            print('-1')
            continue
        else:
            avg = s//x
            b = 0
            for j in range(len(l)):
                if l[j] > avg:
                    t = l[j] - avg
                    b += t
                else:
                    continue
    print(b)
