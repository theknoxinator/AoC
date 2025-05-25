# Determine the number spoken on turn 30000000 based on a couple game rules
import time

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    # return ["0,3,6"]
    # return ["1,3,2"]
    # return ["2,1,3"]
    # return ["1,2,3"]
    # return ["2,3,1"]
    # return ["3,2,1"]
    return ["3,1,2"]


print("Starting Day15-2")
values = read_file("input.txt")
# values = test_data()

# For this part it's a small enough number we can use an array, and we can keep the numbers as strings since their value
# doesn't matter, only the distance between them does
numbers = values[0].split(',')
last_seen = dict()
# Add all numbers except for last one as it will be used in the first turn of the loop
for i, number in enumerate(numbers[:-1]):
    last_seen[number] = i

turn = len(numbers)
start = time.perf_counter()
while turn <= 30000000:
    last_number = numbers[turn - 1]
    if last_number in last_seen:
        new_number = (turn - 1) - last_seen[last_number]
        numbers.append(str(new_number))
    else:
        numbers.append('0')
    last_seen[last_number] = turn - 1   # The last time we saw this number was now the previous turn
    turn += 1

end = time.perf_counter()
print("The 30000000th number is: {0!s}".format(numbers[29999999]))
print("Time taken: {0!s}".format(end-start))
