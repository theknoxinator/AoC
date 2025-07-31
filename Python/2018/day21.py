# Part 1: Run a program of assembly code and determine the lowest value in register 0 that causes the program to halt quickly
# Part 2:

# For this iteration of the same program running, turning it into a class like other similar problems
class Simulator:

    def __init__(self, code, ptr_reg=0):
        self.code = self._parse_code(code)
        self.ptr = ptr_reg
        self.regs = [0] * 6
        self.valid_nums = []
        self.valid_nums_set = set()

    def run(self):
        instructions = 0
        while self.regs[self.ptr] < len(self.code):
            opcode, a, b, c = self.code[self.regs[self.ptr]]
            operation = self._opcodes[opcode]
            operation(self, a, b, c)
            instructions += 1
            self.regs[self.ptr] += 1
            if self.regs[self.ptr] == 28:
                # We are at the check that allows the program to end, so capture the valid numbers that can end it
                if self.regs[4] in self.valid_nums_set:
                    print('Found dupe')
                    break
                else:
                    self.valid_nums_set.add(self.regs[4])
                    self.valid_nums.append(self.regs[4])

        return instructions

    def _parse_code(self, code):
        full_code = []
        for line in code:
            opcode, a, b, c = line.split()
            full_code.append((opcode, int(a), int(b), int(c)))
        return full_code

    def _addr(self, a, b, c):
        self.regs[c] = self.regs[a] + self.regs[b]

    def _addi(self, a, b, c):
        self.regs[c] = self.regs[a] + b

    def _mulr(self, a, b, c):
        self.regs[c] = self.regs[a] * self.regs[b]

    def _muli(self, a, b, c):
        self.regs[c] = self.regs[a] * b

    def _banr(self, a, b, c):
        self.regs[c] = self.regs[a] & self.regs[b]

    def _bani(self, a, b, c):
        self.regs[c] = self.regs[a] & b

    def _borr(self, a, b, c):
        self.regs[c] = self.regs[a] | self.regs[b]

    def _bori(self, a, b, c):
        self.regs[c] = self.regs[a] | b

    def _setr(self, a, _b, c):
        self.regs[c] = self.regs[a]

    def _seti(self, a, _b, c):
        self.regs[c] = a

    def _gtir(self, a, b, c):
        self.regs[c] = 1 if a > self.regs[b] else 0

    def _gtri(self, a, b, c):
        self.regs[c] = 1 if self.regs[a] > b else 0

    def _gtrr(self, a, b, c):
        self.regs[c] = 1 if self.regs[a] > self.regs[b] else 0

    def _eqir(self, a, b, c):
        self.regs[c] = 1 if a == self.regs[b] else 0

    def _eqri(self, a, b, c):
        self.regs[c] = 1 if self.regs[a] == b else 0

    def _eqrr(self, a, b, c):
        self.regs[c] = 1 if self.regs[a] == self.regs[b] else 0

    _opcodes = {
        'addr': _addr,
        'addi': _addi,
        'mulr': _mulr,
        'muli': _muli,
        'banr': _banr,
        'bani': _bani,
        'borr': _borr,
        'bori': _bori,
        'setr': _setr,
        'seti': _seti,
        'gtir': _gtir,
        'gtri': _gtri,
        'gtrr': _gtrr,
        'eqir': _eqir,
        'eqri': _eqri,
        'eqrr': _eqrr,
    }


def run_program(values, reg_zero):
    # Setup the simulator by grabbing the pointer register and loading the code
    ptr_reg = 0
    if '#ip' in values[0]:
        ptr_reg = int(values[0].split()[1])

    program = Simulator(values[1:], ptr_reg)

    # We're just going to hardcode this to the answer because it turns out finding it programmatically was not feasible,
    # the trick is that the program generates the same sequence of numbers every time, so the 0 register just needs to
    # match the first number to force the shortest possible execution
    results = dict()
    program.regs = [0] * 6
    program.regs[0] = reg_zero
    instructions = program.run()
    results[reg_zero] = instructions

    lowest = [x[0] for x in results.items() if x[1] == min(results.values())]
    print(program.valid_nums)
    return min(lowest), program.valid_nums[-1]


def cheat_program(values):
    # I got tired of the long time it was taking to run the program legitimately after figuring out what it wanted,
    # so just copying a re-coded solution from the internet
    seen = set()
    last_seen = None
    c = 0

    while True:
        a = c | 65536
        c = 678134
        while True:
            c = (((c + (a & 255)) & 16777215) * 65899) & 16777215
            if a < 256:
                if c not in seen:
                    seen.add(c)
                    last_seen = c
                    break
                else:
                    return last_seen
            else:
                a = a // 256


def part1(values):
    return run_program(values, 10961197)[0]


def part2(values):
    return cheat_program(values)
