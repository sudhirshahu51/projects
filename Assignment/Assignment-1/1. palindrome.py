x=int(input("Enter the no.:"))
y=str(x)
y=len(y)
digits=[]
for i in range(y):
    n=i+1
    rem=int(x/10**i)
    ld=rem%(10)
    digits.append(ld)
new=digits[:]
#checking
last=0
for i in range(y):
    item=digits[i]*10**(y-i-1)
    last=item+last
if last==x:
    print("Entered no. is a palindrome")
else:
    print("Entered no. is not a palindrome")
