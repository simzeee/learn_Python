"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (
    VEGAN,
    VEGETARIAN,
    KETO,
    PALEO,
    OMNIVORE,
    ALCOHOLS,
    SPECIAL_INGREDIENTS,
    example_dishes,
    EXAMPLE_INTERSECTION,
)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """

    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """

    ingredients_set = set(drink_ingredients)
    if ingredients_set.isdisjoint(ALCOHOLS):
        return drink_name + " Mocktail"
    return drink_name + " Cocktail"


def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: list - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """

    for category in [
        (VEGAN, "VEGAN"),
        (VEGETARIAN, "VEGETARIAN"),
        (KETO, "KETO"),
        (PALEO, "PALEO"),
        (OMNIVORE, "OMNIVORE"),
    ]:
        if set(dish_ingredients).issubset(category[0]):
            return dish_name + f": {category[1]}"


def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """

    comparison = set(dish[1])
    return (dish[0], comparison.intersection(SPECIAL_INGREDIENTS))


def compile_ingredients(dishes):
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """
    result = set()
    for ingredients in dishes:
        result = result.union(ingredients)
    return result


def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    new_dishes = set(dishes)
    new_appetizers = set(appetizers)

    diff = new_dishes.difference(new_appetizers)
    print("HERE", diff)
    return list(diff)


dishes = [
    "Avocado Deviled Eggs",
    "Flank Steak with Chimichurri and Asparagus",
    "Kingfish Lettuce Cups",
    "Grilled Flank Steak with Caesar Salad",
    "Vegetarian Khoresh Bademjan",
    "Avocado Deviled Eggs",
    "Barley Risotto",
    "Kingfish Lettuce Cups",
]

appetizers = [
    "Kingfish Lettuce Cups",
    "Avocado Deviled Eggs",
    "Satay Steak Skewers",
    "Dahi Puri with Black Chickpeas",
    "Avocado Deviled Eggs",
    "Asparagus Puffs",
    "Asparagus Puffs",
]


def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """

    singletons = (dish - intersection for dish in dishes)
    return set.union(*singletons)
