# Determine which sample operations match at least three different opcodes of an available 16
from common import read_file


def check_operations(values, use_part2=False):
    # We need to be able to read in each sample as: the registers before the operation, the operation, and
    # the registers after the operation
    befores = []
    operations = []
    afters = []
    for val in values:
        if val == "":
            continue
        elif "Before" in val:
            before_regs = list(map(int, val.replace('[','').replace(']','').replace(',','').split()[1:]))
            befores.append(before_regs)
        elif "After" in val:
            after_regs = list(map(int, val.replace('[','').replace(']','').replace(',','').split()[1:]))
            afters.append(after_regs)
        else:
            operations.append(list(map(int, val.split())))

    if len(befores) != len(operations) != len(afters):
        print("Problem with the parsing")

    samples = []
    for index in range(len(befores)):
        samples.append((befores[index], operations[index], afters[index]))

    # Now that we have all our samples, we need to define the opcodes
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

    all_opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

    def exec(func, sample):
        # This will actually test the given opcode and return True if the output matches expected
        input,operation,output = sample
        opcode,a,b,c = operation
        result = func(input.copy(), a, b, c)
        return result == output

    if use_part2:
        # Iterate through each sample and determine how many opcodes end with expected output. If three or more
        # opcodes match, then increment the samples found.
        known_opcodes = {
            0: eqir,
            1: addi,
            2: gtir,
            3: setr,
            4: mulr,
            5: seti,
            6: muli,
            7: eqri,
            8: bori,
            9: bani,
            10: gtrr,
            11: eqrr,
            12: addr,
            13: gtri,
            14: borr,
            15: banr}
        opcode_matches = {}
        for sample in samples:
            opcode = sample[1][0]
            if opcode in known_opcodes.keys():
                continue
            for func in all_opcodes:
                func_name = func.__name__
                if func in known_opcodes.values():
                    continue
                if exec(func, sample):
                    if opcode not in opcode_matches:
                        opcode_matches[opcode] = {}
                    if func_name not in opcode_matches[opcode]:
                        opcode_matches[opcode][func_name] = 1
                    else:
                        opcode_matches[opcode][func_name] += 1

        # Now that we know what the different opcodes are, let's run the actual program in input2
        program = read_file("Day16/input2.txt")
        instructions = []
        for line in program:
            instructions.append(list(map(int, line.split())))

        registers = [0, 0, 0, 0]
        for instruction in instructions:
            opcode, a, b, c = instruction
            registers = known_opcodes[opcode](registers, a, b, c)

        print("The final registers are: {0}".format(str(registers)))
        return registers
    else:
        # Iterate through each sample and determine how many opcodes end with expected output. If three or more
        # opcodes match, then increment the samples found.
        samples_found = 0
        for sample in samples:
            opcodes_matched = 0
            for opcode in all_opcodes:
                if exec(opcode, sample):
                    opcodes_matched += 1

            if opcodes_matched >= 3:
                samples_found += 1

        return samples_found


def part1(values):
    return check_operations(values)


def part2(values):
    return check_operations(values, True)
