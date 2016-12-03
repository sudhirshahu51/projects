# To compare two strings
s1 = input("Enter the 1st string\n")
s2 = input("Enter the 2nd string\n")

f = 0
if s1 > s2:
    c=s1
else:
    c=s2
for i in range(len(c)):
    if s1[i] == s2[i]:
        f += 1
    else :
        continue
if f == len(c):
    print("The two entered strings are same")
else :
    print("The two entered strings are not same")
input("Press enter to exit")
