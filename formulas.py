def add(values):
    if values[0] == 0:
        return values[-1]
    elif values[-1] == 0:
        return values[0]
    else:
        return values[0] + values[-1]


def subtract(values):
    if values[0] == 0:
        return -(values[-1])
    elif values[-1] == 0:
        return values[0]
    else:
        return values[0] - values[-1]


def multiply(values):
    if 0 in values:
        return 0
    return values[0] * values[-1]


def divide(values):
    if values[-1] == 0:
        raise ValueError
    elif values[0] == 0:
        return 0
    else:
        return values[0] / values[-1]
