# Determine how many triangle length sets are valid triangle lengths
# Second part: the sets are listed vertically, not horizontally

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values

def test_data():
    return ["5 10 25",
            "10 20 20",
            "25 15 10"]

if __name__ == '__main__':
    print("Starting Day 3-2")
    # Read file into list of values
    values = read_file('input.txt')
    # values = test_data()

    # First, we need to convert the values into a table that can be read easily
    table = []
    for val in values:
        table.append(list(map(int, val.split())))

    # Iterate and check to see if each set of values makes a valid triangle
    valid_triangles = 0
    for offset in range(0, len(table), 3):
        for col in range(3):
            sides = (table[offset][col], table[offset + 1][col], table[offset + 2][col])

            # Check each way is valid
            one_valid = sides[0] < (sides[1] + sides[2])
            two_valid = sides[1] < (sides[0] + sides[2])
            thr_valid = sides[2] < (sides[0] + sides[1])

            if one_valid and two_valid and thr_valid:
                valid_triangles += 1

    # Print out answer
    print("The number of valid triangles is: {0!s}".format(valid_triangles))