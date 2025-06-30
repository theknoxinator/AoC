# Get the bathroom passcode based on inputs from file
# Keypad is standard 1-9, arranged in 3x3 grid, instructions show which way to go: up, down, left, right
# Grid does not wrap so moves into wall are ignored

KEYS_1 = {
    (0,0): "1",
    (1,0): "2",
    (2,0): "3",
    (0,1): "4",
    (1,1): "5",
    (2,1): "6",
    (0,2): "7",
    (1,2): "8",
    (2,2): "9"
}

KEYS_2 = {
    (2,0): "1",
    (1,1): "2",
    (2,1): "3",
    (3,1): "4",
    (0,2): "5",
    (1,2): "6",
    (2,2): "7",
    (3,2): "8",
    (4,2): "9",
    (1,3): "A",
    (2,3): "B",
    (3,3): "C",
    (2,4): "D"
}


def press_keys(values, keys, start):
    # Go through directions to find each key to press (start at 5 key)
    x_coord, y_coord = start
    passcode = ""
    for val in values:
        # Iterate each direction in line
        for letter in val:
            if letter == 'U':
                temp = y_coord - 1
                if (x_coord, temp) in keys:
                    y_coord = temp
            elif letter == 'D':
                temp = y_coord + 1
                if (x_coord, temp) in keys:
                    y_coord = temp
            elif letter == 'L':
                temp = x_coord - 1
                if (temp, y_coord) in keys:
                    x_coord = temp
            elif letter == 'R':
                temp = x_coord + 1
                if (temp, y_coord) in keys:
                    x_coord = temp

        passcode = passcode + keys[(x_coord, y_coord)]

    return passcode


def part1(values):
    return press_keys(values, KEYS_1, (1, 1))


def part2(values):
    return press_keys(values, KEYS_2, (0, 2))
