from itertools import permutations

def is_prime(n):
    for d in range(2,int(n**0.5)):
        if n % d == 0:
            return False
    return True



def is_sequence(nums):
    #nums = sorted(nums)
    return nums[2]-nums[1] == nums[1]-nums[0] == 3330



#print is_sequence([1487, 4817, 8147])


#loops through all 4-digit numbers
for n in range(1000,10000):
    if is_prime(n):
        perms = permutations(str(n))
        perms = set([int("".join(p)) for p in perms])

        sequs = permutations(perms, 3)
        sequs = [s for s in sequs if min(s) >= 1000]

        for s in sequs:
            if is_sequence(s):
                if is_prime(s[0]) and is_prime(s[1]) and is_prime(s[2]):
                    print "".join([str(n) for n in s])
        
        
