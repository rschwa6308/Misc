#print [int(((1+5**0.5)**n - (1-5**0.5)**n)/((2**n)*5**0.5)) for n in range(input("how many fibs?"))]
    

def fib(n):
    if n is 0:
        return 0
    elif n is 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
