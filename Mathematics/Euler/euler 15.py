
from math import factorial




def find_routes(size):
    #permutations of 20 R's and 20 D's
    return factorial(size*2)/(factorial(size)**2)


print find_routes(2)

print find_routes(20)
