t = int(input())
while t:
    s = input()
    length = len(s)
    zeros = s.count('1')
    if length == 1:
        print('Yes')
    else:
        if zeros == length:
            print('No')
        elif zeros == 0:
            print('No')
        elif zeros == 1:
            print('Yes')
        elif zeros == length - 1:
            print('Yes')
        else:
            print('No')
    t -= 1
