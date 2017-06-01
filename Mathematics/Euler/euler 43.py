

##def is_pan(n):
##    digits = range(10)
##    for d in str(n):
##        if int(d) in digits:
##            digits.remove(int(d))
##        else:
##            return False
##    if len(digits) == 0:
##        return True
##    else:
##        return False



def has_prop(n):
    primes = [2,3,5,7,11,13,17]
    for i in range(1,8):
        #print int(str(n)[i:i+3])
        #print primes[i-1]
        if not int(str(n)[i:i+3]) % primes[i-1] == 0:
            return False
    return True



#has_prop(1406357289)


from itertools import permutations

digits = range(10)

perms = permutations(digits)

s = 0
for n in perms:
    x = int("".join([str(digit) for digit in n]))
    if has_prop(x):
        print x
        s += x

print s
