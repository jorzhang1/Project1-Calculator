import sys


def add(values):
    sum = 0
    for i in values:
        if i > 0:
            sum += i
    return sum


def subtract(values):
    new = [x for x in values if x > 0]
    if len(new) > 0:
        diff = new[0]
        for i in new[1:]:
            if i > 0:
                diff -= i
        return diff
    else:
        return 0


def multiply(values):
    new = [x for x in values if x != 0]
    if len(new) > 0:
        product = new[0]
        for i in new[1:]:
            if i != 0:
                product *= i
        return product
    else:
        return 0


def divide(values):
    quotient = values[0]
    for i in values[1:]:
        if i == 0:
            sys.exit('Cannot divide by 0')
        else:
            quotient /= i
    return quotient
