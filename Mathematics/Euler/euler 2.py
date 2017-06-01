from time import sleep



def fib_count(a,b,s):
    if a > 4000000:
        return s
    if a % 2 == 0:
        s += a
    return fib_count(b,a+b,s)
    


print fib_count(1,1,0)


