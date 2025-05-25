# Figure out how many recipes are created before the target recipe sequence is created
from collections import deque

TARGET_RECIPE = "765071"

if __name__ == '__main__':
    print("Starting Day 14-2")

    # Trying different algorithm based on something found online, uses a string to store the values instead
    # of a linked list, much less memory that way
    recipes = "37" # Starting recipes
    first = 0 # Starting index
    second = 1
    while TARGET_RECIPE not in recipes[-7:]:
        recipes = recipes + str(int(recipes[first]) + int(recipes[second]))
        first = (first + int(recipes[first]) + 1) % len(recipes)
        second = (second + int(recipes[second]) + 1) % len(recipes)

    print("Recipes before sequence: {0!s}".format(recipes.index(TARGET_RECIPE)))

    # # Due to the nature of the algorithm involved, it makes the most sense to just use a singly-linked list
    # class Node:
    #     def __init__(self, index, value, next=None):
    #         self.index = index
    #         self.value = value
    #         self.next = next
    #
    # # We start with 3 and 7 already defined as the head and tail, and list circles so tail always has head
    # # as the next node
    # head = Node(1, 3)
    # tail = Node(2, 7)
    # head.next = tail
    # tail.next = head
    #
    # # Our end condition is to get a sequence that matches the target, so we will store the current last
    # # X values in a queue that we will read each addition to see if we get it
    # last_values = deque()
    # first = head
    # second = tail
    # while True:
    #     # Debug print out the list
    #     # runner = head
    #     # while runner != tail:
    #     #     print(str(runner.value), end='')
    #     #     runner = runner.next
    #     # print(str(tail.value))
    #
    #     # Get the two recipes being looked at by the first and second runners
    #     first_recipe = first.value
    #     second_recipe = second.value
    #     sum = first_recipe + second_recipe
    #
    #     # If there are two digits, we need to add the tens digit first
    #     if sum >= 10:
    #         # Calculate new recipe value and list index
    #         new_recipe = int(sum / 10)
    #         new_index = tail.index + 1
    #
    #         # Add new recipe to last values and check to see if it's a sequence match
    #         if len(last_values) == len(TARGET_RECIPE):
    #             last_values.popleft()
    #         last_values.append(str(new_recipe))
    #         current_sequence = ''.join(list(last_values))
    #         print(current_sequence)
    #         if current_sequence  == TARGET_RECIPE:
    #             # Found a match, so find the number of recipes before the target
    #             print("Number of recipes that happened before sequence {0}: {1!s}".format(TARGET_RECIPE, new_index - len(last_values)))
    #             break
    #
    #         # If we haven't found the target sequence, continue on by adding to list
    #         new_node = Node(new_index, new_recipe, head)
    #         tail.next = new_node
    #         tail = new_node
    #
    #     # In all cases, add the ones digit as a new recipe
    #     new_recipe = sum % 10
    #     new_index = tail.index + 1
    #
    #     # Add new recipe to last values and check to see if it's a sequence match
    #     if len(last_values) == len(TARGET_RECIPE):
    #         last_values.popleft()
    #     last_values.append(str(new_recipe))
    #     current_sequence = ''.join(list(last_values))
    #     print(current_sequence)
    #     if current_sequence == TARGET_RECIPE:
    #         # Found a match, so find the number of recipes before the target
    #         print("Number of recipes that happened before sequence {0}: {1!s}".format(TARGET_RECIPE, new_index - len(last_values)))
    #         break
    #
    #     # If we haven't found the target sequence, continue on by adding to list
    #     new_node = Node(new_index, new_recipe, head)
    #     tail.next = new_node
    #     tail = new_node
    #
    #     # New recipes are added, so move up each runner
    #     first_moves = first.value + 1
    #     for i in range(first_moves):
    #         first = first.next
    #     second_moves = second.value + 1
    #     for i in range(second_moves):
    #         second = second.next
