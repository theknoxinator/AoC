# Find the best balance of packages such that they are three equally weighted groups, with the smallest
# group also having the smallest product of weights
from collections import deque

def balance_packages(values, groups=3):
    # First determine how much each group should weigh (sum / number of groups)
    values = sorted(map(int, values), reverse=True)
    total_sum = sum(values)
    group_sum = int(total_sum / groups)

    # We are just going to calculate each combination with the smallest amount of containers
    group_combos = []
    smallest_combo = len(values)
    queue = deque()
    for index in range(len(values)):
        queue.append(([values[index]], index + 1))
    while len(queue) > 0:
        partial_combo,start_index = queue.popleft()
        for index in range(start_index, len(values)):
            new_combo = partial_combo.copy()
            new_combo.append(values[index])
            current_sum = sum(new_combo)
            if current_sum > group_sum or len(new_combo) > smallest_combo:
                continue
            elif current_sum == group_sum:
                if len(new_combo) < smallest_combo:
                    group_combos = [new_combo]
                    smallest_combo = len(new_combo)
                elif len(new_combo) == smallest_combo:
                    group_combos.append(new_combo)
                else:
                    continue
            else:
                # Sum is less than expected, so add new combo to queue for further adding
                queue.append((new_combo, index + 1))

    # Now sort the valid combos by length, and get the QE for the smallest ones
    all_QEs = {}
    for index in range(len(group_combos)):
        combo = group_combos[index]
        QE = 1
        for num in combo:
            QE *= num
        all_QEs[QE] = combo

    return min(all_QEs.keys())


def part1(values):
    return balance_packages(values)


def part2(values):
    return balance_packages(values, 4)
