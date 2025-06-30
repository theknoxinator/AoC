# Run instructions defined in a file to simulate a simple assembly program

def run_program(values, c_value=0):
    # First, setup the registers and the starting instruction index
    regs = {'a':0, 'b':0, 'c':c_value, 'd':0}
    index = 0

    # Iterate through the program, only stopping once index is outside the bounds of the program
    while 0 <= index < len(values):
        instruction = values[index].split()
        if instruction[0] == "cpy":
            # Copy value/register into register
            if instruction[1] in regs:
                regs[instruction[2]] = regs[instruction[1]]
            else:
                regs[instruction[2]] = int(instruction[1])
        elif instruction[0] == "inc":
            # Increment the register by one
            regs[instruction[1]] += 1
        elif instruction[0] == "dec":
            # Decrement the register by one
            regs[instruction[1]] -= 1
        elif instruction[0] == "jnz":
            # Jump if register is not zero
            if (instruction[1] not in regs and int(instruction[1]) != 0) or \
                    (instruction[1] in regs and regs[instruction[1]] != 0):
                index += int(instruction[2])
                continue

        # Default increment the index by 1
        index += 1

    return regs


def part1(values):
    return run_program(values)


def part2(values):
    return run_program(values, 1)
