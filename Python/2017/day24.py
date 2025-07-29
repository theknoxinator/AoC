# Part 1: Given a set of bridge components, find the combination that results in the highest sum of ports
# Part 2: Given the same components and build strategy, find the combination that has the highest sum but is also as long as possible

class Node:
    def __init__(self, val, path):
        self.val = val
        self.path = path
        self.children = []


def build_tree(current_node, remaining):
    for component in remaining:
        if component[0] == current_node.val:
            current_node.children.append(Node(component[1], current_node.path | {component}))
        elif component[1] == current_node.val:
            current_node.children.append(Node(component[0], current_node.path | {component}))

    for child in current_node.children:
        build_tree(child, remaining - child.path)


def create_bridges(values, use_part2=False):
    all_components = set()
    for val in values:
        x, y = list(map(int, val.split('/')))
        all_components.add((x, y))

    # Build the tree from the root which starts with a 0 port
    root_node = Node(0, set())
    build_tree(root_node, all_components)

    # Once tree has been created, we can just do a depth-first-search to find the path with the highest sum
    def dfs_tree(node, depth):
        all_sums = []
        if node.children:
            for child in node.children:
                all_sums.extend(dfs_tree(child, depth + 1))
        else:
            current_sum = 0
            for component in node.path:
                current_sum += component[0] + component[1]
            all_sums.append((depth, current_sum))

        return all_sums


    all_sums = dfs_tree(root_node, 0)

    # For part 1, just return the highest value
    if not use_part2:
        all_strengths = [x[1] for x in all_sums]
        return max(all_strengths)

    # For part 2, return the highest value of paths that also have the highest depth
    longest_length = max([x[0] for x in all_sums])
    longest_strengths = [x[1] for x in all_sums if x[0] == longest_length]
    return max(longest_strengths)


def part1(values):
    return create_bridges(values)


def part2(values):
    return create_bridges(values, True)
