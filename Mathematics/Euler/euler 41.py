




def is_pan(n):
    digits = range(1,len(str(n))+1)
    for d in str(n):
        if int(d) in digits:
            digits.remove(int(d))
        else:
            return False
    if len(digits) == 0:
        return True
    else:
        return False





def is_prime(n, primes):
    for p in primes:
        if p > n**0.5:
            break
        if n%p == 0:
            return False
    return True


primes = [2]

biggest = 0

for n in range(3,10000000):
    #print n
    if is_prime(n, primes):
        primes.append(n)
        if is_pan(n):
            print n
            biggest = n
        

print biggest









