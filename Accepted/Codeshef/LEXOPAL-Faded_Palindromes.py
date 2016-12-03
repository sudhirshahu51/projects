t = int(input())
while t:
    s = list(input())
    length = len(s)
    missing = s.count('.')
    if length % 2 == 0:
        flag = True
        for i in range(length//2):
            if s[i] == s[-i-1] != '.':
                pass
            elif s[i] == '.':
                if s[-i-1] != '.':
                    s[i] = s[-i-1]
                else:
                    s[i] = 'a'
                    s[-i-1] = 'a'
            elif s[-i-1] == '.':
                if s[i] != '.':
                    s[-i-1] = s[i]
                else:
                    s[i] = 'a'
                    s[-i-1] = 'a'
            else:
                flag = False
                break
        if flag:
            print(''.join(s))
        else:
            print('-1')
    else:
        flag = True
        for i in range(length//2):
            if s[i] == s[-i-1] != '.':
                flag = True
            elif s[i] == '.':
                if s[-i-1] != '.':
                    s[i] = s[-i-1]
                else:
                    s[i] = 'a'
                    s[-i-1] = 'a'
            elif s[-i-1] == '.':
                if s[i] != '.':
                    s[-i-1] = s[i]
                else:
                    s[i] = 'a'
                    s[-i-1] = 'a'
            else:
                flag = False
                break
        if flag:
            if s[length//2] == '.':
                s[length//2] = 'a'
            print(''.join(s))
        else:
            print('-1')
    t -= 1
