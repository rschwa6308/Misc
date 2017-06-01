

ones = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

teens = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}


tens = {
    0: '',
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}





def spell(n):

    if n < 10:
        return ones[n]

    if 10 <= n < 20:
        return teens[n]

    elif 20 <= n < 100:
        return tens[int(str(n)[0])] + ones[int(str(n)[1])]

    elif 100 <= n < 1000:
        return ones[int(str(n)[0])] + "hundred" + ("and","")[str(n)[1:] == "00"] + spell(int(str(n)[1:]))

    elif n == 1000:
        return "onethousand"



chars = 0

for n in range(1,1001):
    print spell(n)
    chars += len(spell(n))

print chars





