

names = open("names.txt").read().split(",")



names.sort()

names = [name[1:len(name)-1] for name in names]



alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def get_value(name):
    value = 0
    for char in name:
        
        value += (alpha.index(char) + 1)
    return value





s = 0
for i in range(len(names)):
    s += get_value(names[i])*(i+1)

print s
