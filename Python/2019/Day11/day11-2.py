# Run a program using intcode


class IntCodeRunner:

    def __init__(self, program):
        self.orig_program = program
        self.reset()
        self.inputs = []
        self.outputs = []

    def parse_instruction(self, instruction):
        instruction_str = str(instruction)
        opcode = int(instruction_str[-2:])
        flags = []
        for x in range(3, 6):
            flags.append(0 if len(instruction_str) < x else int(instruction_str[-x]))
        return opcode, flags

    def get_pos(self, offset, flag):
        if flag == 0:
            return self.program[self.position + offset]
        elif flag == 1:
            return self.position + offset
        elif flag == 2:
            return self.relative_base + self.program[self.position + offset]

    def get_param(self, offset, flags):
        param_pos = self.get_pos(offset, flags[offset - 1])
        self.check_memory(param_pos)
        return self.program[param_pos]

    def set_param(self, offset, value, flags):
        param_pos = self.get_pos(offset, flags[offset - 1])
        self.check_memory(param_pos)
        self.program[param_pos] = value

    def check_memory(self, position):
        if position >= len(self.program):
            self.program = self.program.copy() + [0 for _ in range(position - len(self.program) + 1)]

    def add(self, flags):
        value = self.get_param(1, flags) + self.get_param(2, flags)
        self.set_param(3, value, flags)
        return self.position + 4

    def multiply(self, flags):
        value = self.get_param(1, flags) * self.get_param(2, flags)
        self.set_param(3, value, flags)
        return self.position + 4

    def input(self, flags):
        self.set_param(1, self.inputs.pop(0), flags)
        return self.position + 2

    def output(self, flags):
        self.outputs.append(self.get_param(1, flags))
        return self.position + 2

    def jump_true(self, flags):
        if self.get_param(1, flags):
            return self.get_param(2, flags)
        else:
            return self.position + 3

    def jump_false(self, flags):
        if not self.get_param(1, flags):
            return self.get_param(2, flags)
        else:
            return self.position + 3

    def less_than(self, flags):
        value = 1 if self.get_param(1, flags) < self.get_param(2, flags) else 0
        self.set_param(3, value, flags)
        return self.position + 4

    def equals(self, flags):
        value = 1 if self.get_param(1, flags) == self.get_param(2, flags) else 0
        self.set_param(3, value, flags)
        return self.position + 4

    def adjust_relative_base(self, flags):
        self.relative_base += self.get_param(1, flags)
        return self.position + 2

    def end(self, flags):
        return len(self.program)

    def reset(self):
        self.position = 0
        self.relative_base = 0
        self.program = self.orig_program.copy()

    OPS = {
        1: add,
        2: multiply,
        3: input,
        4: output,
        5: jump_true,
        6: jump_false,
        7: less_than,
        8: equals,
        9: adjust_relative_base,
        99: end,
    }

    def execute(self):
        while self.position < len(self.program):
            opcode, flags = self.parse_instruction(self.program[self.position])
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


print("Starting Day11-2")
values = read_file('input.txt')
# values = test_data()

comp = IntCodeRunner(values)

# For this program, we have a grid that we need to track as well, and feed inputs into the computer
x, y = 0, 0
min_x, min_y, max_x, max_y = x, y, x, y
grid = {}
grid[(x,y)] = 1
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

    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)

# Now we need to print out the result
sorted_grid = {k: v for k, v in sorted(grid.items())}
print(sorted_grid)

for row in range(max_y, min_y - 1, -1):
    for col in range(min_x, max_x + 1):
        if (col, row) in grid and grid[(col, row)] == 1:
            print('#', end='')
        else:
            print('.', end='')
    print()
