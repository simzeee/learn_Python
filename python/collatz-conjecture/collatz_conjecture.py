def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    steps = 0

    while number != 1:
        if number % 2 == 0:
            number = number / 2
            steps += 1
        elif number % 2 != 0:
            number = 3 * number + 1
            steps += 1

    return steps


# solution 2 using ternary

# def steps(number):
#     if number <= 0:
#         raise ValueError("Only positive integers are allowed")
#     counter = 0
#     while number != 1:
#         number = number / 2 if number % 2 == 0 else number * 3 + 1
#         counter += 1
#     return counter

# solution 3 using recursion

# def steps(number):
#     if number <= 0:
#         raise ValueError("Only positive integers are allowed")
#     if number == 1:
#         return 0
#     number = number / 2 if number % 2 == 0 else number * 3 + 1
#     return 1 + steps(number)

# cool submitted solution

# def steps(num: int, count=0):
#     if num <1:
#         raise ValueError("Only positive integers are allowed")
#     return count if num==1 else steps(3*num+1 if num %2 else num//2, count+1)
