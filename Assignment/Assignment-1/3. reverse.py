x=int(input("Enter the no.:"))
y=str(x)
y=len(y)
digits=[]
for i in range(y):
    n=i+1
    rem=int(x/10**i)
    ld=rem%(10)
    dl=str(ld)
    digits.append(dl)
    

print(digits)
new=''.join(digits)
print('reverse of the entered no. is ',new)
