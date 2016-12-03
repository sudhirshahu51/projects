# To find out the no. of vowels in the given string
ch = input('enter the string to find the no. of vowels\n ')
l = len(ch)
d = 0

vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(l):
    if ch[i] in vowels:
        d = d + 1
print(d)
input('press enter to exit')

