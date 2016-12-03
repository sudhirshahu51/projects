# To find the no. of divisors of a given no.
f = 0
n = int(input("Enter the no whose divisors to be found\n"))
print('the following are the divisors')
for i in range(1, n):
    if n % i == 0:
        f += 1
        print(i)
    else:
        continue
print(f, 'is the total no. of divisors')
input('press enter to exit')