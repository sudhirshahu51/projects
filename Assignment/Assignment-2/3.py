a, b, c = map(float, input('Enter the angles of the triangle with a space').split())
if a + b + c == 180:
    print('The entered angles can form a triangle')
else:
    print('The entered angles cannot form a triangle')
