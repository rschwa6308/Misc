modules = map(int, open("Problem 1 input.txt").read().split("\n"))


def fuel_from_mass(mass):
    val = mass // 3 - 2
    if val <= 0:
        return 0
    else:
        return val + fuel_from_mass(val)


total = 0
for mass in modules:
    total += fuel_from_mass(mass)
print(total)