def add(values) -> float:
    """
    Method add two numbers

    Returns:
        float: The sum of the two numbers.
    """
    if values[0] == 0:
        return values[-1]
    elif values[-1] == 0:
        return values[0]
    else:
        return values[0] + values[-1]


def subtract(values) -> float:
    """
    Method subtract two numbers

    Returns:
        float: The result of subtracting the second number from the first.
    """
    if values[0] == 0:
        return -(values[-1])
    elif values[-1] == 0:
        return values[0]
    else:
        return values[0] - values[-1]


def multiply(values) -> float:
    """
    Method multiply two numbers.

    Returns:
        float: The product of the two numbers.
    """
    if 0 in values:
        return 0
    return values[0] * values[-1]


def divide(values) -> float:
    """
    Method divide two numbers.

    Raises:
        ValueError: If the second number is zero.

    Returns:
        float: The result of dividing the first number by the second.
    """
    if values[-1] == 0:
        raise ValueError("Cannot divide by 0")
    elif values[0] == 0:
        return 0
    else:
        return values[0] / values[-1]
