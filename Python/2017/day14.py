# Part 1: Using a sequence of knot hashes (from Day10), determine how many squares on the disc are used
# Part 2: Using the same squares on the disc, determine how many regions there are with that data
from collections import deque


def gen_knot_hash(start_str, target_length):
    # Create the start state of the numbers to be knotted
    hash_nums = [i for i in range(target_length)]
    # Convert the starting string into a sequence of lengths to switch
    lengths = [ord(i) for i in list(start_str)]
    lengths += [17, 31, 73, 47, 23] # These are added to the list by the problem statement

    # Now perform all the swaps
    index, skip = 0, 0
    for _ in range(64):
        for length in lengths:
            lower = index
            upper = index + length - 1
            while upper > lower:
                swap = hash_nums[lower % target_length]
                hash_nums[lower % target_length] = hash_nums[upper % target_length]
                hash_nums[upper % target_length] = swap
                lower += 1
                upper -= 1

            # Move the index up by the length + skip, and increment the skip
            index = (index + length + skip) % target_length
            skip += 1

    # Next, perform an XOR on each block of 16 numbers to reduce to 16 values
    reduced_values = []
    for i in range(16):
        start = 16 * i
        end = start + 16
        subvalues = hash_nums[start:end]
        xor_value = subvalues[0]
        for subvalue in subvalues[1:]:
            xor_value = xor_value ^ subvalue
        reduced_values.append(xor_value)

    # Finally, convert and return the reduced values to a hex string
    return ''.join(["{0:02x}".format(x) for x in reduced_values])


def find_squares(values):
    hash_input = values[0]
    grid_size = 128
    grid = []

    # Iterate through rows 0-127, get the knot hash for each row, then convert into binary to find squares
    for i in range(grid_size):
        full_hash = "{0}-{1!s}".format(hash_input, i)
        knot_hash = gen_knot_hash(full_hash, 256)
        grid.append(f"{int(knot_hash, 16):0>128b}")

    # Now count the used squares
    total = 0
    for row in grid:
        total += row.count('1')

    # For part 2, we need to determine the regions of the squares as well
    regions = 0
    processed_squares = dict()
    queue = deque()
    for y in range(grid_size):
        for x in range(grid_size):
            # We will check every square to see if it's been processed or not
            # If the square is used and has not been processed, increase the region and then find all attached squares
            # and process them as well; if the square is free or has been processed already just continue
            if grid[y][x] == '1' and (x, y) not in processed_squares:
                regions += 1
                queue.append((x, y))
                while queue:
                    x1, y1 = queue.popleft()
                    # Skip this square if it's already been processed or is 0
                    if (x1, y1) in processed_squares or grid[y1][x1] == '0':
                        continue
                    processed_squares[(x1, y1)] = regions
                    # Add adjacent squares to queue if they exist
                    for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        x2 = x1 + offset[0]
                        y2 = y1 + offset[1]
                        if 0 <= x2 < grid_size and 0 <= y2 < grid_size:
                            queue.append((x2, y2))


    return total, regions


def part1(values):
    return find_squares(values)[0]


def part2(values):
    return find_squares(values)[1]
