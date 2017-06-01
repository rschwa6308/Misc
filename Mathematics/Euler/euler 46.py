



def is_prime(n):
    if n <= 0:
        return False
    for d in range(2,int(n**0.5)+1):
        if n % d == 0:
            return False
    return True




def is_form(n):
    for base in range(1,int(n**0.5)):
        if is_prime(n - 2*(base**2)):
            return True
        
    return False







oddcomps = [x for x in range(10000) if (not is_prime(x) and x % 2 == 1)]

for n in oddcomps:
    if not is_form(n):
        print n
        break
