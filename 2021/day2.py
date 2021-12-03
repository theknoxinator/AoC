# Determine the amount of movement from the start
def part1(values):
    # We are moving along a 2D plane so we just track the movement by x and y
    x, y = 0, 0
    for movement in values:
        direction, amount = movement.split()
        if direction.lower() == 'forward':
            x += int(amount)
        elif direction.lower() == 'up':
            y -= int(amount)
        elif direction.lower() == 'down':
            y += int(amount)
    print(f'x: {x!s}, y: {y!s}')
    return x * y


def part2(values):
    # Largely the same as before but now keep track of aim which goes up and down
    x, y, aim = 0, 0, 0
    for movement in values:
        direction, amount = movement.split()
        if direction.lower() == 'forward':
            x += int(amount)
            y += int(amount) * aim
        elif direction.lower() == 'up':
            aim -= int(amount)
        elif direction.lower() == 'down':
            aim += int(amount)
    print(f'x: {x!s}, y: {y!s}')
    return x * y
