# Determine the number of unique molecules generated after doing single replacements of one element

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["H => HO",
            "H => OH",
            "O => HH",
            "HOH"]

if __name__ == '__main__':
    print("Starting Day19-1")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # First compile first part of values into the replacement table and grab last value as the molecule
    replacements = {}
    molecule = ""
    for val in values:
        if "=>" in val:
            items = val.split()
            if items[0] not in replacements:
                replacements[items[0]] = [items[2]]
            else:
                replacements[items[0]].append(items[2])
        else:
            molecule = val.strip()

    # Debug print the replacements and molecule
    print("Molecule: {0}".format(molecule))
    for element,values in replacements.items():
        print("Element {0} becomes: [{1}]".format(element, ','.join(values)))
    print()

    # Iterate through each element and replace it, putting the new molecule in a list
    new_molecules = []
    for index in range(len(molecule)):
        end_index = index + 1
        element = molecule[index]
        if element not in replacements:
            end_index = index + 2
            element = molecule[index:index+2]
        if element not in replacements:
            continue

        to_replace = replacements[element]
        for new_element in to_replace:
            new_molecules.append(molecule[:index] + new_element + molecule[end_index:])

    # Debug print the new molecules
    #for new_molecule in new_molecules:
    #    print(new_molecule)
    print("The number of new molecules is: {0}".format(str(len(new_molecules))))

    # Print out answer
    new_molecule_set = set(new_molecules)
    print("The number of new unique molecules is: {0}".format(str(len(new_molecule_set))))
