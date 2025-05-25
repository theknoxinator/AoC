# Determine the smallest number of replacements to create the target molecule from a single element
from collections import deque

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["e => H",
            "e => O",
            "H => HO",
            "H => OH",
            "O => HH",
            "HOH"]

if __name__ == '__main__':
    print("Starting Day19-2")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # First compile first part of values into the replacement table and grab last value as the molecule
    replacements = {}
    max_element_len = 0
    molecule = ""
    for val in values:
        if "=>" in val:
            items = val.split()
            if len(items[2]) > max_element_len:
                max_element_len = len(items[2])
            replacements[items[2]] = items[0]
        else:
            molecule = val.strip()

    # Debug print the replacements and molecule
    print("Molecule: {0}".format(molecule))
    for element,values in replacements.items():
        print("Element {0} becomes: [{1}]".format(element, ','.join(values)))
    print()

    # Add the first element onto a queue that will be used for different states
    queue = deque()
    queue.append((molecule, 0))

    # While there are items on the queue, keep making replacements and put them back on the queue
    smallest_replacement = 999999
    all_partials = {}
    while len(queue) > 0:
        # Grab the next partial from the queue
        partial,count = queue.pop()

        # Check to see if the partial was found with fewer steps on a different route
        if partial in all_partials and all_partials[partial] < count:
            count = all_partials[partial]

        # Increment the count so that each new partial has it, if there are no partials, it just goes away
        count += 1

        # If the count is now higher than the smallest found count, this is a bad path so just move on
        if count > smallest_replacement:
            continue

        # Iterate through each character in the partial, looking for matches in the replacement table
        for index in range(len(partial)):
            for end_index in range(index + 1, index + max_element_len):
                # The length is the last valid end index, so just stop searching at this point
                if end_index > len(partial):
                    break

                # Check to see if the space from index to end index (exclusive) is in the table
                # If not, we just skip and try another substring
                element = partial[index:end_index]
                if element in replacements:
                    # Found replacement, create new partial with the replacement
                    replacement = replacements[element]
                    new_partial = partial[:index] + replacement + partial[end_index:]

                    # If new partial is the final step "e", then check to see if the final count is better
                    # and move on
                    if new_partial == "e":
                        print('Got to "e" with {0!s} steps'.format(count))
                        if count < smallest_replacement:
                            smallest_replacement = count
                        continue

                    # If new partial has already been found, just check to see if the count is better
                    # and throw it out
                    if new_partial in all_partials:
                        if count < all_partials[new_partial]:
                            all_partials[new_partial] = count
                        continue

                    # New partial has not been found already and isn't the end, so throw it on the queue
                    print("{0!s}: {1} -> {2}".format(count, partial, new_partial))
                    queue.append((new_partial, count))

    # Debug print out valid replacement molecules
    print("Smallest replacement count: {0!s}".format(smallest_replacement))
