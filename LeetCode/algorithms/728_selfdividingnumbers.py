"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
"""


def selfDividingNumbers(self, left, right):
    result = []
    for number in range(left, right + 1):
        is_valid = True
        for digit in str(number):
            digit = int(digit)
            if digit == 0 or number % digit != 0:
                is_valid = False
                break
        if is_valid:
            result.append(number)

    return result
