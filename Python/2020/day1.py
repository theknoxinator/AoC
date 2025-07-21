# Determine the numbers that make 2020 when added together

def find_sum_values(values, use_part2=False):
    values = list(map(int, values))
    # Let's brute force this by just doing a simple set of runners through the list
    for index in range(len(values)):
        for first_runner in range(index + 1, len(values)):
            if use_part2:
                for second_runner in range(first_runner + 1, len(values)):
                    if values[index] + values[first_runner] + values[second_runner] == 2020:
                        return values[index] * values[first_runner] * values[second_runner]
            else:
                if values[index] + values[first_runner] == 2020:
                    return values[index] * values[first_runner]
    return 0


def part1(values):
    return find_sum_values(values)


def part2(values):
    return find_sum_values(values, True)
