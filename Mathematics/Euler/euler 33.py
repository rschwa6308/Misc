from fractions import gcd



def shared_digit(a,b):
    for digit in str(a):
        if digit in str(b):
            return digit
    return None



def is_form(a,b):
    if a%10 == 0 and b%10 == 0:
        return False
    
    shared = shared_digit(a,b)
    if shared is not None:
        new = (int(str(a).replace(str(shared),"",1)), int(str(b).replace(str(shared),"",1)))
        if new[0] == 0 or new[1] == 0:
            return False
        #print new
        if float(new[0])/float(new[1]) == float(a)/float(b):
            return True
        
    return False



good = []

for b in range(10,100):
    for a in range(10,b):
        #print (a,b)
        if is_form(a,b):
            print (a,b)
            good.append((a,b))



prod = [1,1]
for frac in good:
    prod[0] *= frac[0]
    prod[1] *= frac[1]

d = gcd(prod[0],prod[1])
prod[0] /= d
prod[1] /= d

print prod
















    
