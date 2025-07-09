# Determine how many steps it takes to get out of an instruction jumping "maze"

def find_steps(values, use_part2=False):
    values = list(map(int, values))

    # Start at the beginning and jump the number specified, incrementing the instruction before the jump
    steps = 0
    index = 0
    while 0 <= index < len(values):
        to_jump = values[index]
        if use_part2 and to_jump >= 3:
            # For second part, only increment if jump is less than three, otherwise decrement
            values[index] -= 1
        else:
            values[index] += 1
        index = index + to_jump
        steps += 1

    return steps


def part1(values):
    return find_steps(values)


def part2(values):
    return find_steps(values, True)
