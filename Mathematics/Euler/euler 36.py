

def is_palindrome(n):
    return str(n) == str(n)[::-1]



def dec_to_bin(x):
    return int(bin(x)[2:])



s = 0

for n in range(1,1000000):
    if is_palindrome(n) and is_palindrome(dec_to_bin(n)):
        s += n

print s
