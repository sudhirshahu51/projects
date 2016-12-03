a = int(input('Enter a positive integer'))
a %= 10
d = {'case 0': a,
     'case 1': a,
     'case 2': a,
     'case 3': a,
     'case 4': a,
     'case 5': a,
     'case 6': a,
     'case 7': a,
     'case 8': a,
     'case 9': a}
b = 'case ' + str(a)
c = d[b]
print('rem is %d' % c)