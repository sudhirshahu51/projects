def sum_digit(n):
    n = int(n)
    if int(n/10) == 0:
        return int(n*(n+1)/2)
    else:
        i = len(list(str(n)))-1
        p = 10 ** i
        m = int(n / p)
        return int((m*45*i*p/10) + (m*(m-1)*p/2) + (m*((n % p)+1)) + sum_digit(n % p))


a = 0
b = 0
while (a != -1) or (b != -1):
    x = str(input())
    l = x.split(maxsplit=3)
    a = int(l[0])
    b = int(l[1])
    sum_a = sum_digit(a-1)
    sum_b = sum_digit(b)
    ab = sum_b - sum_a
    if ab == -1:
        break
    else:
        print(ab)

'''
one important thing is the sum of 1+2+3+.........+9=45
2.now u have to find out that how many times this sum(45) will occur......
3.example::
      let u want to find out sum of digits of 1 to 52.
      then just notice how i m reaching to 52.
     i.e 1,2,3..........9
         11,12,13,...........19
         21,22,23,,,,,,,,,,,,,,,,29
         31,32,,,,,,,,,,,,,,,,,,,,,,39
         41,42,,,,,,,,,,,,,,,,,,,,,49
         10,20,30,40,50
         51,52

         just think how i m making sets....
        1. now observe how many sum(1+2+3+......+9=45)  occuring
         5 times sum(45) occuring

        2.10 times 1,10 times 2,10 times 3,10 times 4
           so i can write this sum as (1+2+3+4) *10 times
                                                 formula for this=4*5*10/2

        3.for 50,51 ,52 i.e how many times 5 occuring...
           i.e 3 times i can write this as 5*(2+1) or 5*(52%10+1)

         4.now for 0+1+2=2*3/2

so finally formula for this is
n*45*i*p/10)+ n*(n-1)*p/2+ n*(N%p+1) + sum(N%p) where p=10 to power i where i is digit(n)-1
'''
