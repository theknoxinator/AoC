# Determine the last elf in the group as they keep stealing gifts from each other

class Node:
    def __init__(self, index):
        self.index = index
        self.gifts = 1


def find_elf(values):
    elves = int(values[0])
    # For ease of use with this problem, we will use a circular linked list where each node is an elf with an index and
    # number of gifts

    # Initialize the list
    start = Node(0)
    end = start
    for index in range(1, elves):
        next = Node(index)
        end.next = next
        end = next
    end.next = start

    # Now play the game, removing each node with 0 gifts along the way
    current = start
    while current.next != current:
        next = current.next
        current.gifts += next.gifts
        current.next = next.next;
        del next
        current = current.next

    return current.index + 1


def find_elf2(values):
    elves = int(values[0])
    # For this version, we still want to keep the circular linked list, and this time we have a runner that goes around
    # the circle until it reaches halfway around, and we remove that node

    # Initialize the list
    start = Node(0)
    end = start
    length = elves
    for index in range(1, length):
        next = Node(index)
        end.next = next
        end = next
    end.next = start

    # Now play the game, removing nodes across from the current
    current = start
    runner = start
    for _ in range(int(length/2)):
        runner = runner.next
    while length > 1:
        runner.index = runner.next.index
        runner.next = runner.next.next
        current = current.next
        length -= 1
        if length % 2 == 0:
            runner = runner.next

    return current.index + 1


def part1(values):
    return find_elf(values)


def part2(values):
    return find_elf2(values)
