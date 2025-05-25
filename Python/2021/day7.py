# Determine the amount of fuel it takes for the crabs to get lined on the same x position
import sys


def get_lowest_fuel(values, calculate_fuel_use):
    # First we convert the list of crabs into a list of positions for each crab
    crab_positions = [int(x) for x in values[0].split(',')]
    lowest_fuel = sys.maxsize
    lowest_position = 0

    # Next
    for position in range(min(crab_positions), max(crab_positions) + 1):
        current_fuel = 0
        for crab_position in crab_positions:
            current_fuel += calculate_fuel_use(crab_position, position)
        if current_fuel == min(current_fuel, lowest_fuel):
            lowest_fuel = current_fuel
            lowest_position = position
        else:
            break

    print(f'Lowest fuel: {lowest_fuel!s} at position: {lowest_position!s}')
    return lowest_fuel


def part1(values):
    # For part 1 the algorithm is just the distance between positions
    def calculate_fuel_use(crab_position, target_position):
        return abs(crab_position - target_position)

    return get_lowest_fuel(values, calculate_fuel_use)


def part2(values):
    # For part 2 the fuel algorithm is a famous divergent series that creates increasing triangular numbers
    def calculate_fuel_use(crab_position, target_position):
        distance = abs(crab_position - target_position)
        return int((distance * (distance + 1)) / 2)

    return get_lowest_fuel(values, calculate_fuel_use)
