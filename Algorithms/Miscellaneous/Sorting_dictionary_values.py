def sorting(d):
    if not isinstance(d, dict):
        return
    l = []
    for x in d.keys():
        if len(l) == 0:
            l.append(x)
        else:
            flag = 0
            for y in range(len(l)):
                if d[l[y]] <= d[x]:
                    pass
                else:
                    l.insert(y, x)
                    flag = 1
                    break
            if flag == 0:
                if d[l[y]] <= d[x]:
                    l.append(x)
    return l


if __name__ == '__main__':
    d = {'a': 3, 'b': 5, 'c': 1, 'e': 9, 'f': 2}
    print(sorting(d))