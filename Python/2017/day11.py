# Determine how far away a hex is

def move_hexes(values):
    dirs = values[0].split(',')

    # The way a hex grid works, moving up or down, you move 2 on the y axis, and any other direction moves 1 in both axes
    x,y = 0,0
    max_distance = 0
    for dir in dirs:
        if dir == 'n':
            y += 2
        elif dir == 's':
            y -= 2
        elif dir == 'nw':
            x -= 1
            y += 1
        elif dir == 'ne':
            x += 1
            y += 1
        elif dir == 'sw':
            x -= 1
            y -= 1
        elif dir == 'se':
            x += 1
            y -= 1

        # To get the distance, it is as simple as adding the x and y ranges, then dividing by 2
        distance = int((abs(x) + abs(y)) / 2)
        max_distance = max(max_distance, distance)

    return distance, max_distance


def part1(values):
    return move_hexes(values)[0]


def part2(values):
    return move_hexes(values)[1]
