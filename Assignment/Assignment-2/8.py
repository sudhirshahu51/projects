x, y = map(int, input('Enter the coordinates of the point').split())
if x == 0 and y != 0:
    print('the point is on x axis')
elif x != 0 and y == 0:
    print('the point is on y axis')
elif x == 0 and y == 0:
    print('the point is origin')
else:
    print('the point lies between x and y axis')
