def gcd(x, y):      # Finding the gcd for finding lcm
    if x == 0:
        return y
    else:
        return gcd(y % x, x)


def lcm(x, y):      # Finding the next common interval after which sensor will stop
    return (x * y)//gcd(x, y)


def min_matrix(m):
    min_value = min(m[0])
    for i in range(len(m)):
        tmp = min(m[i])
        if tmp < min_value:
            min_value = tmp
    return min_value


t = int(input())
while t:
    n = int(input())
    sensors = list(map(int, input().split()))
    matrix = [[0 for _ in range(len(sensors))] for __ in range(len(sensors))]
    for i in range(len(sensors)):
        for j in range(len(sensors)):
            if i == j:
                matrix[i][j] = 1000000001
            else:
                matrix[i][j] = lcm(sensors[i], sensors[j])
    print(min_matrix(matrix))
    t -= 1
