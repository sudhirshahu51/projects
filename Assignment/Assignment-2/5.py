l = int(input('Enter the length of the rectangle'))
b = int(input('Enter the breadth of the rectangle'))
p = 2 * (l + b)
a = l * b
if p > a:
    print('perimeter is greater than area')
elif p < a:
    print('perimeter is lesser than area')
else:
    print('perimeter and area is')