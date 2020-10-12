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
            "K)L"]

print("Starting Day6")
values = read_file('input.txt')
# values = test_data()

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
print("The roots of the map are: {0!s}".format(','.join(roots)))

# Now go through the map and add up all the orbits
orbits = 0
# queue = deque([(x, 0) for x in roots])
queue = deque([('COM', 0)])
while queue:
    parent, depth = queue.popleft()
    if parent not in nodes:
        continue
    children = nodes[parent]
    orbits += len(children) * (depth + 1)
    for child in children:
        queue.append((child, depth + 1))

print("The total number of orbits is: {0!s}".format(orbits))
