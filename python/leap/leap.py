# def leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0 and year % 400 == 0:
#             return True
#         if year % 100 == 0 and year % 400 != 0:
#             return False
#         return True
#     return False


def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# https://exercism.org/tracks/python/exercises/leap/dig_deeper
