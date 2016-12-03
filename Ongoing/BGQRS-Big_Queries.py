t = int(input())
while t:
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    for _ in range(m):
        tmp = list(map(int, input().split()))
        if len(tmp) == 3:
            two, five = 0, 0
            arr = array[tmp[1]:tmp[2]+1]
            for i in arr:
                if i % 2 == 0:
                    two += 1

                if i % 5 == 0:
                    five += 1
                print(min(two, five))
    t -= 1
