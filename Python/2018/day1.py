# Change frequency based on inputs from file
# Positive frequency change adds to current value, negative change subtracts

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            if line[0] == '+':
                values.append(int(line[1:]))
            elif line[0] == '-':
                values.append(int(line[1:]) * -1)

    return values

def sum_freqs(values, use_part2=False):
    freqs = []
    # Iterate and convert values to frequency
    for val in values:
        if val[0] == '+':
            freqs.append(int(val[1:]))
        elif val[0] == '-':
            freqs.append(int(val[1:]) * -1)

    if not use_part2:
        # Sum the frequencies
        return sum(freqs)
    else:
        # Iterate and apply values to frequency
        past_frequencies = [0]
        current = 0
        found_past = False
        loops = 0
        while not found_past:
            for freq in freqs:
                loops += 1
                current += freq
                if current not in past_frequencies:
                    past_frequencies.append(current)
                else:
                    found_past = True
                    break
        return current


def part1(values):
    return sum_freqs(values)


def part2(values):
    return sum_freqs(values, True)
