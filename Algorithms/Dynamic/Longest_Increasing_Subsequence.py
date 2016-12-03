def inc_sub_sequence(l):
    n = len(l)
    a = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if l[j] < l[i]:
                a[i] = max(a[i], a[j] + 1)
    print(a[n-1])


l = list(map(int, input('Enter the sequence with spaces bet them').split()))
inc_sub_sequence(l)
