import math

def is_prime(n, primes):
    for p in primes:
        if p > n**0.5:
            break
        if n%p == 0:
            return False
    return True



primes = [2]

for n in range(3,1000000):
    #print n
    if is_prime(n, primes):
        primes.append(n)



def is_circular(p, primes):
    for i in range(len(str(p))):
        if not is_prime(int(str(p)[i:] + str(p)[:i]), primes):
            return False
    if p in primes:
        return True
    else:
        return False



count = 0

for p in primes:
    if is_circular(p, primes):
        count += 1


print count
