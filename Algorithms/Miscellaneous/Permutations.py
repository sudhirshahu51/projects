def permutations(items):
    n = len(items)
    if n == 0:
        yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i] + items[i+1:]):
                print(items[i], cc)
                yield [items[i]] + cc


def k_permutations(items, n):
    if n == 0:
        yield []
    else:
        for i in range(len(items)):
            for ss in k_permutations(items, n-1):
                if not items[i] in ss:
                    yield [items[i]] + ss


for p in k_permutations([1,2,3,4], 3):
    print('ans', p)