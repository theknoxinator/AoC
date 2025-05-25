# Determine how many steps it takes to get out of an instruction jumping "maze"


def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(int(line))

    return values


def test_data():
    return [0, 3, 0, 1, -3]


if __name__ == "__main__":
    print("Starting Day 5-2")
    values = read_file("input.txt")
    # values = test_data()

    # Start at the beginning and jump the number specified, incrementing the instruction before the jump
    steps = 0
    index = 0
    while 0 <= index < len(values):
        to_jump = values[index]
        # For second part, only increment if jump is less than three, otherwise decrement
        if to_jump >= 3:
            values[index] -= 1
        else:
            values[index] += 1
        index = index + to_jump
        steps += 1

    print("The number of steps it took was: {0!s}".format(steps))
