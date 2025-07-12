# Using a given assembly-style program, determine what the register values are at the end of execution

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


def run_program(values):
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

    # Now run the program
    # For first part, find factors of 1003 (1 + 17 + 59 + 1003 = 1080)
    while regs[inst_reg] < len(program):
        # Get the instruction
        current_inst = regs[inst_reg]
        func,a,b,c = program[current_inst]
        regs = func_table[func](regs, int(a), int(b), int(c))
        regs[inst_reg] += 1

    return regs[0]


def find_factor(_values):
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
    return total


def part1(values):
    return run_program(values)


def part2(values):
    return find_factor(values)
