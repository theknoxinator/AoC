# Determine how many groups of programs are connected to each other using pipe chains
from collections import deque


def read_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def test_data():
    return ["0 <-> 2",
            "1 <-> 1",
            "2 <-> 0, 3, 4",
            "3 <-> 2, 4",
            "4 <-> 2, 3, 6",
            "5 <-> 6",
            "6 <-> 4, 5"]


print("Starting Day12-2")
values = read_file('input.txt')
# values = test_data()

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
    print("Total found for {0!s}: {1!s}".format(origin, total))
    if total > 0:
        total_groups += 1

print("Number of iterations: {0!s}".format(iterations))
print("Number of visited nodes: {0!s}".format(len(visited)))
print("The total number of groups: {0!s}".format(total_groups))