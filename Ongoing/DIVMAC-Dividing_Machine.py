def prime_print(lower):
    lst = []
    least_prime = {}
    length = 1000001          # length of the total numbers between upper and lower
    bool_lst = [True]*length            # Creating an list of all the numbers with initial True
    prime_current = 2                   # Initial Prime
    prime_index = 0
    while prime_current <= 1000:
        index = prime_current   # First occurrence of the prime in the list
        if index < length:
            if index + lower == prime_current:  # So that in the loop, first occurrence does not become False
                index += prime_current
            for i in range(index, length, prime_current):
                bool_lst[i] = False         # Making all those multiples of prime_current False
                if least_prime.get(i) is None:
                    least_prime[i] = prime_current
        prime_index += 1
        try:
            prime_current = primes_lst[prime_index]
        except IndexError:
            break
    for x in range(length):
        if bool_lst[x]:
            least_prime[x] = x
    del least_prime[0]
    for i in range(1, len(least_prime)):
        lst.append(least_prime[i])
    return lst


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
lst = prime_print(0)


t = int(input())
while t:
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    output = []
    for i in range(m):
        typ, l, r = map(int, input().split())
        if typ == 0:        # update
            for j in range(l-1, r):
                array[j] = array[j]//lst[array[j]-1]
        else:
            tmp = []
            for j in range(l-1, r):
                tmp.append(lst[array[j]-1])
            output.append(str(max(tmp)))
    print(' '.join(output))
    t -= 1
