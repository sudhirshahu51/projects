def func(hash):
    if not isinstance(hash, dict):
        return 0
    else:
        tmp = list(hash.keys())
        for i in tmp:
            if hash[i] < 1:
                del hash[i]
        return len(hash)


t = int(input())
while t:
    n = int(input())
    friends = []
    score = []
    for _ in range(n):
        c, *b = map(int, input().split())
        friends.append([b, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}, c])
        score.append(c)
    for i in range(n):
        d = friends[i][1]
        for j in friends[i][0]:
            d[j] += 1
        le = func(d)
        while le > 3:
            m = min(d.values())
            if le == 6:
                score[i] += m * 4
            elif le == 5:
                score[i] += m * 2
            else:
                score[i] += m
            for k in d.keys():
                d[k] -= m
            le = func(d)
    tmp = max(score)
    if score.count(tmp) > 1:
        print('tie')
    elif score.index(tmp) == 0:
        print('chef')
    else:
        print(score.index(tmp)+1)
    t -= 1
