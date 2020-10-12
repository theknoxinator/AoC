# Determine the last elf in the group as they keep stealing gifts from each other

test_data = 5
input = 3017957

if __name__ == "__main__":
    print("Starting Day 19-1")

    # For ease of use with this problem, we will use a circular linked list where each node is an elf with an index and
    # number of gifts
    class Node:
        def __init__(self, index):
            self.index = index
            self.gifts = 1

    # Initialize the list
    start = Node(0)
    end = start
    for index in range(1, input):
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

    # Print out answer
    print("The winning elf is: {0!s}".format(current.index + 1))
