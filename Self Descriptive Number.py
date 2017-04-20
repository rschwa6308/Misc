


def check_digits(digits):
    for index in range(len(digits)):
        digits[index] = digits.count(index)

        print digits
        return check_digits(digits)


