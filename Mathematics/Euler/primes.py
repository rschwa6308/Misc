

###################################BAD############################
def is_prime(n, primes):
    for p in primes:
        if n%p == 0:
            return False
    return True



primes = [2]

for n in range(3,1000):
    if is_prime(n, primes):
        primes.append(n)
###################################################################





#standalone efficient
isPrime(n):
    return 2 in [n,2**n%n]
