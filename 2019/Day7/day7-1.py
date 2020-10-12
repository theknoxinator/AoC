# Run a program using intcode
from itertools import permutations


class IntCodeRunner:

    def __init__(self, program):
        self.orig_program = program
        self.reset()

    def _parse_instruction(self, instruction):
        instruction_str = str(instruction)
        opcode = int(instruction_str[-2:])
        flags = []
        for x in range(3, 6):
            flags.append(0 if len(instruction_str) < x else int(instruction_str[-x]))
        return opcode, flags

    def _get_param(self, offset, flag=1):
        return self.program[self.position + offset] if flag else self.program[self.program[self.position + offset]]

    def _add(self, flags):
        self.program[self._get_param(3)] = self._get_param(1, flags[0]) + self._get_param(2, flags[1])
        return self.position + 4

    def _multiply(self, flags):
        self.program[self._get_param(3)] = self._get_param(1, flags[0]) * self._get_param(2, flags[1])
        return self.position + 4

    def _input(self, flags):
        self.program[self._get_param(1)] = self.inputs.pop(0)
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
        self.program[self._get_param(3)] = 1 if self._get_param(1, flags[0]) < self._get_param(2, flags[1]) else 0
        return self.position + 4

    def _equals(self, flags):
        self.program[self._get_param(3)] = 1 if self._get_param(1, flags[0]) == self._get_param(2, flags[1]) else 0
        return self.position + 4

    def _end(self, flags):
        return len(self.program)

    def set_inputs(self, inputs):
        self.inputs = inputs

    def reset(self):
        self.position = 0
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
        99: _end,
    }

    def execute(self):
        self.outputs = []
        while self.position < len(self.program):
            opcode, flags = self._parse_instruction(self.program[self.position])
            operation = self.OPS.get(opcode, None)
            if opcode is None:
                print("Found unexpected intcode: {0!s} at {1!s}".format(self.program[self.position], self.position))
            else:
                self.position = operation(self, flags)
        return self.outputs


def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            return [int(x) for x in line.split(',')]


def test_data():
    # return [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
    # return [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]
    return [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32,
            31, 31, 4, 31, 99, 0, 0, 0]


print("Starting Day7")
values = read_file('input.txt')
# values = test_data()

setting_permutations = permutations([0, 1, 2, 3, 4], 5)

highest_output = 0
for settings in setting_permutations:
    amp_A = IntCodeRunner(values)
    amp_A.set_inputs([settings[0], 0])
    outputs = amp_A.execute()
    amp_B = IntCodeRunner(values)
    amp_B.set_inputs([settings[1], outputs[0]])
    outputs = amp_B.execute()
    amp_C = IntCodeRunner(values)
    amp_C.set_inputs([settings[2], outputs[0]])
    outputs = amp_C.execute()
    amp_D = IntCodeRunner(values)
    amp_D.set_inputs([settings[3], outputs[0]])
    outputs = amp_D.execute()
    amp_E = IntCodeRunner(values)
    amp_E.set_inputs([settings[4], outputs[0]])
    outputs = amp_E.execute()
    if outputs[0] > highest_output:
        highest_output = outputs[0]

# print("Ending values: {0}".format(','.join(map(str, amp_A.program))))
# print("Output: {0}".format(','.join(map(str, highest_output))))
print("Output: {0!s}".format(highest_output))
