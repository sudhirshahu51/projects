test_cases = int(input())
while test_cases:
    input()
    test_cases -= 1
    if test_cases == '':
        test_cases += 1
    else:
        ng, nm = map(int, input().split())
        ng_list = []
        ng_max = -1
        for i in list(map(int, input().split())):
            if ng_max < i:
                ng_max = i
            ng_list.append(i)
        nm_list = []
        nm_max = -1
        for i in list(map(int, input().split())):
            if nm_max < i:
                nm_max = i
            nm_list.append(i)
        if ng_max >= nm_max:
            print('Godzilla')
        elif nm_max > ng_max:
            print('MechaGodzilla')
        else:
            print('uncertain')