# Count the frequency of different letters in strings
st = str(input("Enter the string\n"))
s = list(st)
x = len(s)
f = 0
c = str(input("Enter the letter whose frequency is to be found"))
for i in range(x):
    if s[i] == c:
        f += 1
    else:
        continue
print('''the frequency of letter {c}  is  {f}'''.format(**locals()))
input('press enter to exit')