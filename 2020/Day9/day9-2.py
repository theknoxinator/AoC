# Determine the set of contiguous numbers in the list that sum up to the bad number from part 1
import itertools

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["35",
            "20",
            "15",
            "25",
            "47",
            "40",
            "62",
            "55",
            "65",
            "95",
            "102",
            "117",
            "150",
            "182",
            "127",
            "219",
            "299",
            "277",
            "309",
            "576"]


print("Starting Day9-2")
values = read_file("input.txt")
# values = test_data()


# For this problem we have a moving window of numbers to sum in that we start in a place and expand until we reach or
# exceed the sum, then start again at the next place. This is not the most efficient way to do this, but I can't be
# bothered.
bad_number = 14360655
def find_bad_range(numbers):
    for start in range(len(numbers)):
        for end in range(start + 1, len(numbers)):
            ranged_sum = sum(numbers[start:end])
            if ranged_sum == bad_number:
                return numbers[start:end]
            elif ranged_sum > bad_number:
                break

numbers = [int(x) for x in values]
bad_numbers = find_bad_range(numbers)
print(bad_numbers)
print("The min and max of the bad numbers are: {0!s}, {1!s}".format(min(bad_numbers), max(bad_numbers)))
print("The encryption weakness is: {0!s}".format(min(bad_numbers) + max(bad_numbers)))
