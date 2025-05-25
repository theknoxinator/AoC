# Determine the number of times the depth increases
def part1(values):
    # This is just a simple compare with the previous depth and incrementing a counter
    answer = 0
    for index in range(len(values) - 1):
        if int(values[index + 1]) > int(values[index]):
            answer += 1
    return answer


def part2(values):
    # This is the same as the previous problem, but we add three numbers before comparing
    answer = 0
    for index in range(len(values) - 3):
        first_window = int(values[index]) + int(values[index + 1]) + int(values[index + 2])
        second_window = int(values[index + 1]) + int(values[index + 2]) + int(values[index + 3])
        if second_window > first_window:
            answer += 1
    return answer
