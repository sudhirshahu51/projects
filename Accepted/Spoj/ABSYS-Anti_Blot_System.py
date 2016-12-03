t = int(input())
while t:
    t -= 1
    s = input()
    if s == '':
        t += 1
    else:
        x, y = s.split('+')
        y, z = y.split('=')
        first, second, third = x.strip(), y.strip(), z.strip()
        if first.isdecimal() and second.isdecimal():
            third1 = int(first) + int(second)
            print('%s + %s = %s' % (first, second, third1))
        elif second.isdecimal() and third.isdecimal():
            first1 = int(third) - int(second)
            print('%s + %s = %s' % (first1, second, third))
        elif first.isdecimal() and third.isdecimal():
            second1 = int(third) - int(first)
            print('%s + %s = %s' % (first, second1, third))
        else:
            print('%s + %s = %s' % (first, second, third))
