def is_sequence(digits):

    #all unique numbers
    for i in range(len(digits)):
        #print i
        if digits.count(str(i)) != 1:
            #print "failed count"
            return False
    #print "passed count"
    digits = "".join(digits)
    for i in range(len(digits)):
        test = int(digits[:i+1])
        #print test
        if test % (i+1) != 0:
            return False

    return True

#ANSWER:
#38164729

my_digits = list(str(3816457290))

print is_sequence(my_digits)


for i in range(10000000,99999999):
    digits = list(str(i))
    digits.insert(4, '5')
    digits.insert(9,'0')
    #print digits

    show = digits
    #print show
    show = int("".join(show))
    if i % 1000000 == 0:
        print show
    
    if is_sequence(digits):
        print i
        break
