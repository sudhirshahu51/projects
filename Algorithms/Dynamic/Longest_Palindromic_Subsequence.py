def palindrome_sequence(l):
    n = len(l)
    m = l[:]
    T = [[1 for _ in range(n+1)] for _ in range(n+1)]
    a = 1
    while a != n:
        i = 0
        while i != n-a:
            j = i + a
            if l[i] == m[j]:
                T[i][j] = T[i+1][j-1] + 2
            else:
                T[i][j] = max(T[i][j-1], T[i+1][j])
            i += 1
        a += 1
    return T[0][-2], get_used(l, T, n)


def get_used(l,  T, n):
    used = [None for _ in range(T[0][-2])]
    i = 0
    j = n - 1
    x = 0
    while i != j:
        if T[i][j] == T[i+1][j]:
            i += 1
        elif T[i][j] == T[i][j-1]:
            j -= 1
        else:
            used[x], used[-1-x] = l[i], l[i]
            j -= 1
            i += 1
            x += 1
    used[x] = l[i]
    return ''.join(used)


l = input('Enter the string')
print(palindrome_sequence(l))
