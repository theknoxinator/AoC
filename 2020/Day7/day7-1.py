# Determine how many bags contain at least one shiny gold bag
from collections import deque
import re


def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags."]


print("Starting Day7-1")
values = read_file("input.txt")
# values = test_data()


# To solve this we are going to create a parent-child tree with all possible bags, so we need a node class to store the
# parents and children. Children is a map of name to number because it will obviously be needed for part 2.
class Node:
    def __init__(self, color):
        self.color = color
        self.parents = []
        self.children = {}


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

print("Total number of parents: {0!s}".format(len(all_parents)))
print(all_parents)
