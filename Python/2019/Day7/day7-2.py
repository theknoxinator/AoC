# Run a program using intcode
from itertools import permutations


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
    # return [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0,
    #         0, 5]
    return [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54, -5, 54, 1105, 1, 12,
            1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0,
            0, 0, 0, 10]


print("Starting Day7-2")
values = read_file('input.txt')
# values = test_data()

setting_permutations = permutations([5, 6, 7, 8, 9], 5)

highest_output = 0
for settings in setting_permutations:
    amp_A = IntCodeRunner(values)
    amp_B = IntCodeRunner(values)
    amp_C = IntCodeRunner(values)
    amp_D = IntCodeRunner(values)
    amp_E = IntCodeRunner(values)

    amp_A.inputs = amp_E.outputs
    amp_B.inputs = amp_A.outputs
    amp_C.inputs = amp_B.outputs
    amp_D.inputs = amp_C.outputs
    amp_E.inputs = amp_D.outputs

    amp_A.inputs.append(settings[0])
    amp_A.inputs.append(0)
    amp_B.inputs.append(settings[1])
    amp_C.inputs.append(settings[2])
    amp_D.inputs.append(settings[3])
    amp_E.inputs.append(settings[4])

    finished = False
    while not finished:
        amp_A.execute()
        amp_B.execute()
        amp_C.execute()
        amp_D.execute()
        finished = amp_E.execute()

    if amp_E.outputs[0] > highest_output:
        highest_output = amp_E.outputs[0]

# print("Ending values: {0}".format(','.join(map(str, amp_A.program))))
# print("Output: {0}".format(','.join(map(str, highest_output))))
print("Output: {0!s}".format(highest_output))
