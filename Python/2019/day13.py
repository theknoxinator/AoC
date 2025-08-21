# Part 1: Using the same intcode runner from previous days, turn the output into a graphical display and count block tiles
# Part 2: Play the game of breakout until all blocks are removed and return the final score
from day11 import IntCodeRunner


def run_program(values, use_part2=False):
    instructions = list(map(int, values[0].split(',')))
    if use_part2:
        instructions[0] = 2
    comp = IntCodeRunner(instructions)

    # For this program, the output is that every three values indicates the x, y coordinate and type of tile
    finished = False
    last_ball_position = None
    while not finished:
        finished = comp.execute()

        index = 0
        raw_tiles = comp.outputs
        tile_map = dict()
        max_x, max_y = 0, 0
        # While we process the tiles, we should track where the ball and paddle currently are so we can compare to the
        # previous frame
        current_ball_position = last_ball_position
        current_paddle_position = (0, 0)
        while index < len(raw_tiles):
            x, y, tile_type = raw_tiles[index], raw_tiles[index + 1], raw_tiles[index + 2]
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            tile_map[(x, y)] = tile_type
            if tile_type == 3:
                current_paddle_position = (x, y)
            elif tile_type == 4:
                current_ball_position = (x, y)
            index += 3

        if not use_part2:
            # For part 1, count the number of block tiles in the map (block tiles are type=2)
            return len([x for x in tile_map.values() if x == 2])

        # For part 2, we want to be moving the paddle to stay under the ball and let the game keep running until all
        # block tiles are removed from the tile map

        # Determine whether we should move the joystick
        if current_ball_position[0] < current_paddle_position[0]:
            # Ball is to the left of the paddle, move paddle left
            comp.inputs.append(-1)
        elif current_ball_position[0] > current_paddle_position[0]:
            # Ball is to the right of the paddle, move paddle right
            comp.inputs.append(1)
        else:
            # Ball is right above paddle, do nothing until it moves again
            comp.inputs.append(0)

        last_ball_position = current_ball_position

        block_count = len([x for x in tile_map.values() if x == 2])
        if block_count < 1 or finished:
            return tile_map[(-1, 0)]



def part1(values):
    return run_program(values)


def part2(values):
    return run_program(values, True)
