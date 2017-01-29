# Code Chef Cats and Dogs problem

t = int(input())        # No. of test cases
while t:
    cats, dogs, legs = map(int, input().split())
    high = (cats + dogs) * 4        # when all the cats and dogs legs are touching ground
    if (cats - (2 * dogs)) <= 0:
        low = (dogs * 4)            # only dogs legs are touching ground
    else:
        low = (cats - dogs) * 4     # cats no. are greater than twice of dogs
    if legs % 4 == 0 and low <= legs <= high:
        print('yes')
    else:
        print('no')
    t -= 1
