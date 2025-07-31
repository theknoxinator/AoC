# Part 1: Given a set of nanobots floating in 3D space, determine how many bots are within signal range of the strongest one
# Part 2: Using the same nanobots, find the point closest to the origin that is within the most bot ranges
import heapq
import re


def find_nearby_bots(values):
    # First parse all the nanobots into a dictionary based on the coordinates
    # At the same time, determine which bot has the largest radius
    bots = dict()
    target_bot = (0, 0, 0, 0)
    for val in values:
        x, y, z = list(map(int, re.search(r'pos=<([0-9-,]+)>', val).group(1).split(',')))
        radius = int(re.search(r'r=([0-9]+)', val).group(1))

        bots[(x, y, z)] = radius
        if radius > target_bot[3]:
            target_bot = (x, y, z, radius)

    # Now iterate through the bots again and figure out how many bots are within the radius of the target bot
    count = 0
    for bot in bots.keys():
        distance = abs(bot[0] - target_bot[0]) + abs(bot[1] - target_bot[1]) + abs(bot[2] - target_bot[2])
        if distance <= target_bot[3]:
            count += 1

    return count


def find_optimal_spot(values):
    # First parse all the nanobots into a list, since the dictionary doesn't really help with this problem
    bots = []
    for val in values:
        x, y, z = list(map(int, re.search(r'pos=<([0-9-,]+)>', val).group(1).split(',')))
        radius = int(re.search(r'r=([0-9]+)', val).group(1))
        bots.append((x, y, z, radius))

    # The last problems of this year have just been kicking my butt in terms of needing to know algorithms that I just
    # don't and online resources are not good at explaining the ones that I know can help me out, so I cheated again
    # for this one just so that I can try to understand how those algorithms work
    # A lot of the solutions just use a third-party library to figure it out for them, but I'm going with an approach
    # using boxes that get smaller but try to maintain the largest overlap with the bots ranges

    # To start with the box, we need to figure out the size of the box that will contain all bots
    farthest_point = max(max(abs(bot[i]) + bot[3] for bot in bots) for i in [0, 1, 2])
    boxsize = 1
    while boxsize <= farthest_point:
        boxsize *= 2

    # The box is represented by negative-most coordinate and positive-most coordinate of the box
    starting_box = ((-boxsize, -boxsize, -boxsize), (boxsize, boxsize, boxsize))

    # Helper function to determine how many bots ranges are in the current box
    def intersecting_bots(box):
        count = 0
        for bot in bots:
            distance = 0
            for i in [0, 1, 2]:
                # Get just the points of the current edge of the box
                box_low, box_high = box[0][i], box[1][i] - 1
                # These lines determine the distance between the bot and the closest point of the box by adding the
                # closest and furthest together, and subtracting the length of the edge, which leaves a distance of
                # 2 times the closest point (since the furthest point is the distance of the closest point plus the
                # length of the edge)
                distance += abs(bot[i] - box_low) + abs(bot[i] - box_high)
                distance -= box_high - box_low

            # Once we have the Manhattan distance of all three edges, we divide by two to remove the duplicates as
            # mentioned above
            distance = distance // 2
            # Finally check to see if the distance is within the radius of the bot (again, the distance is zero if the
            # bot is within the box
            if distance <= bot[3]:
                count += 1
        return count


    # Now for the meat of the algorithm, we start with the initial box that covers all bots on a heap. The heap is used
    # to set priority of computations on the boxes that continue to cover the largest number of bots. Since the heap
    # is designed to sort based on smallest first, we inverse the number of the bots and box size to make sure it pulls
    # the correct ones. With each box we subdivide it into 8 equal sized boxes and put those onto the heap until we
    # eventually get to a 1x1x1 box that is our answer.
    # The heap starts with: inverse of the number of all bots, the inverse length of the full box (which is boxsize * 2
    # because boxsize was relative to 0 for each axis), the Manhattan distance of the furthest point of the box, and the
    # coordinates of the box
    box_heap = [(-len(bots), -2 * boxsize, 3 * boxsize, starting_box)]
    while box_heap:
        inverse_bot_count, inverse_edge_length, furthest_point, box = heapq.heappop(box_heap)
        if abs(inverse_edge_length) == 1:
            # We have reached a box of size 1x1x1, so we are done, the furthest point is the distance of the box from
            # the origin
            return furthest_point
        # Set the new edge length (divide by negative 2 to make it positive again)
        new_edge_length = inverse_edge_length // -2
        for octant in [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]:
            # To get the new coordinates, we take the current lowest point of the box and then selectively add the new
            # edge length which is half the current length, depending on which octant it is
            new_box_low = tuple(box[0][i] + new_edge_length * octant[i] for i in [0, 1, 2])
            # Then to get the new highest point we just take the lowest point and add the edge to it
            new_box_high = tuple(new_box_low[i] + new_edge_length for i in [0, 1, 2])
            new_box = (new_box_low, new_box_high)
            new_bot_count = intersecting_bots(new_box)
            # The lowest point is not guaranteed to be the furthest or closets point to the origin, but since we keep
            # going until it's a single unit box, it's not that important
            new_furthest_point = abs(new_box_low[0]) + abs(new_box_low[1]) + abs(new_box_low[2])
            heapq.heappush(box_heap, (-new_bot_count, -new_edge_length, new_furthest_point, new_box))

    # Should never get here
    return 0


def part1(values):
    return find_nearby_bots(values)


def part2(values):
    return find_optimal_spot(values)
