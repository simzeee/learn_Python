def response(hey_bob):

    if hey_bob == "" or hey_bob.isspace():
        return "Fine. Be that way!"
    elif hey_bob[-1] == "?" and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob.strip()[-1] == "?":
        return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."


# solution 2 if statements

# def response(hey_bob):
#     hey_bob = hey_bob.rstrip()
#     if not hey_bob:
#         return 'Fine. Be that way!'
#     is_shout = hey_bob.isupper()
#     is_question = hey_bob.endswith('?')
#     if is_shout and is_question:
#         return "Calm down, I know what I'm doing!"
#     if is_shout:
#         return 'Whoa, chill out!'
#     if is_question:
#         return 'Sure.'
#     return 'Whatever.'

# solution 3 nested if statements

# def response(hey_bob):
#     hey_bob = hey_bob.rstrip()
#     if not hey_bob:
#         return 'Fine. Be that way!'
#     is_shout = hey_bob.isupper()
#     is_question = hey_bob.endswith('?')
#     if is_shout:
#         if is_question:
#             return "Calm down, I know what I'm doing!"
#         return 'Whoa, chill out!'
#     if is_question:
#         return 'Sure.'
#     return 'Whatever.'
