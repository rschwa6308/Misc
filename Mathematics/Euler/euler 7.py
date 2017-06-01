


def is_prime(n, primes):
    for p in primes:
        if n%p == 0:
            return False
    return True



primes = [2]

for n in range(2,10000000):
    #print n
    if is_prime(n, primes):
        primes.append(n)
    if len(primes) == 10001:
        print n



print max(primes)
