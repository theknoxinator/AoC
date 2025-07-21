# Determine the sum of values in memory after applying various bitmasks to the values on entry
import re

def apply_bitmasks(values):
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

    return sum(memory.values())


def compute_masks(values):
    # For the second part, we are doing bitmask operations on the addresses as we put the value into memory. The memory is
    # just going to be a dictionary.
    def compute_addresses(address, mask):
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
            addresses = compute_addresses(address, mask)
            for addr in addresses:
                memory[int(addr, 2)] = int(value)

    return sum(memory.values())


def part1(values):
    return apply_bitmasks(values)


def part2(values):
    return compute_masks(values)
