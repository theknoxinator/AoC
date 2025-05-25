# Determine how many programs are connected to an initial program using pipe chains
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


print("Starting Day12-1")
values = read_file('input.txt')
# values = test_data()

# First we need to process the file and determine the connections
connections = {}
for line in values:
    # Remove spaces, then split on the <->, and split again on the comma-separated list
    origin, pipes = line.replace(' ', '').split('<->')
    connections[origin] = pipes.split(',')

print(connections)

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

print("The list of visited nodes: {0}".format(', '.join(visited)))
print("The total number visited: {0!s}".format(total))