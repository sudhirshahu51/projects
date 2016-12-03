while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        if b - a == c - b:
            print('AP %s' % (2*c - b))
        else:
            print('GP %s' % (c*(c//b)))
exit(0)
