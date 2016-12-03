a, b, c = map(int, input('Enter the sides of the triangle with spaces').split())
if a + b > c and b + c > a and c + a > b:
    print('The triangle is possible')
else:
    print('The triangle is not possible')
