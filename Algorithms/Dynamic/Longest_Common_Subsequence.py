def common_sub_seq(s1, s2):
    T = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
    for i in range(1, len(s2)+1):
        for j in range(1, len(s1)+1):
            if s2[i-1] == s1[j-1]:
                T[i][j] = T[i-1][j-1] + 1
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
    return T[len(s2)][len(s1)], sub_seq(s1, s2, T)


def sub_seq(s1, s2, T):
    used = []
    i = len(s2)
    j = len(s1)
    while T[i][j] != 0:
        if T[i][j] == T[i][j-1]:
            j -= 1
        elif T[i][j] == T[i-1][j]:
            i -= 1
        else:
            used.append(s2[i-1])
            j -= 1
            i -= 1
    used = used[::-1]
    return ''.join(used)


s1 = input('Enter the first sequence')
s2 = input('Enter the second sequence')
print(common_sub_seq(s1, s2))