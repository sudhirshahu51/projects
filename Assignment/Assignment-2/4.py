a = input('Enter the no.')
if a[0] == '-':
    a = list(a)
    print(''.join(a[1:]))
else:
    print(a)
