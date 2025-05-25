# Create an algorithm for generating look-and-say sequences of digits
# For each set of consecutive digits in an existing sequence, the new sequence will have the number
# in the set followed by the digit

def run_sequence(start, iterations):
    current = start
    for _ in range(iterations):
        new_sequence = ""

        digit = current[0]
        index = 1
        count = 1
        while index < len(current):
            if digit != current[index]:
                new_sequence += str(count) + digit
                count = 1
                digit = current[index]
            else:
                count += 1
            index += 1
        new_sequence += str(count) + digit

        current = new_sequence

    return current


def part1(values):
    sequence = run_sequence(values[0], 40)
    return len(sequence)


def part2(values):
    sequence = run_sequence(values[0], 50)
    return len(sequence)
