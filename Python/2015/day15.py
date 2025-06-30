# Determine the best ratio of ingredients to make the highest scoring cookie
import itertools

class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)


def generate_amounts(length):
    all_amounts = itertools.product(range(101), repeat=length)
    for amounts in all_amounts:
        if sum(amounts) == 100:
            yield amounts


def create_cookie(values, cal_total=0):
    # First, create a list of ingredient objects that holds their stats
    ingredient_list = []
    for val in values:
        items = val.replace(':','').replace(',','').split()
        ingredient_list.append(Ingredient(items[0], items[2], items[4], items[6], items[8], items[10]))

    # Create tracker for current amount of each ingredient
    all_amounts = generate_amounts(len(ingredient_list))

    # Calculate scores and shift amounts until maximum is reached
    def calculate_score(amounts, cal_total=0):
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        calories = 0
        for index in range(len(amounts)):
            amount = amounts[index]
            ingredient = ingredient_list[index]
            capacity += amount * ingredient.capacity
            durability += amount * ingredient.durability
            flavor += amount * ingredient.flavor
            texture += amount * ingredient.texture
            calories += amount * ingredient.calories

        if capacity < 0:
            capacity = 0
        if durability < 0:
            durability = 0
        if flavor < 0:
            flavor = 0
        if texture < 0:
            texture = 0
        if 0 < cal_total != calories:
            return 0

        total = capacity * durability * flavor * texture

        return total

    highest = 0
    for amounts in all_amounts:
        highest = max(calculate_score(amounts, cal_total), highest)
    return highest


def part1(values):
    return create_cookie(values)


def part2(values):
    return create_cookie(values, 500)
