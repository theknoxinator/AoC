# Calculate the number of defined squares that overlap, and determine the exact number of square inches
# that is being overlapped

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]

if __name__ == '__main__':
    print("Starting Day3-1")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Set up array that represents the full piece of fabric (1000x1000)
    fabric = [[0]*1000 for i in range(1000)]

    # Iterate through each order and fill in the square the order represents
    for order in values:
        # Get the data we care about, split by whitespace and take the third and fourth parts
        order_parts = order.replace(':', '').split()
        # The third part is the starting point
        start_point = list(map(int, order_parts[2].split(',')))
        # The fourth part is the size of the square
        size = list(map(int, order_parts[3].split('x')))

        # Now loop through each space of the square and increment the fabric value
        for i in range(start_point[1], start_point[1] + size[1]):
            for j in range(start_point[0], start_point[0] + size[0]):
                fabric[i][j] += 1

    # Go back through the fabric and check how many spaces are above one
    total_sq = 0
    for row in fabric:
        print(''.join(map(str, row)))
        for space in row:
            if space > 1:
                total_sq += 1

    # Print out answer
    print("The total number of overlapping squares is: {0}".format(str(total_sq)))
