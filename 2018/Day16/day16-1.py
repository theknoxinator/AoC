# Determine which sample operations match at least three different opcodes of an available 16

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values

def test_data():
    return ["Before: [3, 2, 1, 1]",
            "9 2 1 2",
            "After:  [3, 2, 2, 1]"]

if __name__ == '__main__':
    print("Starting Day 16-1")
    # Read file into list of values
    values = read_file('input.txt')
    # values = test_data()

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

    # Iterate through each sample and determine how many opcodes end with expected output. If three or more
    # opcodes match, then increment the samples found.
    samples_found = 0
    for sample in samples:
        opcodes_matched = 0
        for opcode in all_opcodes:
            if exec(opcode, sample):
                print("Opcode {0} matches with sample: {1!s}".format(opcode.__name__, sample))
                opcodes_matched += 1

        if opcodes_matched >= 3:
            samples_found += 1

    # Print out answer
    print("Total number of samples with three or more matching opcodes is: {0!s}".format(samples_found))
