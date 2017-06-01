

def is_prime(n):
    for d in range(2,int(abs(n)**0.5)+1):
        if n % d == 0:
            return False
    return True



def get_primes(a,b):
    s = 0
    n = 0
    while True:
        n += 1
        if is_prime(n**2 + a*n + b):
            s += 1
        else:
            return s





best_pair = (0,0)
best_primes = 0

for a in range(-999,1000):
    for b in range(-1000,1001):
        p = get_primes(a,b)
        if p > best_primes:
            best_pair = (a,b)
            best_primes = p

print best_pair[0]*best_pair[1]
