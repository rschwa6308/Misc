

def pent(n):
    return n*(3*n-1)/2


def is_pent(x):
    n = ((24*x+1)**0.5+1)/6
    return n == int(n)






# a>b



a = 0
done = False
while not done:
    a += 1
    for b in range(1,a):
        add = pent(a)+pent(b)
        diff = abs(pent(a)-pent(b))
        if is_pent(add) and is_pent(diff):
            print (a,b)
            print diff
            done = True
            break
            


