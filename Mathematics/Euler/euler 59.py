from itertools import permutations



##def is_prime_slow(n, primes):
##    for p in primes:
##        if n%p == 0:
##            return False
##    return True
##
##
##
##primes = [2]
##
##for n in range(3,10000):
##    if is_prime_slow(n, primes):
##        primes.append(n)


def is_prime_fast(n):
    return 2 in [n, 2**n%n]


print is_prime_fast(37)




def is_set(nums):
    perms = permutations(nums, 2)

    for p in perms:
        if not is_prime_fast(int(str(p[0]) + str(p[1]))):
            print int(str(p[0]) + str(p[1]))
            print p
            return False
    return True




print is_set([3, 7, 108, 673])
