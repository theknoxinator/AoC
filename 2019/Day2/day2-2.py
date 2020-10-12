# Run a program using intcode

def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            return line.split(',')

def test_data():
    # return [1,9,10,3,2,3,11,0,99,30,40,50]
    # return [1,0,0,0,99]
    # return [2,3,0,3,99]
    # return [2,4,4,5,99,0]
    return [1,1,1,4,99,5,6,0,99]

print("Starting Day2-2")
values = read_file('input.txt')
# values = test_data()

values = list(map(int, values))
values[1] = 64
values[2] = 21

# Start at index 0 and go through the program
index = 0
while index < len(values) and values[index] != 99:
    if values[index] == 1:
        # Add next two positions into third
        values[values[index + 3]] = values[values[index + 1]] + values[values[index + 2]]
    elif values[index] == 2:
        # Multiple next two positions into third
        values[values[index + 3]] = values[values[index + 1]] * values[values[index + 2]]
    else:
        print("Found unexpected intcode: {0!s} at {1!s}".format(values[index], index))

    index += 4

print("Ending values: {0}".format(','.join(map(str, values))))
print("The result at position 0 is: {0!s}".format(values[0]))

print("Expected: 19690720")
print("Result:   {0!s}".format(values[0]))
