from math import log

new = []

numbers = open("p099_base_exp.txt").read()

lines = numbers.split("\n")

lines = [line.split(",") for line in lines]

for line in lines:
    new.append(float(line[1])*log(float(line[0])))
        

print new.index(max(new))+1
