# Determine the sum of values in memory after applying various bitmasks to the memory addresses on entry
import re


def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["mask = 000000000000000000000000000000X1001X",
            "mem[42] = 100",
            "mask = 00000000000000000000000000000000X0XX",
            "mem[26] = 1"]


print("Starting Day14-2")
values = read_file("input.txt")
# values = test_data()


# For the second part, we are doing bitmask operations on the addresses as we put the value into memory. The memory is
# just going to be a dictionary.
def compute_masks(address, mask):
    addresses = ["{0:036b}".format(int(address))]
    for i in range(len(mask)):
        if mask[i] == 'X':
            new_addresses = []
            for old in addresses:
                # Create two new addresses with 0 and 1 at the index where X is
                new_addresses.append(old[:i] + '0' + old[i + 1:])
                new_addresses.append(old[:i] + '1' + old[i + 1:])
            addresses = new_addresses
        elif mask[i] == '1':
            new_addresses = []
            for old in addresses:
                # Enforce a 1 at the index for all existing addresses
                new_addresses.append(old[:i] + '1' + old[i + 1:])
            addresses = new_addresses
    return addresses


memory = dict()
mask = ""
for val in values:
    if "mask" in val:
        # This time around we just grab the mask as we will process the masks on the memory addresses directly
        mask = val[7:]
    else:
        # We grab the address to process into a list of addresses based on the mask, and save the value to all
        address, value = re.findall("[0-9]+", val)
        addresses = compute_masks(address, mask)
        for addr in addresses:
            memory[int(addr, 2)] = int(value)

print(memory)
print("The sum of the values in memory is: {0!s}".format(sum(memory.values())))
