# Determine how far the ship gets after following a bunch of movement instructions

def ship_movement(values):
    # Ship starts at 0,0, looking to the E
    direction = 'E'
    x, y = 0, 0
    for val in values:
        instruction = val[0]
        number = int(val[1:])
        # If the instruction is F, then we just convert it to the direction we are facing
        if instruction == 'F':
            instruction = direction

        if instruction == 'N':
            # Go north (negative y)
            y = y - number
        elif instruction == 'S':
            # Go south (positive y)
            y = y + number
        elif instruction == 'W':
            # Go west (negative x)
            x = x - number
        elif instruction == 'E':
            # Go east (positive x)
            x = x + number

        # For the R and L instructions, we convert the degrees into turns then loop that number of times in the direction
        turns = int(number / 90)
        for turn in range(turns):
            if instruction == 'L':
                if direction == 'N':
                    direction = 'W'
                elif direction == 'W':
                    direction = 'S'
                elif direction == 'S':
                    direction = 'E'
                elif direction == 'E':
                    direction = 'N'
            elif instruction == 'R':
                if direction == 'N':
                    direction = 'E'
                elif direction == 'E':
                    direction = 'S'
                elif direction == 'S':
                    direction = 'W'
                elif direction == 'W':
                    direction = 'N'

    # After doing all the movements, figure out the distance traveled
    return abs(x) + abs(y)


def ship_movement2(values):
    # Ship starts at 0,0, looking to the E
    # Waypoint starts at 10, -1 (east 10, north 1)
    x, y = 0, 0
    point_x, point_y = 10, -1
    for val in values:
        instruction = val[0]
        number = int(val[1:])

        # If the instruction is F, then we move that number of waypoints
        if instruction == 'F':
            for times in range(number):
                x += point_x
                y += point_y

        if instruction == 'N':
            # Move waypoint north (negative y)
            point_y -= number
        elif instruction == 'S':
            # Move waypoint south (positive y)
            point_y += number
        elif instruction == 'W':
            # Move waypoint west (negative x)
            point_x -= number
        elif instruction == 'E':
            # Move waypoint east (positive x)
            point_x += number

        # For the R and L instructions, we convert the degrees into turns then loop that number of times in the direction
        turns = int(number / 90)
        for turn in range(turns):
            if instruction == 'L':
                # 10, -4 -> -4, -10 -> -10, 4 -> 4, 10 -> 10, -4
                old_x, old_y = point_x, point_y
                point_x = old_y
                point_y = -old_x
            elif instruction == 'R':
                # 10, -4 -> 4, 10 -> -10, 4 -> -4, -10 -> 10, -4
                old_x, old_y = point_x, point_y
                point_x = -old_y
                point_y = old_x

    # After doing all the movements, figure out the distance traveled
    return abs(x) + abs(y)


def part1(values):
    return ship_movement(values)


def part2(values):
    return ship_movement2(values)
