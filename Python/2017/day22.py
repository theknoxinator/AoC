# Part 1: Given a starting grid of infected nodes, determine how many movements cause another infection after 10K iterations
# Part 2: Using the same setup, add two new status and rules, determine infections after 10 million iterations

def create_map(values):
    grid = dict()
    for y in range(len(values)):
        for x in range(len(values[y])):
            grid[(x,y)] = values[y][x]
    return grid


# Instead of a big if-else block, we can determine the new direction based on current direction and status in a dictionary
change_direction = {
    'U': {
        '.': 'L',
        '#': 'R',
        'W': 'U',
        'F': 'D',
    },
    'D': {
        '.': 'R',
        '#': 'L',
        'W': 'D',
        'F': 'U',
    },
    'R': {
        '.': 'U',
        '#': 'D',
        'W': 'R',
        'F': 'L',
    },
    'L': {
        '.': 'D',
        '#': 'U',
        'W': 'L',
        'F': 'R',
    },
}


def virus_carrier(values, iterations, use_part2=False):
    grid = create_map(values)

    # The starting position is in the very middle and starts facing up
    x, y = len(values[0]) // 2, len(values) // 2
    direction = 'U'

    infections = 0
    for _ in range(iterations):
        # Get the status of the current space
        current_status = grid[(x,y)] if (x,y) in grid else '.'

        # Change direction
        direction = change_direction[direction][current_status]

        # Change the current node status
        if current_status == '.':
            grid[(x,y)] = 'W' if use_part2 else '#'
        elif current_status == 'W':
            grid[(x,y)] = '#'
        elif current_status == '#':
            grid[(x,y)] = 'F' if use_part2 else '.'
        else:
            grid[(x,y)] = '.'
        if grid[(x,y)] == '#':
            infections += 1

        # Move forward one space
        if direction == 'U':
            y -= 1
        elif direction == 'D':
            y += 1
        elif direction == 'R':
            x += 1
        else:
            x -= 1

    # Return the number of infections that occurred during movements
    return infections


def part1(values):
    return virus_carrier(values, 10_000)


def part2(values):
    return virus_carrier(values, 10_000_000, True)
