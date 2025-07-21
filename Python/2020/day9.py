# Determine the first number in the list that does not equal of sum of any two of the previous X numbers
import itertools

def find_unique(values):
    # This problem is a lot like Day 1 where we were summing numbers in a list, so we will take a similar approach but
    # add in the moving window aspect
    def get_sums(numbers, start, end):
        return {sum(x) for x in itertools.combinations(numbers[start:end], 2)}

    numbers = list(map(int, values))
    preamble = 25
    if len(numbers) <= 20:
        preamble = 5
    for index in range(preamble, len(numbers)):
        sums = get_sums(numbers, index - preamble, index)
        if numbers[index] not in sums:
            return numbers[index]
    return 0


def find_bad_range(values, target):
    numbers = list(map(int, values))
    bad_numbers = None
    for start in range(len(numbers)):
        for end in range(start + 1, len(numbers)):
            ranged_sum = sum(numbers[start:end])
            if ranged_sum == target:
                bad_numbers = numbers[start:end]
                break
            elif ranged_sum > target:
                break
        if bad_numbers:
            break

    return min(bad_numbers) + max(bad_numbers)


def part1(values):
    return find_unique(values)


def part2(values):
    return find_bad_range(values, find_unique(values))
