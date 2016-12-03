# To copy one string to another string
s1 = str(input("Enter the 1st string\n"))
s2 = str(input("Enter the 2nd string (string to be copied)\n"))
l1 = list(s1)
l2 = list(s2)
l1.append(' ')
for i in range(len(s2)):
    l1.append(l2[i])
l3 = ''.join(l1)
print(l3)
input('enter to exit')
