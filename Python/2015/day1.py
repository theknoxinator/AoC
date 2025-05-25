# Determine the floor the instructions end up on
def part1(values):
    # For this we simply increment floor one for each ( and decrement for each ), no limit
    floor = 0
    for direction in values[0]:
        if direction == '(':
            floor += 1
        elif direction == ')':
            floor -= 1
    return floor


def part2(values):
    # For this part we want to stop reading as soon as we hit below 0, and return the position
    position = 0
    floor = 0
    for direction in values[0]:
        position += 1
        if direction == '(':
            floor += 1
        elif direction == ')':
            floor -= 1
        if floor < 0:
            break
    return position
