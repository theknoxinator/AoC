# Get total amount of ribbon to order for dimensions listed in file
# Dimensions are given in height x width x depth, ribbon length is calculated as the shortest diameter plus total volume
# of box

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
    print("Starting Day2-2")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Iterate and calculate shortest diameter for each box and add to total
    total_ft = 0
    for val in values:
        dimensions = list(map(int, val.split('x')))
        shortest_diameter = 2 * dimensions[0] + 2 * dimensions[1]
        second_diameter = 2 * dimensions[0] + 2 * dimensions[2]
        if second_diameter < shortest_diameter:
            shortest_diameter = second_diameter
        third_diameter = 2 * dimensions[1] + 2 * dimensions[2]
        if third_diameter < shortest_diameter:
            shortest_diameter = third_diameter

        total_ft += shortest_diameter + dimensions[0] * dimensions[1] * dimensions[2]

    # Print out answer
    print("The total feet is: {0}".format(str(total_ft)))