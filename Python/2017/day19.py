# Part 1: Using a maze-like diagram, determine the letters that someone tracing the diagram will cross over
# Part 2: Using the same answer as part 1, just count the number of steps taken to trace to the end

def trace_diagram(values):
    grid = [list(x) for x in values]

    # Starting position will be whichever space in the top row has a pipe '|'
    pos = grid[0].index('|'), 0
    direction = 'D'
    found = []
    steps = 1
    found_end = False
    while not found_end:
        if direction == 'D':
            pos = pos[0], pos[1] + 1
        elif direction == 'U':
            pos = pos[0], pos[1] - 1
        elif direction == 'R':
            pos = pos[0] + 1, pos[1]
        elif direction == 'L':
            pos = pos[0] - 1, pos[1]

        if not (0 <= pos[0] < len(grid[pos[1]]) and 0 <= pos[1] < len(grid)):
            # Next space is outside grid, so stop here
            found_end = True
            continue

        current_space = grid[pos[1]][pos[0]]
        if current_space.isalpha():
            # If new space is a character, we need to record it
            found.append(current_space)
        elif current_space == '+':
            # If new space is a plus '+', we need to turn
            if direction == 'D' or direction == 'U':
                left_space = grid[pos[1]][pos[0] - 1] if pos[0] > 0 else ' '
                if left_space not in '+| ':
                    # Space to the left is not empty or another path
                    direction = 'L'
                else:
                    # Assume that if left is not valid, then it must be right
                    direction = 'R'
            else:
                up_space = grid[pos[1] - 1][pos[0]] if (pos[1] > 0 and pos[0] < len(grid[pos[1] - 1])) else ' '
                if up_space not in '+- ':
                    # Space above is not empty or another path
                    direction = 'U'
                else:
                    # Assume that if up is not valid, then it must be down
                    direction = 'D'
        elif current_space == ' ':
            # We have reached the end
            found_end = True
            continue

        steps += 1

    # Return the path as a string
    return ''.join(found), steps


def part1(values):
    return trace_diagram(values)[0]


def part2(values):
    return trace_diagram(values)[1]
