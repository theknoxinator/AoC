# Run some assembly language

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6"]


print("Starting Day8-1")
values = read_file("input.txt")
# values = test_data()

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
                return
            line = code[self.pointer]
            opcode, var = self.parse(line)
            operation = self._opcodes.get(opcode, None)
            if operation is None:
                print("Found unexpected opcode: {0!s} at {1!s}".format(line, self.pointer))
            else:
                self.profiler[self.pointer] = self.profiler.get(self.pointer, 0) + 1
                self.pointer = operation(self, var)

    def parse(self, line):
        opcode, raw_var = line.split(' ')
        return opcode, int(raw_var)

    def acc(self, var):
        self.accumulator += var
        return self.pointer + 1

    def jmp(self, var):
        return self.pointer + var

    def nop(self, var):
        return self.pointer + 1

    _opcodes = {
        'acc': acc,
        'jmp': jmp,
        'nop': nop
    }


# Now run the program we've been given and output what the profiler catches as the start of the infinite loop
program = Assembler()
program.run(values)
print("The program stopped at line: {0!s}".format(program.pointer))
print("The value of the accumulator where it stopped is: {0!s}".format(program.accumulator))

