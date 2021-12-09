# Determine the correct output of the randomized display patterns
def part1(values):
    # For part 1 the intent is to determine how many digits in the output displays are unique
    # First we split the digits from the output and just store the output for now
    outputs = []
    for display_parts in values:
        digits, output = display_parts.split(' | ')
        outputs.append(output)

    # Now we iterate through the outputs and determine how many digits are unique in each
    unique_digits = 0
    for output in outputs:
        digits = output.split()
        for digit in digits:
            if len(digit) in [2, 3, 4, 7]:
                unique_digits += 1

    return unique_digits


def decode_digits(digits):
    segment_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
    digit_mappings = dict()
    segment_mappings = dict()
    digit_4 = ''    # Special digit for determining segment mappings

    # Iterate through the list of digits once to get the unique digits and segment counts
    for digit in digits:
        for segment in digit:
            segment_count[segment] = segment_count[segment] + 1
        if len(digit) == 2:
            digit_mappings[digit] = 1
        elif len(digit) == 3:
            digit_mappings[digit] = 7
        elif len(digit) == 4:
            digit_mappings[digit] = 4
            digit_4 = digit
        elif len(digit) == 7:
            digit_mappings[digit] = 8

    # Now iterate through the segments to determine which segment is which
    for segment, count in segment_count.items():
        if count == 4:
            # Segment e
            segment_mappings[segment] = 'e'
        elif count == 6:
            # Segment b
            segment_mappings[segment] = 'b'
        elif count == 7:
            # Segments d and g
            if segment in digit_4:
                segment_mappings[segment] = 'd'
            else:
                segment_mappings[segment] = 'g'
        elif count == 8:
            # Segments a and c
            if segment in digit_4:
                segment_mappings[segment] = 'c'
            else:
                segment_mappings[segment] = 'a'
        elif count == 9:
            # Segment f
            segment_mappings[segment] = 'f'

    # Now iterate the digits again to find the remaining mappings
    for digit in digits:
        if digit in digit_mappings:
            continue
        mapped_digit = ''.join(sorted([segment_mappings[x] for x in digit]))
        if mapped_digit == 'abcefg':
            digit_mappings[digit] = 0
        elif mapped_digit == 'acdeg':
            digit_mappings[digit] = 2
        elif mapped_digit == 'acdfg':
            digit_mappings[digit] = 3
        elif mapped_digit == 'abdfg':
            digit_mappings[digit] = 5
        elif mapped_digit == 'abdefg':
            digit_mappings[digit] = 6
        elif mapped_digit == 'abcdfg':
            digit_mappings[digit] = 9

    return digit_mappings


def get_decoded_output(output, digits):
    return 1000 * digits[output[0]] + 100 * digits[output[1]] + 10 * digits[output[2]] + digits[output[3]]


def part2(values):
    # For part 2 we need to decode all of the digits, so we use the digits to determine the pattern and apply to
    # the outputs to get the results
    decoded_outputs = []
    for display_parts in values:
        digits, output = display_parts.split(' | ')
        cleaned_digits = [''.join(sorted(x)) for x in digits.split()]
        decoded_digits = decode_digits(cleaned_digits)
        cleaned_output = [''.join(sorted(x)) for x in output.split()]
        decoded_outputs.append(get_decoded_output(cleaned_output, decoded_digits))

    print(f'{decoded_outputs!s}')
    return sum(decoded_outputs)
