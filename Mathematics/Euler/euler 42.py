words = open("words.txt").read()

words = words.split(",")

words = [word[1:len(word)-1] for word in words]




def get_value(word):
    return sum([ord(char)-96 for char in word.lower()])


#print get_value("SKY")




triangles = [n*(n+1)/2 for n in range(1,100)]




count = 0

for word in words:
    if get_value(word) in triangles:
        count += 1

print count
