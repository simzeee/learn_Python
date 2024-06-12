def convert(number):
    result = ""
    if number % 3 == 0:
        result = result + "Pling"
    if number % 5 == 0:
        result = result + "Plang"
    if number % 7 == 0:
        result = result + "Plong"
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return str(number)
    return result


# refactored version of my solution
# def convert(num):
#     sounds = ''

#     if num % 3 == 0: sounds += 'Pling'
#     if num % 5 == 0: sounds += 'Plang'
#     if num % 7 == 0: sounds += 'Plong'

#     return sounds if sounds else str(num)

# using ternary

# def convert(number):
#     threes = "" if number % 3 else "Pling"
#     fives = "" if number % 5 else "Plang"
#     sevens = "" if number % 7 else "Pling"

#     return f"{threes}{fives}{sevens}" or str(number)

# def convert(number):
#     threes = 'Pling' if not number % 3 else '' # Sound if there is NOT a remainder
#     fives =  'Plang' if not number % 5 else ''
#     sevens = 'Plong' if not number % 7 else ''
    
#     return f'{threes}{fives}{sevens}' or str(number)

# def convert(number):
#     sounds = ''
#     drops = ("i", 3), ("a", 5), ("o", 7)

#     for vowel, factor in drops:
#         if number % factor == 0:
#             sounds += f'Pl{vowel}ng'
    
#     return sounds or str(number)

# using join

# def convert(number):
#     drops = ["Pling","Plang","Plong"]
#     factors = [3,5,7]
#     sounds = ''.join(drops[index] for 
#                      index, factor in 
#                      enumerate(factors) if (number % factor == 0))

#     return sounds or str(number)


# arguably the "best"

# def convert(number):
    #This is clear and easily added to.  Unless the factors get
    # really long, this won't take up too much memory.
    # sounds = {3: 'Pling',
    #           5: 'Plang', 
    #           7: 'Plong'}

    # results = (sound for 
    #            divisor, sound in sounds.items()
    #            if number % divisor == 0)

    # return ''.join(results) or str(number)


# https://exercism.org/tracks/python/exercises/raindrops/dig_deeper