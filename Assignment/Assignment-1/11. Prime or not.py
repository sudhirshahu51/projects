# To find a given number is prime or not
print("enter the no. to be checked of prime or not")
n = float(input())
f = 0
x=int(n/2)
for i in range(2,x):
    if n % i == 0:
        f = f + 1
    else:
        continue
if f == 0:
    print('the given no. is prime')
else:
    print('the given no. is not prime')
input('press enter to exit')