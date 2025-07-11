# Determine the winning score in a marble game where each marble has ascending value and is placed/removed
# in a specific order, based on the number of players

def play_game(values):
    players = int(values[0])
    last_marble = int(values[1])

    # There is no real setup for this one, we just need to keep track of the marbles in play and what
    # each player currently has for score
    player_scores = [0] * players

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
    while marble_number <= last_marble:
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
            current_player = marble_number % players - 1
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

    # Print out answer
    high_score = 0
    for player_score in player_scores:
        if player_score > high_score:
            high_score = player_score
    return high_score


def part1(values):
    return play_game(values)


def part2(values):
    values[1] = values[1] + "00"
    return play_game(values)
