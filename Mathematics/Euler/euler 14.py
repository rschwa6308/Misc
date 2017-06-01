
def collatz(n, step):
    if n == 1:
        return step
    
    if n % 2 == 0:
        return collatz(n/2, step+1)
    else:
        return collatz(3*n+1, step+1)



biggest = 0
starting = 0
for n in range(1,1000000):
    c = collatz(n,1)
    if c > biggest:
        biggest = c
        starting = n



print starting
