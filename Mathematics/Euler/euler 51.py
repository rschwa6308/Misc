from itertools import combinations

def is_prime(n, primes):
    for p in primes:
        if n%p == 0:
            return False
    return True


global primes
primes = [2]

for n in range(3,100000):
    if is_prime(n, primes):
        primes.append(n)





def get_replacements(n):
    return [int(n.replace("*", str(x))) for x in range(0,10)]


def family(parent):
    members = []
    for n in get_replacements(parent):
        if is_prime(n, primes):
            members.append(n)
    return members



for p in primes:
    digits = len(str(p))
    for stars in range(1, digits+1):
        perms = combinations(range(digits), stars)
        for perm in perms:
            parent = list(str(p))
            for pos in perm:
                parent[pos] = "*"
            parent = "".join(parent)
            #print str(p) + ": " + str(parent)
        print family(parent)
        if len(family(parent)) == 8:
            print parent
            break
