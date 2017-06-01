

def is_pan(n):
    if not len(str(n)) == 9:
        return False
    digits = [1,2,3,4,5,6,7,8,9]
    for d in str(n):
        if int(d) in digits:
            digits.remove(int(d))
        else:
            return False
    if len(digits) == 0:
        return True
    else:
        return False



def concat_prod(n, prods):
    return int("".join([str(n*x) for x in prods]))






biggest = 0

for n in range(2,10):
    for a in range(1,100000):
        cp = concat_prod(a, range(1,n))
        if is_pan(cp):
            if cp > biggest:
                print (a, range(1,n))
                biggest = cp

print biggest
    
