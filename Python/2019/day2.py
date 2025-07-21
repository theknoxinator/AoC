# Run a program using intcode

def run_program(values, noun=12, verb=2):
    instructions = list(map(int, values[0].split(',')))
    if len(instructions) > 10:
        instructions[1] = noun
        instructions[2] = verb

    # Start at index 0 and go through the program
    index = 0
    while index < len(instructions) and instructions[index] != 99:
        if instructions[index] == 1:
            # Add next two positions into third
            instructions[instructions[index + 3]] = instructions[instructions[index + 1]] + instructions[instructions[index + 2]]
        elif instructions[index] == 2:
            # Multiple next two positions into third
            instructions[instructions[index + 3]] = instructions[instructions[index + 1]] * instructions[instructions[index + 2]]
        else:
            print("Found unexpected intcode: {0!s} at {1!s}".format(instructions[index], index))

        index += 4

    return instructions[0]


def part1(values):
    return run_program(values)


def part2(values):
    return run_program(values, 64, 21)
