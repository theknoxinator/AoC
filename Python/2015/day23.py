# Run instructions defined in a file to simulate a simple assembly program

def run_program(values, start_a=0):
    # First, setup the two registers and the starting instruction index
    a = start_a
    b = 0
    index = 0

    # Iterate through the program, only stopping once index is outside the bounds of the program
    while 0 <= index < len(values):
        instruction = values[index].replace(',','').split()
        if instruction[0] == "hlf":
            # Half the given register
            if instruction[1] == 'a':
                a = int(a / 2)
            elif instruction[1] == 'b':
                b = int(b / 2)
        elif instruction[0] == "tpl":
            # Triple the given register
            if instruction[1] == 'a':
                a = a * 3
            elif instruction[1] == 'b':
                b = b * 3
        elif instruction[0] == "inc":
            # Increment the register by 1
            if instruction[1] == 'a':
                a += 1
            elif instruction[1] == 'b':
                b += 1
        elif instruction[0] == "jmp":
            # Jump to new index offset to the current one, then move to that instruction immediately
            index = index + int(instruction[1])
            continue
        elif instruction[0] == "jie":
            # Jump to new index offset if register is even
            jump = False
            if instruction[1] == 'a':
                jump = (a % 2 == 0)
            elif instruction[1] == 'b':
                jump = (b % 2 == 0)
            if jump:
                index = index + int(instruction[2])
                continue
        elif instruction[0] == "jio":
            # Jump to new index offset if register is equal to 1 (one)
            jump = False
            if instruction[1] == 'a':
                jump = (a == 1)
            elif instruction[1] == 'b':
                jump = (b == 1)
            if jump:
                index = index + int(instruction[2])
                continue

        # Default increment the index by 1
        index += 1

    # Print out answer
    print("Final register values are a={0!s}, b={1!s}".format(a, b))
    return {"a": a, "b": b}


def part1(values):
    return run_program(values)


def part2(values):
    return run_program(values, 1)
