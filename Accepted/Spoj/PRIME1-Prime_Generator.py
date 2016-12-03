def prime_print(lower, upper):
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
                bool_lst[i] = False         # Making all those multiples of prime_current False
        prime_index += 1
        try:
            prime_current = primes_lst[prime_index]
        except IndexError:
            break
    for x in range(length):
        if bool_lst[x]:
            print(x+lower)


primes = [True] * 31623     # Creating an list of maximum primes whose coprimes are <1000000000
primes[0] = primes[1] = False
primes_lst = []
for i in range(2, 31623):
    if primes[i]:
        primes_lst.append(i)
        n = i*i                 # n are co primes of same prime
        while n < 31623:        # making all those false who are a multiple of prime i
            primes[n] = False
            n += i
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a <= 2:
        a = 2
    prime_print(a, b)
    print()