# Run a program using intcode

def run_program(values, inputs):
    instructions = list(map(int, values[0].split(',')))
    outputs = []

    # Start at index 0 and go through the program
    index = 0
    while index < len(instructions) and instructions[index] != 99:
        # Convert opcode into its parts
        operation = str(instructions[index])
        opcode = int(operation[-2:])
        first_param_flag = 0 if len(operation) < 3 else int(operation[-3])
        second_param_flag = 0 if len(operation) < 4 else int(operation[-4])
        third_param_flag = 0 if len(operation) < 5 else int(operation[-5])

        if opcode == 1:
            # Add next two parameters into third
            first_param = instructions[index + 1] if first_param_flag else instructions[instructions[index + 1]]
            second_param = instructions[index + 2] if second_param_flag else instructions[instructions[index + 2]]
            instructions[instructions[index + 3]] = first_param + second_param
            index += 4
        elif opcode == 2:
            # Multiply next two parameters into third
            first_param = instructions[index + 1] if first_param_flag else instructions[instructions[index + 1]]
            second_param = instructions[index + 2] if second_param_flag else instructions[instructions[index + 2]]
            instructions[instructions[index + 3]] = first_param * second_param
            index += 4
        elif opcode == 3:
            # Take input and save to parameter
            instructions[instructions[index + 1]] = inputs.pop(0)
            index += 2
        elif opcode == 4:
            # Take parameter and output
            first_param = instructions[index + 1] if first_param_flag else instructions[instructions[index + 1]]
            outputs.append(first_param)
            index += 2
        elif opcode == 5:
            # Jump to second parameter if first parameter is non-zero
            first_param = instructions[index + 1] if first_param_flag else instructions[instructions[index + 1]]
            second_param = instructions[index + 2] if second_param_flag else instructions[instructions[index + 2]]
            if first_param:
                index = second_param
            else:
                index += 3
        elif opcode == 6:
            # Jump to second parameter if first parameter is zero
            first_param = instructions[index + 1] if first_param_flag else instructions[instructions[index + 1]]
            second_param = instructions[index + 2] if second_param_flag else instructions[instructions[index + 2]]
            if not first_param:
                index = second_param
            else:
                index += 3
        elif opcode == 7:
            # Set third parameter to 1 if first parameter is less than second, otherwise 0
            first_param = instructions[index + 1] if first_param_flag else instructions[instructions[index + 1]]
            second_param = instructions[index + 2] if second_param_flag else instructions[instructions[index + 2]]
            instructions[instructions[index + 3]] = 1 if first_param < second_param else 0
            index += 4
        elif opcode == 8:
            # Set third parameter to 1 if first parameter is equal to second, otherwise 0
            first_param = instructions[index + 1] if first_param_flag else instructions[instructions[index + 1]]
            second_param = instructions[index + 2] if second_param_flag else instructions[instructions[index + 2]]
            instructions[instructions[index + 3]] = 1 if first_param == second_param else 0
            index += 4
        else:
            print("Found unexpected intcode: {0!s} at {1!s}".format(instructions[index], index))

    return ''.join(map(str, outputs))


def part1(values):
    return run_program(values, [1])


def part2(values):
    return run_program(values, [5])
