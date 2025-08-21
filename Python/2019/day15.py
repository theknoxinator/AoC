# Part 1: Using the same intcode runner from previous days, interact with it to move a repair droid the fewest number of movements
# Part 2: After finding the oxygen tank, figure out how long it takes for oxygen to spread through the entire map
from day11 import IntCodeRunner
import heapq


def run_program(values, use_part2=False):
    instructions = list(map(int, values[0].split(',')))
    comp = IntCodeRunner(instructions)

    # For this program, it is expected that there is always one input to tell the droid which direction to go and the
    # program will produce one output which indicates if the movement was successful or not
    # Seen tracks how many moves it took to get to that coordinate, start with origin
    seen = {(0, 0): 0}
    x, y = 0, 0
    direction = 1
    # These will be added to the current x, y to determine the new spot based on current direction
    offsets = {1: (0, 1), 2: (0 , -1), 3: (-1, 0), 4: (1, 0)}
    # This keeps track of the spaces we know we haven't seen yet for part 2
    unseen = set()
    o_tank = None

    def print_map():
        print()
        min_x = min(x[0] for x in seen.keys())
        min_y = min(x[1] for x in seen.keys())
        max_x = max(x[0] for x in seen.keys())
        max_y = max(x[1] for x in seen.keys())
        for row in range(max_y, min_y - 1, -1):
            to_print = [f'{row:3} ']
            for col in range(min_x, max_x + 1):
                if (col, row) not in seen:
                    to_print.append(' ')
                elif seen[(col, row)] == -1:
                    to_print.append('#')
                else:
                    to_print.append(str(seen[(col, row)] % 10))
            print(''.join(to_print))

    iterations = 0
    while True:
        iterations += 1
        # For part 1 we are tasked with finding the oxygen tank, which is a pathfinding algorithm similar to others
        # we've seen before. What makes this one different is that the IntCodeRunner is maintaining its own position
        # so we have to follow it instead of using a queue or heap to quickly find the shortest path. While it is not
        # possible to know the map, based on prior problems it makes sense that it's just going to be a maze of hallways
        # so the moves are limited. We will follow typical "always do X" rules and trace our way along.

        # For part 2 we still want to find the oxygen tank, but we need to map out the entire maze so that once we have
        # the whole map we can determine how long it takes for oxygen to spread to each space from the tank (at a rate
        # of one space in every direction per tick). So this time we still want to know where the tank is, but drone
        # will keep exploring until we determine there are no unseen spaces it can get to.
        dx, dy = offsets[direction]
        new_x, new_y = x + dx, y + dy
        new_move_count = seen[(x, y)] + 1

        comp.inputs.append(direction)
        finished = comp.execute()
        if finished:
            # This should theoretically never happen
            break
        result = comp.outputs.pop(0)

        if result == 0:
            # There is a wall at this coordinate, so record it as such and pull next move
            seen[(new_x, new_y)] = -1
        elif result == 2 and not use_part2:
            # We have reached the oxygen tank, we can just return from here since it should be shortest path
            return new_move_count
        else:
            # This is a valid space so we assume the robot has moved into it
            if (new_x, new_y) not in seen or seen[(new_x, new_y)] > new_move_count:
                # This is either a new space or we got here faster than previously (hopefully this doesn't happen
                # because it would mess up the other logic)
                seen[(new_x, new_y)] = new_move_count
            x, y = new_x, new_y
            if result == 2:
                # For part 2, we want to record the location of the oxygen tank for later
                o_tank = (x, y)

        # From here, check each direction and see if we should move in that direction. Obviously if we know it's a
        # wall we ignore it. We will also ignore spaces with a higher move count than the current one since it
        # indicates we already backtracked to this spot. We want to focus on unseen spaces first, and then backtrack
        # on spaces with lower move counts as the last resort.
        possible_moves = []
        for new_d in range(1, 5):
            cdx, cdy = offsets[new_d]
            check_x, check_y = x + cdx, y + cdy
            if (check_x, check_y) not in seen:
                # Haven't seen this space before, highest priority
                possible_moves.append((0, new_d))
                # Also add this space to the unseen set for tracking
                unseen.add((check_x, check_y))
            elif seen[(check_x, check_y)] < 0:
                # Space is a wall, skip
                continue
            elif seen[(x, y)] >= seen[(check_x, check_y)]:
                # We would be backtracking to this space
                possible_moves.append((1, new_d))

        if not possible_moves:
            print("Ran into a problem with drone not being able to move further")
            break

        # Set the new direction
        direction = sorted(possible_moves)[0][1]

        if not unseen:
            # We have no spaces left to check, so we should be done mapping out the maze
            break

    print_map()
    print(f'Tank is at {o_tank}')

    # Now that we have the full map, we can use our normal pathfinding algorithm with a heap to track the oxygen as it
    # spreads in all directions from the tank
    # To start we need to track all spaces that need to be oxygenated, which should be all spaces that are not walls
    need_oxygen = set(k for k,v in seen.items() if v >= 0)
    # Heap starts with tank space which gets oxygen at minute 0 (minute, x, y)
    queue = [(0, o_tank[0], o_tank[1])]
    total_minutes = 0
    while queue:
        minutes, x, y = heapq.heappop(queue)
        total_minutes = max(total_minutes, minutes)
        # This space now has oxygen
        need_oxygen.remove((x, y))
        # Spread to nearby spaces that are still in the set that needs oxygen
        for d, offset in offsets.items():
            new_x, new_y = x + offset[0], y + offset[1]
            if (new_x, new_y) in need_oxygen:
                heapq.heappush(queue, (minutes + 1, new_x, new_y))

    return total_minutes


def part1(values):
    return run_program(values)


def part2(values):
    return run_program(values, True)
