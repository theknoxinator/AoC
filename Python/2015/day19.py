# Determine the number of unique molecules generated after doing single replacements of one element
import re
from collections import deque
from random import shuffle

def change_molecule(values):
    # First compile the first part of values into the replacement table and grab last value as the molecule
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

    return len(set(new_molecules))


def reduce_molecule(values):
    # First compile the first part of values into the replacement table and grab last value as the molecule
    replacements = []
    molecule = ""
    for val in values:
        if "=>" in val:
            items = val.split()
            replacements.append((items[0], items[2]))
        else:
            molecule = val.strip()

    target = molecule
    count = 0

    while target != 'e':
        start = target
        for element, replacement in replacements:
            if replacement not in target:
                continue

            target = target.replace(replacement, element, 1)
            count += 1

        if start == target:
            target = molecule
            count = 0
            shuffle(replacements)

    return count


def part1(values):
    return change_molecule(values)


def part2(values):
    return reduce_molecule(values)
