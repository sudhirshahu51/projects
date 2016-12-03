def min_dist(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    T = [[0 for _ in range(n1+1)] for _ in range(n2+1)]
    for j in range(n1+1):
        T[0][j] = j
    for i in range(n2+1):
        T[i][0] = i
    for i in range(1, n2+1):
        for j in range(1, n1+1):
            if s1[j-1] == s2[i-1]:
                T[i][j] = T[i-1][j-1]
            else:
                T[i][j] = min(T[i-1][j], T[i][j-1], T[i-1][j-1]) + 1
    return T[n2][n1], get_used(s1, s2, n1, n2, T)


def get_used(s1, s2, n1, n2, T):
    i = n2
    j = n1
    used = []
    while T[i][j] != 0:
        if T[i][j] == T[i-1][j-1] and s1[j-1] == s2[i-1]:
            j -= 1
            i -= 1
        elif T[i][j] == T[i][j-1] + 1:
            used.append(s1[j-1] + ' is deleted')
            j -= 1
        elif T[i][j] == T[i-1][j] + 1:
            used.append(s2[i-1] + ' is added')
            i -= 1
        elif T[i][j] == T[i-1][j-1] + 1:
            used.append(s1[j-1] + ' is edited to ' + s2[i-1])
            i -= 1
            j -= 1
    used.reverse()
    return used


a1 = input('Enter the 1st string')
a2 = input('Enter the 2nd string')
print(min_dist(a1, a2))