# Determine how many bags contain at least one shiny gold bag
from collections import deque
import re


# To solve this we are going to create a parent-child tree with all possible bags, so we need a node class to store the
# parents and children. Children is a map of name to number because it will obviously be needed for part 2.
class Node:
    def __init__(self, color):
        self.color = color
        self.parents = []
        self.children = {}


def parse_bags(values):
    all_bags = dict()
    # Iterate through each line and parse out the various pieces
    for val in values:
        # First is to use regex to grab each part that defines the bags
        matches = re.finditer("([0-9]*\s?\w+\s\w+)\sbag[s]?", val)
        bags = [x.group(1) for x in matches]

        # Next, we take the current bag which is first in the list and create a node if it doesn't exist already
        if bags[0] not in all_bags:
            all_bags[bags[0]] = Node(bags[0])
        # Now we add the children to the current bag. If the child doesn't exist, we create a node as well. In either case
        # we will add the current node as a parent to the child node as well.
        for i in range(1, len(bags)):
            child = bags[i]
            # Do nothing if the child is just "no other"
            if "no other" in child:
                break
            # Split the number and color into two parts with regex
            number = re.match("[0-9]+", child).group(0)
            color = re.search("[a-z]+\s[a-z]+", child).group(0)
            all_bags[bags[0]].children[color] = number
            if color not in all_bags:
                all_bags[color] = Node(color)
            all_bags[color].parents.append(bags[0])

    # Now that we have our tree, we start at "shiny gold" and find all its parents up to the roots
    all_parents = set()
    queue = deque(all_bags["shiny gold"].parents)
    while queue:
        parent = queue.popleft()
        if parent not in all_parents:
            all_parents.add(parent)
            queue.extend(all_bags[parent].parents)

    # We also need to get the bags inside the "shiny gold" bag, so do a recursive count
    def total_bags(color):
        total = 1 # Start with one for the current bag
        for child, count in all_bags[color].children.items():
            total += int(count) * total_bags(child)
        return total
    all_children = total_bags("shiny gold") - 1 # need to subtract one because we're not counting the shiny gold bag itself

    return len(all_parents), all_children


def part1(values):
    return parse_bags(values)[0]


def part2(values):
    return parse_bags(values)[1]
