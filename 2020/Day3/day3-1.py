# Determine the number of trees encountered on slope

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


print("Starting Day3-1")
values = read_file("input.txt")
# values = test_data()

# We can leave the input data as-is because strings act as arrays of characters
# For this we are incrementing x by 3 and y by 1 each cycle, until y is greater than the number of rows in values
x = 0
tree_count = 0
for y in range(1, len(values)):
    # Since the map extends to the right forever, we can determine the x-coord by modulus
    x += 3
    adjusted_x = x % len(values[y])
    if values[y][adjusted_x] == '#':
        tree_count += 1

print("The tree count is: {0!s}".format(tree_count))
