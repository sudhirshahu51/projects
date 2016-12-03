def converter(x):
    values = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
              'nine': 9, 'ten': 10, 'eleven': 11,
              'twelfth': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
              'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen':19,
              'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60,
              'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100,
              'lakhs': 100000, 'crores': 10000000, 'thousand': 1000, 'lakh': 100000,'crore': 10000000}
    if not isinstance(x, str):
        print('OOPS! WRONG INPUT')
        return
    l = x.split()
    if 'and' in l:
        l.pop(l.index('and'))
    if 'rupees' in l:
        l.pop(l.index('rupees'))
    if 'rupee' in l:
        l.pop(l.index('rupee'))
    for i in range(len(l)):
        if not l[i].islower():
            l[i] = l[i].lower()
    for i in range(len(l)):
        l[i] = values[l[i]]
    for i in range(len(l)-1):
        try:
            if l[i] + l[i+1] < 100:
                l[i] += l[i+1]
                l.remove(l[i+1])
        except IndexError:
            break
    for i in range(len(l)-1):
        try:
            l[i] *= l[i+1]
            l.remove(l[i+1])
        except IndexError:
            break
    return sum(l)


print('Enter the spelled integers without using and, To exit input ---')
y = input()
while y != '---':
    print(converter(y))
    y = input()
