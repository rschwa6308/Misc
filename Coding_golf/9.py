from random import randint
print [x for x in [randint(0,25) for _ in range(100)] if x in [randint(0,25) for _ in range(100)]]
