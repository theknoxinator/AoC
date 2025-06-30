# Find the shortest path that crosses all of the numbers on the floor
from collections import deque
from itertools import permutations

def find_path(values, use_part2=False):
    # First, we need to create our map
    points = {}
    grid = []
    for line in values:
        grid.append(list(line))

    # Debug print out the map and get the points
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != '#' and grid[y][x] != '.':
                points[grid[y][x]] = (x, y)

    # Now for the hard part, getting the shortest paths between each pair of points
    paths = {}
    for point,start in points.items():
        queue = deque()
        distances = {}
        x, y = start
        queue.append((x, y, 0))
        while len(queue) > 0:
            x, y, cur_dist = queue.popleft()
            if (x,y) not in distances:
                distances[(x,y)] = cur_dist
            elif cur_dist < distances[(x,y)]:
                distances[(x,y)] = cur_dist
            else:
                # Distance to get to this node is longer than prior distance so just move on
                continue

            # Go up
            if grid[y-1][x] != '#':
                queue.append((x, y - 1, cur_dist + 1))
            # Go left
            if grid[y][x-1] != '#':
                queue.append((x - 1, y, cur_dist + 1))
            # Go right
            if grid[y][x+1] != '#':
                queue.append((x + 1, y, cur_dist + 1))
            # Go down
            if grid[y+1][x] != '#':
                queue.append((x, y + 1, cur_dist + 1))

        # Calculate the paths
        paths[point] = {}
        for target,end in points.items():
            if point == target:
                continue
            paths[point][target] = distances[end]

    # With the paths now calculated, we can determine the shortest path to hit every point
    full_paths = {}
    for full_path in list(permutations(map(str, range(1, len(points))))):
        total_dist = 0
        prev = '0'
        for next in full_path:
            total_dist += paths[prev][next]
            prev = next
        if use_part2:
            total_dist += paths[prev]['0']
        full_paths[full_path] = total_dist

    # Debug print out all paths
    shortest_path = None
    shortest_dist = 9999999
    for full_path,dist in full_paths.items():
        if dist < shortest_dist:
            shortest_dist = dist
            shortest_path = full_path

    print("The shortest path is 0,{0} with a distance of {1!s}".format(','.join(shortest_path), shortest_dist))
    return shortest_dist


def part1(values):
    return find_path(values)


def part2(values):
    return find_path(values, True)
