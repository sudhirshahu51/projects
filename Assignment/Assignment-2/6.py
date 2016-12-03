x1, y1 = map(int, input('Enter the first coordinates with a space').split())
x2, y2 = map(int, input('Enter the first coordinates with a space').split())
x3, y3 = map(int, input('Enter the first coordinates with a space').split())
s1 = y1 * (x2 - x3)
s2 = y2 * (x3 - x1)
s3 = y3 * (x1 - x2)
s = s1 + s2 + s3
if s == 0:
    print('Points lie on the same line')
else:
    print('''points don't lie on the same line''')
