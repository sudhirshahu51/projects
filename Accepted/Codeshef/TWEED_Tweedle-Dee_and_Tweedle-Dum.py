t = int(input())
while t:
    n, p = input().split()
    n = int(n)
    heap = list(map(int, input().split()))
    if p == 'Dee':
        if n == 1 and heap[0] % 2 == 0:
            print('Dee')
        else:
            print('Dum')
    else:
        print('Dum')
    t -= 1
