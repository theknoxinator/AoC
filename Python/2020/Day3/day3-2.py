# Determine the number of trees encountered on slope
import math

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#"]


print("Starting Day3-2")
values = read_file("input.txt")
# values = test_data()

# We can leave the input data as-is because strings act as arrays of characters
# For this we are using various increments and multiplying the results together, so make a list of slopes
slopes = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
]
tree_counts = []
for x_step, y_step in slopes:
    x = 0
    tree_count = 0
    for y in range(y_step, len(values), y_step):
        # Since the map extends to the right forever, we can determine the x-coord by modulus
        x += x_step
        adjusted_x = x % len(values[y])
        if values[y][adjusted_x] == '#':
            tree_count += 1
    tree_counts.append(tree_count)

print("The tree counts are: {0!s}".format(tree_counts))
print("The counts multiplied together is: {0!s}".format(math.prod(tree_counts)))
