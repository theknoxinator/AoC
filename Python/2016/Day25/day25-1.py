# Run instructions defined in a file to simulate a simple assembly program

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


if __name__ == "__main__":
    print("Starting Day 25-1")
    values = read_file('input.txt')

    start_a = 0
    while True:
        # First, setup the registers and starting instruction index
        regs = {'a':start_a, 'b':0, 'c':0, 'd':0}
        index = 0

        # Iterate through the program, only stopping once index is outside the bounds of the program
        output = ""
        while 0 <= index < len(values) and len(output) < 100:
            instruction = values[index].split()
            # New this time, we need to check to make this is a valid instruction, so check in each part
            if instruction[0] == "cpy":
                if instruction[2] not in regs:
                    # Skip since the second argument is not a register
                    index += 1
                    continue
                if instruction[1] in regs:
                    regs[instruction[2]] = regs[instruction[1]]
                else:
                    regs[instruction[2]] = int(instruction[1])
            elif instruction[0] == "inc":
                if instruction[1] not in regs:
                    # Skip since the argument is not a register
                    index += 1
                    continue
                # Increment the register by one
                regs[instruction[1]] += 1
            elif instruction[0] == "dec":
                if instruction[1] not in regs:
                    # Skip since the argument is not a register
                    index += 1
                    continue
                # Decrement the register by one
                regs[instruction[1]] -= 1
            elif instruction[0] == "jnz":
                if (instruction[1] not in regs and int(instruction[1]) != 0) or \
                        (instruction[1] in regs and regs[instruction[1]] != 0):
                    if instruction[2] in regs:
                        index += regs[instruction[2]]
                    else:
                        index += int(instruction[2])
                    continue
            elif instruction[0] == "tgl":
                # New this time, toggle function changes other functions
                if instruction[1] in regs:
                    target = index + regs[instruction[1]]
                else:
                    target = index + int(instruction[1])
                if target < 0 or target >= len(values):
                    # Out of bounds target, so ignore
                    index += 1
                    continue
                if "cpy" in values[target]:
                    values[target] = values[target].replace("cpy", "jnz")
                elif "jnz" in values[target]:
                    values[target] = values[target].replace("jnz", "cpy")
                elif "inc" in values[target]:
                    values[target] = values[target].replace("inc", "dec")
                elif "dec" in values[target]:
                    values[target] = values[target].replace("dec", "inc")
                elif "tgl" in values[target]:
                    values[target] = values[target].replace("tgl", "inc")
            elif instruction[0] == "out":
                # New to this final iteration, it just outputs whatever the number or register is
                if instruction[1] in regs:
                    output += str(regs[instruction[1]])
                else:
                    output += str(instruction[1])

            # Default increment the index by 1
            index += 1

        print("Final register values are: {0}".format(regs))
        print("The output pattern is: {0}".format(output))

        passes = True
        for index in range(len(output)):
            if index % 2 != int(output[index]):
                passes = False
                break

        if passes:
            break
        else:
            start_a += 1

    print("The winning start value for a is: {0!s}".format(start_a))
