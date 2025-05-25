# Determine how many triangle length sets are valid triangle lengths

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values

def test_data():
    return ["5 10 25"]

if __name__ == '__main__':
    print("Starting Day 3-1")
    # Read file into list of values
    values = read_file('input.txt')
    # values = test_data()

    # Iterate and check to see if each set of values makes a valid triangle
    valid_triangles = 0
    for val in values:
        # Split into three values
        sides = list(map(int, val.split()))

        # Check each way is valid
        one_valid = sides[0] < (sides[1] + sides[2])
        two_valid = sides[1] < (sides[0] + sides[2])
        thr_valid = sides[2] < (sides[0] + sides[1])

        if one_valid and two_valid and thr_valid:
            valid_triangles += 1

    # Print out answer
    print("The number of valid triangles is: {0!s}".format(valid_triangles))