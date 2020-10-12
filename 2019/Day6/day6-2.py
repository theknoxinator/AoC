# Determine the number of orbits
from collections import deque

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values

def test_data():
    return ["COM)B",
            "B)C",
            "C)D",
            "D)E",
            "E)F",
            "B)G",
            "G)H",
            "D)I",
            "E)J",
            "J)K",
            "K)L",
            "K)YOU",
            "I)SAN"]

print("Starting Day6-2")
values = read_file('input.txt')
# values = test_data()

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

print ("The common node is: {0}".format(common))

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

print("The total number of jumps is: {0!s}".format(jumps))
