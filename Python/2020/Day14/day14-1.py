# Determine the sum of values in memory after applying various bitmasks to the values on entry
import re


def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            "mem[8] = 11",
            "mem[7] = 101",
            "mem[8] = 0"]


print("Starting Day14-1")
values = read_file("input.txt")
# values = test_data()

# For the first part, we are doing simple bitmask operations on values to put into memory. The memory is just going to
# be a dictionary.
memory = dict()
and_mask = 1
or_mask = 0
for val in values:
    if "mask" in val:
        # We are updating the mask, so convert it into the appropriate and/or masks
        mask = val[7:]
        and_mask = int(mask.replace('X', '1'), 2)
        or_mask = int(mask.replace('X', '0'), 2)
    else:
        # We are saving a value into memory, so get the memory location and the value, apply the two masks, and save
        address, value = re.findall("[0-9]+", val)
        memory[int(address)] = int(value) & and_mask | or_mask

print(memory)
print("The sum of the values in memory is: {0!s}".format(sum(memory.values())))
