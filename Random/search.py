def prime_print(lower, upper):
    least_prime = {}
    length = upper - lower + 1          # length of the total numbers between upper and lower
    bool_lst = [True]*length            # Creating an list of all the numbers with initial True
    prime_current = 2                   # Initial Prime
    prime_index = 0
    while prime_current <= upper**0.5:
        index = lower % prime_current   # intial distance from the lower of the prime
        if index != 0:
            index = prime_current - index   # First occurrence of the prime in the list
        if index < length:
            if index + lower == prime_current:  # So that in the loop, first occurrence does not become False
                index += prime_current
            for i in range(index, length, prime_current):
                bool_lst[i + lower] = False         # Making all those multiples of prime_current False
                if least_prime.get(i + lower) is None:
                    least_prime[i + lower] = prime_current
        prime_index += 1
        try:
            prime_current = primes_lst[prime_index]
        except IndexError:
            break
    for x in range(length):
        if bool_lst[x]:
            least_prime[x+lower] = x + lower
    del least_prime[0]
    return least_prime

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
lst = prime_print(0, 1000000)


t = int(input())
while t:
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    output = []
    for i in range(m):
        typ, l, r = map(int, input().split())
        if typ == 0:        # update
            for j in range(l-1, r):
                try:
                    array[j] = array[j]//lst[array[j]]
                except TypeError:
                    raise AssertionError(array[j])
        else:
            result = 1
            for j in range(l-1, r):
                result = max(result, lst[array[j]])
            output.append(str(result))
    print(' '.join(output))
    t -= 1







