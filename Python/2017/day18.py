# Part 1: Run a program of instructions that plays sounds based on registers, determine most recent sound on recovery
# Part 2: Run two programs in parallel that send data to each other, determine how many times second program sent values
from collections import deque


class Simulator:

    def __init__(self, code, pid=0, mode=0):
        self.code = code
        self.mode = mode
        self.pointer = 0
        self.registers = dict()
        self.registers['p'] = pid
        self.last_sound = 0
        self.queue = deque()
        self.waiting = False
        self.other = None
        self.sent_count = 0

    def run(self):
        while 0 <= self.pointer < len(self.code) and not self.waiting:
            line = self.code[self.pointer]
            opcode, reg, var = self._parse(line)
            operation = self._opcodes.get(opcode, None)
            if operation is None:
                print(f'Found unexpected opcode: {line} at {self.pointer!s}')
                return False
            self.pointer = operation(self, reg, var)
        return True

    def enqueue(self, val):
        self.queue.append(str(val))
        self.waiting = False

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

    # For part 1, this plays a sound with the frequency at the selected register
    # For part 2 (mode=1), this is sending data to the other program
    def _snd(self, reg, _val):
        if self.mode == 0:
            self.last_sound = self._get_value(reg)
        else:
            self.other.enqueue(self._get_value(reg))
            self.sent_count += 1
        return self.pointer + 1

    # Sets a value to the selected register
    def _set(self, reg, val):
        self.registers[reg] = self._get_value(val)
        return self.pointer + 1

    # Adds a value to the selected register
    def _add(self, reg, val):
        self.registers[reg] = self._get_value(reg) + self._get_value(val)
        return self.pointer + 1

    # Multiplies a value to the selected register
    def _mul(self, reg, val):
        self.registers[reg] = self._get_value(reg) * self._get_value(val)
        return self.pointer + 1

    # Modulos a value to the selected register
    def _mod(self, reg, val):
        self.registers[reg] = self._get_value(reg) % self._get_value(val)
        return self.pointer + 1

    # For part 1, this marks a recovery and we want to quit the program as soon as we hit this with a non-zero value in
    # the register, so jump to -1
    # For part 2 (mode=1), this is receiving data from the other program, so get values from queue or wait if empty
    def _rcv(self, reg, _val):
        if self.mode == 0:
            if self._get_value(reg) != 0:
                return -1
            else:
                return self.pointer + 1
        else:
            if self.queue:
                val = self.queue.popleft()
                return self._set(reg, val)
            else:
                self.waiting = True
                return self.pointer

    # Jumps the pointer to the specified offset, but only if value at selected register is greater than zero
    def _jgz(self, reg, val):
        if self._get_value(reg) > 0:
            return self.pointer + self._get_value(val)
        else:
            return self.pointer + 1

    _opcodes = {
        'snd': _snd,
        'set': _set,
        'add': _add,
        'mul': _mul,
        'mod': _mod,
        'rcv': _rcv,
        'jgz': _jgz,
    }


def run_program(values):
    # Get the code from values and then run the program until it terminates
    code = values
    program = Simulator(code)
    program.run()

    # Return the last sound that was played after rcv was hit the first time
    return program.last_sound


def run_programs(values):
    # Get the code from values and then create parallel programs
    code = values
    program_0 = Simulator(code, pid=0, mode=1)
    program_1 = Simulator(code, pid=1, mode=1)
    program_0.other = program_1
    program_1.other = program_0

    # Now run each program in sequence, they will return when they get blocked or finished, so keep running until either
    # both finish or they deadlock
    while True:
        program_0.run()
        program_1.run()
        if program_0.waiting and not program_0.queue and program_1.waiting and not program_1.queue:
            # We have a deadlock where both queues are empty but programs are waiting
            break
        elif not program_0.waiting and not program_1.waiting:
            # Neither program is waiting so we assume they both finished properly
            break

    # Return the number of sent items from the second program
    return program_1.sent_count


def part1(values):
    return run_program(values)


def part2(values):
    return run_programs(values)
