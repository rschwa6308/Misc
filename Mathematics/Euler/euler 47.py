def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return set(primfac)




for n in range(10000000):
    if len(primes(n)) == 4:
        if len(primes(n+1)) == 4:
            if len(primes(n+2)) == 4:
                if len(primes(n+3)) == 4:
                    print n
                    break
        
