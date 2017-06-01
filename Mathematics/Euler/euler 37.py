


def is_prime(n, primes):
    if n == 1:
        return False
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


#print primes



def is_trunc(n, primes):
    for i in range(len(str(n))):
        #print str(n)[i:]
        #print str(n)[:len(str(n))-i]
        if not is_prime(int(str(n)[i:]), primes):
            return False
        if not is_prime(int(str(n)[:len(str(n))-i]),primes):
            return False
    return True





s = 0

for n in range(8,1000000):
    if is_trunc(n, primes):
        print n
        s += n

print s






