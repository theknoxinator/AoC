# Determine how many programs are connected to an initial program using pipe chains
from collections import deque

def make_connections(values):
    # First we need to process the file and determine the connections
    connections = {}
    for line in values:
        # Remove spaces, then split on the <->, and split again on the comma-separated list
        origin, pipes = line.replace(' ', '').split('<->')
        connections[origin] = pipes.split(',')

    # Next, we start from 0 and find all connections it has through chains
    total = 0
    visited = set()
    queue = deque('0')
    while queue:
        visitor = queue.popleft()
        if visitor in visited:
            continue
        visited.add(visitor)
        total += 1
        for connection in connections[visitor]:
            queue.append(connection)

    return total


def make_connections2(values):
    # First we need to process the file and determine the connections
    connections = {}
    for line in values:
        # Remove spaces, then split on the <->, and split again on the comma-separated list
        origin, pipes = line.replace(' ', '').split('<->')
        connections[origin] = pipes.split(',')

    # Next, we iterate through each node and find its group if it hasn't been found yet
    total_groups = 0
    visited = set()
    iterations = 0
    for origin in connections.keys():
        iterations += 1
        total = 0
        queue = deque([origin])
        while queue:
            visitor = queue.popleft()
            if visitor in visited:
                continue
            visited.add(visitor)
            total += 1
            for connection in connections[visitor]:
                queue.append(connection)
        if total > 0:
            total_groups += 1

    return total_groups


def part1(values):
    return make_connections(values)


def part2(values):
    return make_connections2(values)