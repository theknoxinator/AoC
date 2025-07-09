# Calculate the checksum of inputs from file
# Checksum is calculated by taking biggest difference between numbers in each line and summing the differences
import sys

def calc_checksum(values):
    # Iterate and calculate largest difference in each line
    checksum = 0
    for val in values:
        min = sys.maxsize
        max = 0
        for num in list(map(int, val.split())):
            if num < min:
                min = num
            if num > max:
                max = num

        checksum += max - min

    return checksum


def calc_checksum2(values):
    # Iterate and find which values divide into an int
    checksum = 0
    for val in values:
        numbers = list(map(int, val.split()))

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                result = numbers[i] / numbers[j]
                if result.is_integer():
                    checksum += int(result)
                result = numbers[j] / numbers[i]
                if result.is_integer():
                    checksum += int(result)

    return checksum


def part1(values):
    return calc_checksum(values)


def part2(values):
    return calc_checksum2(values)
