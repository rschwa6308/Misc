import math


def is_prime(n, primes):
    for p in primes:
        if p > math.sqrt(n):
            break
        if n%p == 0:
            return False
        
    return True




def is_prime2(n):
    return 2 in [n,2**n%n]



primes = [2]

for i in range(1,1000000):
    n = 2*i+1
    if (n-1) % 100000 == 0:
        print n
    #print n
    if is_prime(n, primes):
        primes.append(n)



print sum(primes)
