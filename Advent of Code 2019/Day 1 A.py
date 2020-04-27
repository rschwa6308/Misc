modules = map(int, open("Problem 1 input.txt").read().split("\n"))
total = 0
for mass in modules:
    total += mass // 3 - 2
print(total)