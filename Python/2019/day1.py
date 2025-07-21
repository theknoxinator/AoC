# Calculate the sum of fuel needed for many masses

def sum_fuel(values, use_part2=False):
    # Iterate and calculate individual fuel needs and add to total
    total = 0
    for val in values:
        mass = int(val)
        fuel = int(mass / 3) - 2
        total += fuel

        if use_part2:
            # Now calculate how much fuel the fuel needs
            mass = fuel
            while mass > 0:
                fuel = int(mass / 3) - 2
                if fuel < 0:
                    break
                total += fuel
                mass = fuel

    return total


def part1(values):
    return sum_fuel(values)


def part2(values):
    return sum_fuel(values, True)
