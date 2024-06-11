def square(number):
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    total = 1
    for num in range(number - 1):
        total = total * 2
    return total


def total():
    total = 1
    for num in range(64):
        total = total * 2
    return total - 1


def square_better(number):
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total_better():
    return 2**64 - 1
