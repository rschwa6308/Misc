from fractions import gcd


def simp(n, d):

    div = gcd(n, d)

    return (n/div, d/div)




def root2(level, (n, d)):
    #print (n, d)
    if level == 1:
        return simp(n + d, n)
    else:
        return root2(level - 1, simp(2*n + d, n))




print root2(993, (2, 1))



count = 0

for level in range(1, 1001):
    try:
        exp = root2(level, (2, 1))
    except:
        print "error at level " + str(level)
        break

    if len(str(exp[0])) > len(str(exp[1])):
        count += 1
        print level



print count + 1         #misses one instance above limit of python float size
