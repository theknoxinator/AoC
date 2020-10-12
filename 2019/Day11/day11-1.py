# Run a program using intcode


class IntCodeRunner:

    def __init__(self, program):
        self.orig_program = program
        self.reset()
        self.inputs = []
        self.outputs = []

    def _parse_instruction(self, instruction):
        instruction_str = str(instruction)
        opcode = int(instruction_str[-2:])
        flags = []
        for x in range(3, 6):
            flags.append(0 if len(instruction_str) < x else int(instruction_str[-x]))
        return opcode, flags

    def _get_pos(self, offset, flag=0):
        if flag == 0:
            return self.program[self.position + offset]
        elif flag == 1:
            return self.position + offset
        elif flag == 2:
            return self.relative_base + self.program[self.position + offset]

    def _get_param(self, offset, flag=1):
        param_pos = self._get_pos(offset, flag)
        self._check_memory(param_pos)
        return self.program[param_pos]

    def _check_memory(self, position):
        if position >= len(self.program):
            self.program = self.program.copy() + [0 for _ in range(position - len(self.program) + 1)]

    def _add(self, flags):
        self.program[self._get_pos(3, flags[2])] = self._get_param(1, flags[0]) + self._get_param(2, flags[1])
        return self.position + 4

    def _multiply(self, flags):
        self.program[self._get_pos(3, flags[2])] = self._get_param(1, flags[0]) * self._get_param(2, flags[1])
        return self.position + 4

    def _input(self, flags):
        self.program[self._get_pos(1, flags[0])] = self.inputs.pop(0)
        return self.position + 2

    def _output(self, flags):
        self.outputs.append(self._get_param(1, flags[0]))
        return self.position + 2

    def _jump_true(self, flags):
        if self._get_param(1, flags[0]):
            return self._get_param(2, flags[1])
        else:
            return self.position + 3

    def _jump_false(self, flags):
        if not self._get_param(1, flags[0]):
            return self._get_param(2, flags[1])
        else:
            return self.position + 3

    def _less_than(self, flags):
        self.program[self._get_pos(3, flags[2])] = 1 if self._get_param(1, flags[0]) < self._get_param(2, flags[1]) else 0
        return self.position + 4

    def _equals(self, flags):
        self.program[self._get_pos(3, flags[2])] = 1 if self._get_param(1, flags[0]) == self._get_param(2, flags[1]) else 0
        return self.position + 4

    def _adjust_relative_base(self, flags):
        self.relative_base += self._get_param(1, flags[0])
        return self.position + 2

    def _end(self, flags):
        return len(self.program)

    def reset(self):
        self.position = 0
        self.relative_base = 0
        self.program = self.orig_program.copy()

    OPS = {
        1: _add,
        2: _multiply,
        3: _input,
        4: _output,
        5: _jump_true,
        6: _jump_false,
        7: _less_than,
        8: _equals,
        9: _adjust_relative_base,
        99: _end,
    }

    def execute(self):
        while self.position < len(self.program):
            opcode, flags = self._parse_instruction(self.program[self.position])
            operation = self.OPS.get(opcode, None)
            if opcode is None:
                print("Found unexpected intcode: {0!s} at {1!s}".format(self.program[self.position], self.position))
            else:
                try:
                    self.position = operation(self, flags)
                except IndexError:
                    return False
        return True


def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            return [int(x) for x in line.split(',')]


def test_data():
    # return [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    # return [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
    return [104, 1125899906842624, 99]


print("Starting Day11")
values = read_file('input.txt')
# values = test_data()

comp = IntCodeRunner(values)

# For this program, we have a grid that we need to track as well, and feed inputs into the computer
x, y = 0, 0
grid = {}
orientation = 'U'
finished = False
while not finished:
    if (x,y) not in grid:
        grid[(x,y)] = 0
    comp.inputs.append(grid[(x,y)])
    finished = comp.execute()
    print("Output: {0}".format(','.join(map(str, comp.outputs))))
    if finished or not comp.outputs:
        break
    color = comp.outputs.pop(0)
    direction = comp.outputs.pop(0)
    grid[(x,y)] = color
    if orientation == 'U':
        orientation = 'R' if direction else 'L'
    elif orientation == 'L':
        orientation = 'U' if direction else 'D'
    elif orientation == 'D':
        orientation = 'L' if direction else 'R'
    elif orientation == 'R':
        orientation = 'D' if direction else 'U'

    if orientation == 'U':
        y += 1
    elif orientation == 'L':
        x -= 1
    elif orientation == 'D':
        y -= 1
    elif orientation == 'R':
        x += 1

print("Number of grid spaces covered: {0!s}".format(len(grid)))
