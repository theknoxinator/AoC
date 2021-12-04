# Determine the number of times bit values appear in a binary number
def part1(values):
    # We iterate through the list of binary numbers and count the 1's in each position
    total_values = len(values)
    ones_counter = [0 for _ in range(len(values[0]))]
    for binary in values:
        for index, digit in enumerate(binary):
            if digit == '1':
                ones_counter[index] += 1
    zeros_counter = [total_values - x for x in ones_counter]
    print(f'Zeroes: {zeros_counter}')
    print(f'Ones: {ones_counter}')

    gamma = ''
    epsilon = ''
    for index in range(len(ones_counter)):
        if ones_counter[index] > zeros_counter[index]:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    print(f'Gamma: {gamma} ({int(gamma, 2)})')
    print(f'Epsilon: {epsilon} ({int(epsilon, 2)})')

    return int(gamma, 2) * int(epsilon, 2)

def part2(values):
    # We go through the process of iterating and paring down twice to determine the most/least common
    def process_list(remaining, index, most_common):
        if len(remaining) == 1:
            return remaining[0]
        zeros_list = []
        ones_list = []
        for binary in remaining:
            if binary[index] == '0':
                zeros_list.append(binary)
            else:
                ones_list.append(binary)
        if most_common:
            if len(ones_list) >= len(zeros_list):
                return process_list(ones_list, index + 1, most_common)
            else:
                return process_list(zeros_list, index + 1, most_common)
        else:
            if len(zeros_list) <= len(ones_list):
                return process_list(zeros_list, index + 1, most_common)
            else:
                return process_list(ones_list, index + 1, most_common)

    oxygen = process_list(values, 0, True)
    carbondioxide = process_list(values, 0, False)
    print(f'Oxygen: {oxygen} ({int(oxygen, 2)})')
    print(f'CO2: {carbondioxide} ({int(carbondioxide, 2)})')

    return int(oxygen, 2) * int(carbondioxide, 2)
