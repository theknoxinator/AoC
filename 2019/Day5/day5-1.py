# Run a program using intcode

def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            return [int(x) for x in line.split(',')]

def test_data():
    # return [3,0,4,0,99]
    # return [1002,4,3,4,33]
    return [1101,100,-1,4,0]

print("Starting Day5")
values = read_file('input.txt')
# values = test_data()

inputs = [1]
outputs = []

# Start at index 0 and go through the program
index = 0
while index < len(values) and values[index] != 99:
    # Convert opcode into its parts
    operation = str(values[index])
    opcode = int(operation[-2:])
    first_param_flag = 0 if len(operation) < 3 else int(operation[-3])
    second_param_flag = 0 if len(operation) < 4 else int(operation[-4])
    third_param_flag = 0 if len(operation) < 5 else int(operation[-5])

    if opcode == 1:
        # Add next two parameters into third
        first_param = values[index + 1] if first_param_flag else values[values[index + 1]]
        second_param = values[index + 2] if second_param_flag else values[values[index + 2]]
        values[values[index + 3]] = first_param + second_param
        index += 4
    elif opcode == 2:
        # Multiply next two parameters into third
        first_param = values[index + 1] if first_param_flag else values[values[index + 1]]
        second_param = values[index + 2] if second_param_flag else values[values[index + 2]]
        values[values[index + 3]] = first_param * second_param
        index += 4
    elif opcode == 3:
        # Take input and save to parameter
        values[values[index + 1]] = inputs.pop(0)
        index += 2
    elif opcode == 4:
        # Take parameter and output
        first_param = values[index + 1] if first_param_flag else values[values[index + 1]]
        outputs.append(first_param)
        index += 2
    else:
        print("Found unexpected intcode: {0!s} at {1!s}".format(values[index], index))

print("Ending values: {0}".format(','.join(map(str, values))))
print("Output: {0}".format(','.join(map(str, outputs))))
