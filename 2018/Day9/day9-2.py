# Determine the winning score in a marble game where each marble has ascending value and is placed/removed
# in a specific order, based on the number of players
import time

PLAYERS = 476
LAST_MARBLE = 7165700

if __name__ == '__main__':
    print("Starting Day9-2")
    start_time = time.time()

    # There is no real setup for this one, we just need to keep track of the marbles in play and what
    # each player currently has for score
    player_scores = [0]*PLAYERS

    # For this iteration, going to create a circular linked list instead of a normal list
    class Node:
        def __init__(self, value, next=None, prev=None):
            self.value = value
            self.next = next
            self.prev = prev

    start_node = Node(0)
    start_node.next = start_node
    start_node.prev = start_node

    # Start the loop with marble 1, finish the loop when the last marble pulled is equal to the expected
    marble_number = 1
    current_marble = start_node
    while marble_number <= LAST_MARBLE:
        if marble_number % 10000 == 0:
            print(str(marble_number))

        # If the marble number is a multiple of 23, we do different things
        if marble_number % 23 == 0:
            marble_to_remove = current_marble
            for i in range(7):
                marble_to_remove = marble_to_remove.prev
            removed_marble = marble_to_remove.value
            left_marble = marble_to_remove.prev
            right_marble = marble_to_remove.next
            left_marble.next = marble_to_remove.next
            right_marble.prev = marble_to_remove.prev
            del marble_to_remove

            # Determine which player is currently going
            current_player = marble_number % PLAYERS - 1
            player_scores[current_player] += removed_marble + marble_number
            current_marble = right_marble
        else:
            # Otherwise, just do a standard insert
            left_marble = current_marble.next
            right_marble = current_marble.next.next
            new_marble = Node(marble_number, right_marble, left_marble)
            left_marble.next = new_marble
            right_marble.prev = new_marble
            current_marble = new_marble
        marble_number += 1

    end_time = time.time()
    print("Time taken: {0!s}".format(end_time - start_time))

    # Print out answer
    print("The final scores of the players is: [{0}]".format(','.join(map(str, player_scores))))
    high_score = 0
    for player_score in player_scores:
        if player_score > high_score:
            high_score = player_score
    print("The highest score is: {0!s}".format(high_score))

