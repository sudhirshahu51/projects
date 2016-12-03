
print('This is to find out if the given sequence of puzzle can be solved')
d = {}
a = input().split()
if len(a) <= 8:
    for i in range(len(a)):
        d[i] = a[i]
d[8] = ' '
print(d)
print('|%s|%s|%s|' % (d[0], d[1], d[2]))
print('_______')
print('|%s|%s|%s|' % (d[3], d[4], d[5]))
print('_______')
print('|%s|%s|%s|' % (d[6], d[7], d[8]))
b = 0
count = 0
while b < 7:
    if d[b] > d[b +1]:
        count += 1
        b += 1
    else:
        b += 1
print(count)
