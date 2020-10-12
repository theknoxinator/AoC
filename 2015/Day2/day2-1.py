# Get total amount of wrapping paper to order for dimensions listed in file
# Dimensions are given in height x width x depth, surface area is calculated as each side plus smallest side once as extra

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    #return ["2x3x4"]
    return ["1x1x10"]

if __name__ == '__main__':
    print("Starting Day2")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Iterate and calculate surface area for each box and add to total
    total_sqft = 0
    for val in values:
        dimensions = list(map(int, val.split('x')))
        first_side = dimensions[0] * dimensions[1]
        smallest_side = first_side
        second_side = dimensions[0] * dimensions[2]
        if second_side < smallest_side:
            smallest_side = second_side
        third_side = dimensions[1] * dimensions[2]
        if third_side < smallest_side:
            smallest_side = third_side

        total_sqft += 2 * first_side + 2 * second_side + 2 * third_side + smallest_side

    # Print out answer
    print("The total square feet is: {0}".format(str(total_sqft)))