# Part 1: Run a program of instructions, similar to day 18 previously, determine how many times mul opcode is called
# Part 2: Run the same program with a different mode and determine the result of register 'h'

class Simulator:

    def __init__(self, code):
        self.code = code
        self.pointer = 0
        self.registers = {x: 0 for x in 'abcdefgh'}
        self.mul_count = 0

    def run(self):
        while 0 <= self.pointer < len(self.code):
            line = self.code[self.pointer]
            opcode, reg, var = self._parse(line)
            operation = self._opcodes.get(opcode, None)
            if operation is None:
                print(f'Found unexpected opcode: {line} at {self.pointer!s}')
                return False
            self.pointer = operation(self, reg, var)
        return True

    def _parse(self, line):
        params = line.split(' ')
        if len(params) < 3:
            return params[0], params[1], 0
        return params[0], params[1], params[2]

        # Helper function that determines if val is a register value or a hard value, and returns the correct value

    def _get_value(self, val):
        if val.isalpha():
            return self.registers[val] if val in self.registers else 0
        else:
            return int(val)

    # Sets a value to the selected register
    def _set(self, reg, val):
        self.registers[reg] = self._get_value(val)
        return self.pointer + 1

    # Subtracts a value from the selected register
    def _sub(self, reg, val):
        self.registers[reg] = self._get_value(reg) - self._get_value(val)
        return self.pointer + 1

    # Multiplies a value to the selected register
    def _mul(self, reg, val):
        self.registers[reg] = self._get_value(reg) * self._get_value(val)
        self.mul_count += 1
        return self.pointer + 1

    # Jumps the pointer to the specified offset, but only if value at selected register is not equal to zero
    def _jnz(self, reg, val):
        if self._get_value(reg) != 0:
            return self.pointer + self._get_value(val)
        else:
            return self.pointer + 1

    _opcodes = {
        'set': _set,
        'sub': _sub,
        'mul': _mul,
        'jnz': _jnz,
    }


def run_program(values):
    # Get the code from values and then run the program until it terminates
    code = values
    program = Simulator(code)
    program.run()

    # Return the number of times mul was executed
    return program.mul_count


def run_modified_program(_values):
    # After trying to modify the original assembly and not getting the efficiency I think is needed, I looked it up and
    # apparently everyone just rewrote it entirely in a high-level language, so just going to do that
    # Effectively the program is trying to figure out which numbers within a range are not prime, and returns the count
    # of those

    # In the original code, register 'a' is effectively the mode, not needed here
    # Register 'b' is the current value we are checking, starting at 108,100, aka the bottom of the range
    # Register 'c' is the last value to check, which is 125,100 since it's 'b' + 17,000, aka the top of the range
    b = 81 * 100 + 100_000
    c = b + 17_000

    # Registers 'd' and 'e' are used for the factors that are being multiplied and checked against 'b'
    # The inefficiency comes in with these since they both increment by 1 from 2 to the value of 'b', and there's no real
    # way to stop them early due to only having jnz as an instruction (jge or jump when greater or equal to zero would've
    # solved this issue entirely)
    # Register 'f' is just a flag to check if a pair of factors comes to the value of 'b', if this is yes (or 0 in the
    # assembly), then register 'h' would increment by 1, effectively our count of non-primes
    # Register 'g' is effectively the main variable used for doing all the math on

    # The main loop is to check all numbers between 'b' and 'c' (inclusive) at the start, and increment by 17 for 1001
    # total checks
    h = 0
    while b <= c:
        # Inside the loop, we are checking all valid factors to see if they match 'b'
        # Both 'd' and 'e' should only go up to half of 'b' at most since anything past that is completely useless
        f = 0
        for d in range(2, b // 2 + 1):
            for e in range(d, b // 2 + 1):
                if d * e == b:
                    f = 1
                    break
                elif d * e > b:
                    break
            if f == 1:
                h += 1
                break
        b += 17

    # Return the count of non-primes
    return h


def part1(values):
    return run_program(values)


def part2(values):
    return run_modified_program(values)
