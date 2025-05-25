# Find the best balance of packages such that they are three equally weighted groups, with the smallest
# group also having the smallest product of weights
from collections import deque

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(int(line))

    return values

def test_data():
    return [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

if __name__ == '__main__':
    print("Starting Day24-1")
    # Read file into list of values
    values = sorted(read_file('input.txt'), reverse=True)
    #values = sorted(test_data(), reverse=True)

    # First determine how much each group should weigh (sum / 3)
    total_sum = sum(values)
    group_sum = int(total_sum / 4)

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

    # Debug print out all combinations
    for combo in group_combos:
        print("[{0}]".format(','.join(map(str, combo))))
    print("Total number of combos: {0!s}".format(len(group_combos)))

    # Now sort the valid combos by length, and get the QE for the smallest ones
    all_QEs = {}
    for index in range(len(group_combos)):
        combo = group_combos[index]
        QE = 1
        for num in combo:
            QE *= num
        all_QEs[QE] = combo

    # Print out answer
    for QE in sorted(all_QEs.keys()):
        print("QE value for [{0}] is: {1!s}".format(','.join(map(str, all_QEs[QE])), QE))
