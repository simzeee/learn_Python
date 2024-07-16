def value_of_card(card):
    royal = ("J", "Q", "K")
    if card in royal:
        return 10
    if card == "A":
        return 1
    return int(card)


def higher_card(card_one, card_two):
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    if card_one_value == card_two_value:
        return card_one, card_two
    if card_one_value > card_two_value:
        return card_one
    return card_two


def value_of_ace(card_one, card_two):
    if card_one == "A" or card_two == "A":
        return 1
    return 11 if (value_of_card(card_one) + value_of_card(card_two) <= 10) else 1


def is_blackjack(card_one, card_two):
    if card_one == "A" and value_of_card(card_two) == 10:
        return True
    if card_two == "A" and value_of_card(card_one) == 10:
        return True
    return False
#   return (card_one == 'A' and value_of_card(card_two) == 10) or (card_two == 'A' and value_of_card(card_one) == 10)

def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):

    value = value_of_card(card_one) + value_of_card(card_two)
    return 9 <= value < 12
