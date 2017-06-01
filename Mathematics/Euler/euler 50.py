def is_prime(n, primes):
    for p in primes:
        if n%p == 0:
            return False
    return True



cap = 1000000


primes = [2]

for n in range(3, cap):
    if is_prime(n, primes):
        primes.append(n)


print "done generating primes"

most_terms = 0
best_prime = 0

print len(primes)

for p_index in range(len(primes)):
    if p_index % 1000 == 0:
        print str(float(p_index)/len(primes)*100) + "%"
    p = primes[-1*(p_index+1)]
    for start in range(0, p_index):
        s = 0
        i = 0
        while s < p:
            s += primes[start+i]
            i += 1
        if s == p:
            if i > most_terms:
                most_terms = i
                best_prime = p
                print str(best_prime) + ": " + str(most_terms)
                print start
            









##most_terms = 0
##best_prime = 0
##
##for start in range(0,len(primes)):
##    for end in range(start, len(primes)):
##        s = sum(primes[start:end]) 
##        if s in primes:
##            if end-start > most_terms:
##                most_terms = end-start
##                best_prime = s
##                print s
##                print most_terms
##
##print s
##            


