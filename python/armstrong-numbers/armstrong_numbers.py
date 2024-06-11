def is_armstrong_number(number):
    exponent = len(str(number))
    number_as_string = str(number)
    total = 0
    for num in number_as_string:
        total = total + int(num) ** exponent
    return total == number

# solution 2 using list comprehension and sum function

# def is_armstrong_number(number):
    # return sum([int(x)**len(str(number)) for x in str(number)]) == number