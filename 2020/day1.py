# Determine the numbers that make 2020 when added together
def part1(values):
    # Let's brute force this by just doing a simple double runner through the list (n^2)
    answer = 0
    for index in range(len(values)):
        for runner in range(index + 1, len(values)):
            if int(values[index]) + int(values[runner]) == 2020:
                answer = int(values[index]) * int(values[runner])
                break
        if answer:
            break
    return answer


def part2(values):
    # Let's brute force this by just doing a simple double runner through the list (n^3)
    answer = 0
    for index in range(len(values)):
        for first_runner in range(index + 1, len(values)):
            for second_runner in range(first_runner + 1, len(values)):
                if int(values[index]) + int(values[first_runner]) + int(values[second_runner]) == 2020:
                    answer = int(values[index]) * int(values[first_runner]) * int(values[second_runner])
                    break
            if answer:
                break
        if answer:
            break
    return answer
