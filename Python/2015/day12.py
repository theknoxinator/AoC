# Sum up all the numbers found in the given JSON document
import json

# Find all the numbers in the document
def recurse_json(json_part, ignore_red=False):
    subtotal = 0
    if isinstance(json_part, int):
        subtotal += json_part
    elif isinstance(json_part, str):
        pass
    elif isinstance(json_part, list):
        for value in json_part:
            subtotal += recurse_json(value, ignore_red)
    elif isinstance(json_part, dict):
        for value in json_part.values():
            if ignore_red and value == "red":
                return 0
            subtotal += recurse_json(value, ignore_red)
    return subtotal


def calc_json(json_full, ignore_red=False):
    return recurse_json(json_full, ignore_red)


def part1(values):
    return calc_json(json.loads(values[0]))


def part2(values):
    return calc_json(json.loads(values[0]), True)
