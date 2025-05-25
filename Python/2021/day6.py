# Determine the number of fish at the end of a bunch of breeding cycles
def breed_fish(values, days):
    # First we parse the list of fish into buckets for how many days each has until next breeding
    fishes = [0] * 9
    for fish in values[0].split(','):
        fishes[int(fish)] += 1
    print(f'{fishes!s}')

    # Now we iterate through days and perform the breeding algo
    for _ in range(days):
        breeding = fishes[0]
        for index in range(len(fishes) - 1):
            fishes[index] = fishes[index + 1]
        fishes[6] += breeding
        fishes[8] = breeding

    print(f'{fishes!s}')
    return sum(fishes)


def part1(values):
    return breed_fish(values, 80)


def part2(values):
    # Exactly the same as part1 just with a larger number
    return breed_fish(values, 256)
