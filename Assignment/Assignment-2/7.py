a, b = map(int, input('Enter the coordinates of centre of circle by a space').split())
r = int(input('Enter the radii'))
x, y = map(int, input('Enter the coordinates of the point').split())
d = ((a - x)**2 + (b - y)**2)**.5
if d > r:
    print('The point lies outside the circle')
elif d < r:
    print('The point lies inside the circle')
else:
    print('The point lies on the circle')
