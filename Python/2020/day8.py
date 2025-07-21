# Run some assembly language

# Doing one of these again, we'll create a class that does the actions and stores the variables since it will be
# used again later.
# In this iteration we have a profiler in place to keep track of how often each line is called since we need it to
# determine where the infinite loop starts.
class Assembler:

    def __init__(self):
        self.accumulator = 0
        self.pointer = 0
        self.profiler = dict()

    def run(self, code):
        while self.pointer < len(code):
            if self.pointer in self.profiler:
                # Here is the point where it repeats, so stop now
                return False
            line = code[self.pointer]
            opcode, var = self.parse(line)
            operation = self._opcodes.get(opcode, None)
            if operation is None:
                print("Found unexpected opcode: {0!s} at {1!s}".format(line, self.pointer))
            else:
                self.profiler[self.pointer] = self.profiler.get(self.pointer, 0) + 1
                self.pointer = operation(self, var)
        return True

    def parse(self, line):
        opcode, raw_var = line.split(' ')
        return opcode, int(raw_var)

    def acc(self, var):
        self.accumulator += var
        return self.pointer + 1

    def jmp(self, var):
        return self.pointer + var

    def nop(self, _var):
        return self.pointer + 1

    _opcodes = {
        'acc': acc,
        'jmp': jmp,
        'nop': nop
    }


def run_program(values):
    # Now run the program we've been given and output what the profiler catches as the start of the infinite loop
    program = Assembler()
    program.run(values)
    return program.accumulator


def modify_program(values):
    # This time we are going to modify the code line by line until it runs without creating an infinite loop
    for i in range(len(values)):
        if "acc" in values[i]:
            continue
        modified_code = values.copy()
        if "nop" in values[i]:
            modified_code[i] = values[i].replace("nop", "jmp")
        elif "jmp" in values[i]:
            modified_code[i] = values[i].replace("jmp", "nop")
        program = Assembler()
        success = program.run(modified_code)
        if success:
            return program.accumulator
    return 0


def part1(values):
    return run_program(values)


def part2(values):
    return modify_program(values)
