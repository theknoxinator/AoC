# Determine the number spoken on turn 2020 based on a couple game rules

def find_number(values, end):
    # For this part it's a small enough number we can use an array, and we can keep the numbers as strings since their value
    # doesn't matter, only the distance between them does
    numbers = values[0].split(',')
    last_seen = dict()
    # Add all numbers except for last one as it will be used in the first turn of the loop
    for i, number in enumerate(numbers[:-1]):
        last_seen[number] = i

    turn = len(numbers)
    while turn <= end:
        last_number = numbers[turn - 1]
        if last_number in last_seen:
            new_number = (turn - 1) - last_seen[last_number]
            numbers.append(str(new_number))
        else:
            numbers.append('0')
        last_seen[last_number] = turn - 1   # The last time we saw this number was now the previous turn
        turn += 1

    return numbers[end - 1]


def part1(values):
    return find_number(values, 2020)


def part2(values):
    return find_number(values, 30000000)
