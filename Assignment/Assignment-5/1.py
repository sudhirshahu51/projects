from math import sqrt, floor
import functools


def palindrome(x):
    y = list(x)
    y.reverse()
    y = ''.join(y)
    if x == y:
        print('The entered no. is palindrome')
    else:
        print('The entered no. is not palindrome')


def prime(x):
    flag = 0
    x = int(x)
    y = floor(sqrt(x))
    for i in range(2, y+1):
        if x % i == 0:
            flag = 1
            break
        else:
            pass
    if flag == 0:
        print('Entered no. is prime')
    else:
        print('Entered no. is not prime')


def perfect_no(x):
    x = int(x)
    d = []
    for i in range(1, x):
        if x % i == 0:
            d.append(i)
        else:
            pass
    o = functools.reduce(lambda a, b: a + b, d)
    if o == x:
        print('The entered no. is perfect no.')
    else:
        print('The entered no. is not a perfect no.')


def reverse(x):
    y = list(x)
    y.reverse()
    y = ''.join(y)
    print('The reverse of the no.', y)


def digits(x):
    print('The no. of digits', len(x))


def summing(x):
    y = list(x)
    y = list(map(int, y))
    a = 0
    for i in range(len(x)):
        a += y[i]
    print('The sum of digits', a)


def sum_factorial(x):
    d = {'0': 1, '1': 1, '2': 2, '3': 6, '4': 24, '5': 120, '6': 720, '7': 5040, '8': 40320, '9': 362880 }
    y = list(x)
    a = 0
    for i in y:
        a += d[i]
    print('The sum of factorial of digits', a)


def divisible_11(x):
    y = list(x)
    y = list(map(int, y))
    o = y[-1::-2]
    e = y[-2::-2]
    od = functools.reduce(lambda t, a: a + t, o)
    ev = functools.reduce(lambda t, a: a + t, e)
    s = od - ev
    if s % 11 == 0 or s == 0:
        print('Entered no. is divisible by 11')
    else:
        print('Entered no. is not divisible by 11')


def odd_or_even(x):
    x = str(bin(int(x)))
    if x[len(x)-1] == '1':
        print('odd')
    else:
        print('even')


def remainder(x):
    print('remainder is %s after dividing by 10' % (x[:len(x) - 1]))

t = input('Enter th no.')
palindrome(t)
prime(t)
perfect_no(t)
reverse(t)
digits(t)
summing(t)
sum_factorial(t)
divisible_11(t)
odd_or_even(t)
remainder(t)
