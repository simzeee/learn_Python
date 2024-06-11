# solution 1 (mine)

# def equilateral(sides):
#     a = sides[0]
#     b = sides[1]
#     c = sides[2]
#     if is_triangle(sides):
#         return a == b and a == c
#     return False


# def isosceles(sides):
#     if is_triangle(sides):
#         return any(sides.count(x) > 1 for x in sides)
#     return False


# def scalene(sides):
#     a = sides[0]
#     b = sides[1]
#     c = sides[2]
#     if is_triangle(sides):
#         return a != b and a != c and b != c
#     return False


# def is_triangle(sides):
#     a = sides[0]
#     b = sides[1]
#     c = sides[2]
#     return a + b >= c and b + c >= a and a + c >= b and a > 0 and b > 0 and c > 0

# Solution 2

def valid_triangle(f):
    def inner(sides):
        return sum(sides) > 2 * max(sides) and f(sides)
    return inner


@valid_triangle
def equilateral(sides):
    return len(set(sides)) == 1


@valid_triangle
def isosceles(sides):
    return len(set(sides)) < 3


@valid_triangle
def scalene(sides):
    return len(set(sides)) == 3

# Solution 3 tuple unpacking

def equilateral(sides):
    a, b, c = sorted(sides)
    return 0 < a == c


def isosceles(sides):
    a, b, c = sorted(sides)
    return 0 < a and c < a + b and b in (a, c)


def scalene(sides):
    a, b, c = sorted(sides)
    return 0 < a < b < c < a + b