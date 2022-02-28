def is_prime(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0: return False
    return True




MAX = 50_000_000
# MAX = 100


primes = []
for n in range(2, int(MAX ** 0.5) + 1):
    if is_prime(n):
        # print(n)
        primes.append(n)


p2 = [p for p in primes if p**2 < MAX]
p3 = [p for p in primes if p**3 < MAX]
p4 = [p for p in primes if p**4 < MAX]

print(len(p2), len(p3), len(p4))
print(len(p2)*len(p3)*len(p4))

nums = set()
for a in p2:
    for b in p3:
        for c in p4:
            n = a**2 + b**3 + c**4
            if n < MAX:
                nums.add(n)

# print(list(sorted(nums)))
print(len(nums))