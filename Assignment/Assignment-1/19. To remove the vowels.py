# To remove the vowels from the strings and replace it with space
l = str(input('Enter the string whose vowels is to be subtracted\n'))
x = len(l)
l=list(l)
for i in range(x):
    if l[i] in ['a', 'e', 'i', 'o', 'u',]:
        l[i] = ' '
    else:
        continue
l = ''.join(l)
print(l)
input('Press enter to exit')
