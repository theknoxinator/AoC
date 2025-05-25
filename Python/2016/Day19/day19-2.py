# Determine the last elf in the group as they keep stealing gifts from each other
# For part 2, they steal from across the circle rather than the elf to their left

test_data = 10
input = 3017957

if __name__ == "__main__":
    print("Starting Day 19-2")

    # For this version, we still want to keep the circular linked list, and this time we have a runner that goes around
    # the circle until it reaches halfway around, and we remove that node
    class Node:
        def __init__(self, index):
            self.index = index

    # Initialize the list
    start = Node(0)
    end = start
    length = input
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
        print(length)

    # Print out answer
    print("The winning elf is: {0!s}".format(current.index + 1))
