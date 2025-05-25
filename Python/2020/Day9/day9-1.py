# Determine the first number in the list that does not equal of sum of any two of the previous X numbers
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


print("Starting Day9-1")
values = read_file("input.txt")
# values = test_data()


# This problem is a lot like Day 1 where we were summing numbers in a list, so we will take a similar approach but
# add in the moving window aspect
def get_sums(numbers, start, end):
    return {sum(x) for x in itertools.combinations(numbers[start:end], 2)}


numbers = [int(x) for x in values]
preamble = 25
for index in range(preamble, len(numbers)):
    sums = get_sums(numbers, index - preamble, index)
    if numbers[index] not in sums:
        print("Could not find sum for number: {0!s}".format(numbers[index]))
        break
