# Run a program using intcode

def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            return [int(x) for x in line.split(',')]

def test_data():
    # return [3,9,8,9,10,9,4,9,99,-1,8]
    # return [3,9,7,9,10,9,4,9,99,-1,8]
    # return [3,3,1108,-1,8,3,4,3,99]
    # return [3,3,1107,-1,8,3,4,3,99]
    # return [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    # return [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
    return [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,
            1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

print("Starting Day5-2")
# values = read_file('input.txt')
values = test_data()

inputs = [9]
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
    elif opcode == 5:
        # Jump to second parameter if first parameter is non-zero
        first_param = values[index + 1] if first_param_flag else values[values[index + 1]]
        second_param = values[index + 2] if second_param_flag else values[values[index + 2]]
        if first_param:
            index = second_param
        else:
            index += 3
    elif opcode == 6:
        # Jump to second parameter if first parameter is zero
        first_param = values[index + 1] if first_param_flag else values[values[index + 1]]
        second_param = values[index + 2] if second_param_flag else values[values[index + 2]]
        if not first_param:
            index = second_param
        else:
            index += 3
    elif opcode == 7:
        # Set third parameter to 1 if first parameter is less than second, otherwise 0
        first_param = values[index + 1] if first_param_flag else values[values[index + 1]]
        second_param = values[index + 2] if second_param_flag else values[values[index + 2]]
        values[values[index + 3]] = 1 if first_param < second_param else 0
        index += 4
    elif opcode == 8:
        # Set third parameter to 1 if first parameter is equal to second, otherwise 0
        first_param = values[index + 1] if first_param_flag else values[values[index + 1]]
        second_param = values[index + 2] if second_param_flag else values[values[index + 2]]
        values[values[index + 3]] = 1 if first_param == second_param else 0
        index += 4
    else:
        print("Found unexpected intcode: {0!s} at {1!s}".format(values[index], index))

print("Ending values: {0}".format(','.join(map(str, values))))
print("Output: {0}".format(','.join(map(str, outputs))))
