# Part 1: Given a method for generating regions with erosion levels, determine the risk level of a rectangle of regions
# Part 2: Using the same generated region, determine the quickest route to the target with tool requirements in place
import heapq


def generate_regions(depth, target):
    # For part 1 we only care about the rectangle between the origin and the target but part 2 requires the known area
    # to be bigger, so we will extend it by 1000 spaces in each direction
    erosion_grid = dict()
    for y in range(target[1] + 1000):
        for x in range(target[0] + 1000):
            geologic_index = 0
            if (x == 0 and y == 0) or (x == target[0] and y == target[1]):
                # Special case for the origin and target space, they are always 0 for the geo index
                pass
            elif x == 0:
                # For all spaces along the left edge, the geo index is 48271 times Y
                geologic_index = 48271 * y
            elif y == 0:
                # For all spaces along the top edge, the geo index is 16807 times X
                geologic_index = 16807 * x
            else:
                # For all other spaces, multiply the erosion levels of (x - 1, y) and (x, y - 1)
                geologic_index = erosion_grid[(x - 1, y)] * erosion_grid[(x, y - 1)]

            # Now that we have the geo index, we find the erosion level using (geo index + depth) % 20183
            erosion_grid[(x, y)] = (geologic_index + depth) % 20183

    return erosion_grid


def find_risk_level(values):
    # Get the depth and target coordinates from the values
    depth = int(values[0].split()[1])
    target = tuple(map(int, values[1].split()[1].split(',')))

    erosion_grid = generate_regions(depth, target)

    # For part 1 we sum the risk levels of all the spaces we care about, just modulo 3 to figure out the risk level
    return sum(erosion_grid[(x, y)] % 3 for x in range(target[0] + 1) for y in range(target[1] + 1))


def find_path(values):
    # Get the depth and target coordinates from the values
    depth = int(values[0].split()[1])
    target = tuple(map(int, values[1].split()[1].split(',')))

    erosion_grid = generate_regions(depth, target)

    # For path 2 we are doing a pathfinding adventure to figure out the quickest way to the target
    # Since I looked up other solutions to figure out why I was messing up part 1 (it was because I couldn't read), I
    # discovered that my usual method of pathfinding with a queue is better done with a heap that keeps pushing the
    # currently quickest option to you instead of just iterating through every option
    # The queue contains a tuple of (minutes, x, y, tool) where tool: 0 = neither, 1 = torch, 2 = climbing gear
    # The tools are labeled this way because the risk level indicates which tool is NOT allowed there
    queue = [(0, 0, 0, 1)]
    quickest_map = dict()

    while queue:
        minutes, x, y, tool = heapq.heappop(queue)
        quickest_key = (x, y, tool)
        if quickest_key in quickest_map and quickest_map[quickest_key] <= minutes:
            # We've already been here just as quick or quicker, so don't continue this path
            continue
        # This is the quickest we've been here
        quickest_map[quickest_key] = minutes

        # If we've made it to the target, then we can just return here since the heap ensures this is the quickest
        # current path
        # Note that tool must be the torch to end per the problem
        if x == target[0] and y == target[1] and tool == 1:
            return minutes

        # We are not at the end and can keep going, so we want to add all available options
        # First, add the option to switch tools, which takes 7 minutes (there is only one option since one tools is
        # equipped and one tool is not allowed on our current region
        for i in range(3):
            if i != tool and i != erosion_grid[(x, y)] % 3:
                heapq.heappush(queue, (minutes + 7, x, y, i))

        # Second, move in all possible directions (cannot go off the map or on a region where our tool is disallowed)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x = x + dx
            new_y = y + dy
            if new_x < 0 or new_y < 0 or tool == erosion_grid[(new_x, new_y)] % 3:
                continue
            heapq.heappush(queue, (minutes + 1, new_x, new_y, tool))

    # We should never get here, but just return 0 as an error if we do
    return 0


def part1(values):
    return find_risk_level(values)


def part2(values):
    return find_path(values)
