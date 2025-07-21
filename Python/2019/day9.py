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

    def _get_param(self, offset, flag=1):
        if flag == 0:
            return self.program[self.program[self.position + offset]]
        elif flag == 1:
            return self.program[self.position + offset]
        elif flag == 2:
            return self.program[self.relative_base + self.program[self.position + offset]]

    def _get_pos(self, offset, flag=0):
        if flag == 0:
            return self.program[self.position + offset]
        elif flag == 2:
            return self.relative_base + self.program[self.position + offset]

    def _check_memory(self, position):
        if position >= len(self.program):
            self.program = self.program.copy() + [0 for _ in range(position - len(self.program) + 1)]

    def _add(self, flags):
        self._check_memory(self._get_pos(3, flags[2]))
        self.program[self._get_pos(3, flags[2])] = self._get_param(1, flags[0]) + self._get_param(2, flags[1])
        return self.position + 4

    def _multiply(self, flags):
        self._check_memory(self._get_pos(3, flags[2]))
        self.program[self._get_pos(3, flags[2])] = self._get_param(1, flags[0]) * self._get_param(2, flags[1])
        return self.position + 4

    def _input(self, flags):
        self._check_memory(self._get_pos(1, flags[0]))
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
        self._check_memory(self._get_pos(3, flags[2]))
        self.program[self._get_pos(3, flags[2])] = 1 if self._get_param(1, flags[0]) < self._get_param(2, flags[1]) else 0
        return self.position + 4

    def _equals(self, flags):
        self._check_memory(self._get_pos(3, flags[2]))
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


def run_program(values, start_input):
    instructions = list(map(int, values[0].split(',')))
    comp = IntCodeRunner(instructions)
    comp.inputs.append(start_input)
    comp.execute()

    return ''.join(map(str, comp.outputs))


def part1(values):
    return run_program(values, 1)


def part2(values):
    return run_program(values, 2)
