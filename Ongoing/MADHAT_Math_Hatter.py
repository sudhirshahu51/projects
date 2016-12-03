def permutations(items):
    n = len(items)
    if n == 0:
        yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i] + items[i+1:]):
                yield [items[i]] + cc


def find_pupils(lst):       # lst is the list of iq
    le = len(lst)
    pupils = [0]*le
    for i in range(le):
        pupil = 0
        for j in range(i, le):
            if lst[i] < lst[j]:
                pupils[i] = pupil
                break
            elif lst[i] > lst[j]:
                pupil += 1
            pupils[i] = pupil
    return pupils


t = int(input())
while t:
    n = int(input())
    students = list(map(int, input().split()))
    count = 0
    for p in permutations(list(range(1, n+1))):
        if students == find_pupils(p):
            count += 1
    print(count % 1000000007)
    t -= 1
