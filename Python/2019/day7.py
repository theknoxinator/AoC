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


def run_program(values):
    instructions = list(map(int, values[0].split(',')))
    setting_permutations = permutations([0, 1, 2, 3, 4], 5)

    highest_output = 0
    for settings in setting_permutations:
        amp_A = IntCodeRunner(instructions)
        amp_A.set_inputs([settings[0], 0])
        amp_A.execute()
        amp_B = IntCodeRunner(instructions)
        amp_B.set_inputs([settings[1], amp_A.outputs[0]])
        amp_B.execute()
        amp_C = IntCodeRunner(instructions)
        amp_C.set_inputs([settings[2], amp_B.outputs[0]])
        amp_C.execute()
        amp_D = IntCodeRunner(instructions)
        amp_D.set_inputs([settings[3], amp_C.outputs[0]])
        amp_D.execute()
        amp_E = IntCodeRunner(instructions)
        amp_E.set_inputs([settings[4], amp_D.outputs[0]])
        amp_E.execute()
        if amp_E.outputs[0] > highest_output:
            highest_output = amp_E.outputs[0]

    return highest_output


def run_looping_program(values):
    instructions = list(map(int, values[0].split(',')))
    setting_permutations = permutations([5, 6, 7, 8, 9], 5)

    highest_output = 0
    for settings in setting_permutations:
        amp_A = IntCodeRunner(instructions)
        amp_B = IntCodeRunner(instructions)
        amp_C = IntCodeRunner(instructions)
        amp_D = IntCodeRunner(instructions)
        amp_E = IntCodeRunner(instructions)

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

    return highest_output


def part1(values):
    return run_program(values)


def part2(values):
    return run_looping_program(values)
