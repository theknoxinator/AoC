# Determine the largest value in any register at the any time after a bunch of instructions


def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["b inc 5 if a > 1",
            "a inc 1 if b < 5",
            "c dec -10 if a >= 1",
            "c inc -20 if c == 10"]


if __name__ == "__main__":
    print("Starting Day 8-1")
    values = read_file("input.txt")
    # values = test_data()

    # Start with a register dict
    regs = {}

    # Now iterate through each instruction and determine what to do
    highest = 0
    for val in values:
        # Split the instruction by the if statement
        parts = val.split("if")

        # Look at the second part first and determine if we need to do the first part
        condition = parts[1].strip().split()
        # First get the values from the condition
        reg_name = condition[0]
        comp = condition[1]
        value = int(condition[2])

        # Determine the register value
        if reg_name in regs:
            reg_value = regs[reg_name]
        else:
            reg_value = 0

        # Now do the comparison
        passed = False
        if comp == '<':
            # Less than
            passed = reg_value < value
        elif comp == '>':
            # Greater than
            passed = reg_value > value
        elif comp == '<=':
            # Less than or equal to
            passed = reg_value <= value
        elif comp == '>=':
            # Greater than or equal to
            passed = reg_value >= value
        elif comp == '==':
            # Equal to
            passed = reg_value == value
        elif comp == '!=':
            # Not equal to
            passed = reg_value != value

        if passed:
            # The condition is true, so execute the first part
            statement = parts[0].strip().split()
            reg_name = statement[0]
            if reg_name not in regs:
                regs[reg_name] = 0
            inst = statement[1]
            value = int(statement[2])

            if inst == 'inc':
                # Increment
                regs[reg_name] += value
            elif inst == 'dec':
                # Decrement
                regs[reg_name] -= value

            if regs[reg_name] > highest:
                highest = regs[reg_name]

    for reg_name, reg_value in regs.items():
        print("Reg {0}: {1!s}".format(reg_name, reg_value))
        if reg_value > highest:
            highest = reg_value
    print("The highest register value at any time is: {0!s}".format(highest))
