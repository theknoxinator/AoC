# Calculate the lowest house number that gets a given number of presents assuming that elves are visiting
# houses in ascending orders
from functools import reduce

def find_house(values):
    target = int(values[0])

    all_houses = [0] * (target // 10)

    # Populate the presents for each house
    for elf in range(1, target // 10):
        for house in range(elf, target // 10, elf):
            all_houses[house] += elf * 10

    for house, total in enumerate(all_houses):
        if total >= target:
            return house


def find_house2(values):
    target = int(values[0])

    all_houses = [0] * (target // 10)

    # Populate the presents for each house
    for elf in range(1, target // 10):
        for steps in range(50):
            house = elf * (steps + 1)
            if house >= len(all_houses):
                break
            all_houses[house] += elf * 11

    for house, total in enumerate(all_houses):
        if total >= target:
            return house


def part1(values):
    return find_house(values)

def part2(values):
    return find_house2(values)
