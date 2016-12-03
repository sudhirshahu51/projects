primes = [True] * 1000     # Creating an list of maximum primes whose coprimes are <1000000000
primes[0] = primes[1] = False
primes_lst = []
for i in range(2, 1000):
    if primes[i]:
        primes_lst.append(i)
        n = i*i                 # n are co primes of same prime
        while n < 1000:        # making all those false who are a multiple of prime i
            primes[n] = False
            n += i
lst = primes_lst


def least_prime_divisor(num):
    if num == 1:
        return 1
    elif num in lst:
        return num
    else:
        for i in lst:
            if num % i == 0:
                return i


t = int(input())
while t:
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    output = []
    for i in range(m):
        typ, l, r = map(int, input().split())
        if typ == 0:        # update
            for j in range(l-1, r):
                array[j] = array[j]//least_prime_divisor(array[j])
        else:
            result = 1
            for j in range(l-1, r):
                result = max(result, least_prime_divisor(array[j]))
            output.append(str(result))
    print(' '.join(output))
    t -= 1
