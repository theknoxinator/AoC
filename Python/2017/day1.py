# Add sums of repeating digits based on inputs from file
# Digits are only added to the total sum if the following digit is the same

def find_sum(values):
    digits = values[0]

    # Iterate and add repeated digits to sum
    sum = 0
    for index in range(len(digits)):
        if index == len(digits) - 1:
            # Last digit, check first digit
            if digits[index] == digits[0]:
                sum += int(digits[index])
        elif digits[index] == digits[index+1]:
            sum += int(digits[index])

    return sum


def find_sum2(values):
    digits = values[0]

    # Digits only count if they repeat halfway through the list
    # Iterate and add repeated digits to sum
    sum = 0
    half_length = len(digits) // 2
    for index in range(half_length):
        if digits[index] == digits[index + half_length]:
            sum += int(digits[index])
    sum *= 2

    return sum


def part1(values):
    return find_sum(values)


def part2(values):
    return find_sum2(values)
