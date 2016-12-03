
array = [None for _ in range(10001)]
array[0], array[1], array[2] = 0, 0, 1
array[3], array[4], array[5] = 1, 1, 1
array[6], array[7] = 1, 1
flag = 8


def dynamic(a):
    global flag
    if array[a-1] is not None:
        pass
    else:
        for i in range(flag, a+1):
            f1 = 1 + array[i - 3-1]
            f2 = 1 + array[i - 4-1]
            f3 = 1 + array[i - 7-1]
            if f1 % 2 != 0 or f2 % 2 != 0 or f3 % 2 != 0:
                array[i-1] = 1
            else:
                array[i-1] = 0
        flag = a-1
    return array[a-1]


t = int(input())
while t:
    if dynamic(int(input())) == 1:
        print('A')
    else:
        print('B')
    t -= 1
