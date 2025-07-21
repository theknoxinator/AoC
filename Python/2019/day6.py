# Determine the number of orbits
from collections import deque

def find_orbits(values):
    # Iterate through list of orbits and construct the map
    nodes = {}
    roots = set()
    leafs = set()
    for val in values:
        left, right = val.split(')')
        roots.add(left)
        leafs.add(right)
        if left not in nodes:
            nodes[left] = [right]
        else:
            nodes[left].append(right)

    roots = roots - leafs

    # Now go through the map and add up all the orbits
    orbits = 0
    queue = deque([(x, 0) for x in roots])
    while queue:
        parent, depth = queue.popleft()
        if parent not in nodes:
            continue
        children = nodes[parent]
        orbits += len(children) * (depth + 1)
        for child in children:
            queue.append((child, depth + 1))

    return orbits


def find_closest(values):
    # Iterate through list of orbits and construct the map
    nodes = {}
    parents = {}
    for val in values:
        left, right = val.split(')')
        parents[right] = left
        if left not in nodes:
            nodes[left] = [right]
        else:
            nodes[left].append(right)

    # Find the orbits of YOU and SAN, determine the closest node
    visited = set()
    common = 'COM'
    queue = deque(['YOU', 'SAN'])
    while queue:
        child = queue.popleft()
        if child not in parents:
            continue
        parent = parents[child]
        if parent in visited:
            common = parent
            continue
        visited.add(parent)
        queue.append(parent)

    # Now calculate the length it takes to get there
    jumps = 0
    queue = deque(['YOU', 'SAN'])
    while queue:
        child = queue.popleft()
        parent = parents[child]
        if parent == common:
            continue
        jumps += 1
        queue.append(parent)

    return jumps


def part1(values):
    return find_orbits(values)


def part2(values):
    return find_closest(values)
