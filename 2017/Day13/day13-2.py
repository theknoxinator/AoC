# Determine the amount of time we have to wait so that we don't get caught by firewall


def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append((int(x) for x in line.strip().replace(' ', '').split(':')))
    return values


def test_data():
    return [(0,3), (1,2), (4,4), (6,4)]


print("Starting Day13-2")
# values = read_file("input.txt")
values = test_data()

# Setup our grid and starting positions
value_map = dict(values)
size = 91
lengths = [0] * size
positions = [None] * size
forward = [True] * size

for i in range(size):
    if i in value_map:
        lengths[i] = value_map[i]
        positions[i] = 0

# Now go through the firewall
current = 0
violations = []
while current < size:
    # print(lengths)
    # print(positions)
    # print(forward)
    # print()

    # Do the check first
    if positions[current] == 0:
        violations.append(current)

    # Move ourselves forward
    current += 1

    # Now tick each layer
    for i in range(size):
        # Skip if length is 0
        if lengths[i] == 0:
            continue

        # Check first to see if we need to change direction
        if forward[i] and positions[i] == lengths[i] - 1:
            forward[i] = False
        elif not forward[i] and positions[i] == 0:
            forward[i] = True

        # Now move in direction
        if forward[i]:
            positions[i] += 1
        else:
            positions[i] -= 1

severity = 0
for violation in violations:
    severity += violation * lengths[violation]

print("The violations are: {0}".format(', '.join([str(x) for x in violations])))
print("The severity is: {0!s}".format(severity))
