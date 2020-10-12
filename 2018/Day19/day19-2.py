# Using a given assembly-style program, determine what the register values are at the end of execution

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["#ip 0",
            "seti 5 0 1",
            "seti 6 0 2",
            "addi 0 1 0",
            "addr 1 2 3",
            "setr 1 0 0",
            "seti 8 0 4",
            "seti 9 0 5"]


# Copy all of the instructions from day 16 here for use
def addr(regs, a, b, c):
    regs[c] = regs[a] + regs[b]
    return regs


def addi(regs, a, b, c):
    regs[c] = regs[a] + b
    return regs


def mulr(regs, a, b, c):
    regs[c] = regs[a] * regs[b]
    return regs


def muli(regs, a, b, c):
    regs[c] = regs[a] * b
    return regs


def banr(regs, a, b, c):
    regs[c] = regs[a] & regs[b]
    return regs


def bani(regs, a, b, c):
    regs[c] = regs[a] & b
    return regs


def borr(regs, a, b, c):
    regs[c] = regs[a] | regs[b]
    return regs


def bori(regs, a, b, c):
    regs[c] = regs[a] | b
    return regs


def setr(regs, a, b, c):
    regs[c] = regs[a]
    return regs


def seti(regs, a, b, c):
    regs[c] = a
    return regs


def gtir(regs, a, b, c):
    regs[c] = 1 if a > regs[b] else 0
    return regs


def gtri(regs, a, b, c):
    regs[c] = 1 if regs[a] > b else 0
    return regs


def gtrr(regs, a, b, c):
    regs[c] = 1 if regs[a] > regs[b] else 0
    return regs


def eqir(regs, a, b, c):
    regs[c] = 1 if a == regs[b] else 0
    return regs


def eqri(regs, a, b, c):
    regs[c] = 1 if regs[a] == b else 0
    return regs


def eqrr(regs, a, b, c):
    regs[c] = 1 if regs[a] == regs[b] else 0
    return regs


func_table = {
    'addr': addr,
    'addi': addi,
    'mulr': mulr,
    'muli': muli,
    'banr': banr,
    'bani': bani,
    'borr': borr,
    'bori': bori,
    'setr': setr,
    'seti': seti,
    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,
    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr
}


if __name__ == '__main__':
    print("Starting Day 19-2")
    # Read file into list of values
    values = read_file('input.txt')
    # values = test_data()

    # We need to read the instructions into a list so that we can jump around to the correct spots
    program = []
    inst_reg = 0
    for val in values:
        if "#ip" in val:
            inst_reg = int(val.split()[1])
        else:
            program.append(val.split())

    # Set up the registers
    regs = [0] * 6
    # regs[0] = 1

    # Now run the program
    # For second part, find factors of 10551403
    # while regs[inst_reg] < len(program):
    #     # Get the instruction
    #     current_inst = regs[inst_reg]
    #     func,a,b,c = program[current_inst]
    #     regs = func_table[func](regs, int(a), int(b), int(c))
    #     print("After instruction {0!s}:[{1}], registers are: [{2}]".format(current_inst, ','.join([func,a,b,c]), ','.join(map(str, regs))))
    #     regs[inst_reg] += 1

    # Instead of trying to fix the program, let's just write a more efficient way of getting them
    # Start with the number itself as the loop limit, this will go down as more factors are found
    number = 10551403
    # number = 1003
    limit = number
    factor = 1
    total = 0
    while factor < limit:
        if number % factor == 0:
            total += factor
            total += int(number / factor)
            limit = int(number / factor)
        factor += 1

    print("The total is: {0!s}".format(total))

    # Print out the final registers
    print("The final registers are: {0}".format(str(regs)))
