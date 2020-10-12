# Determine the winning score in a marble game where each marble has ascending value and is placed/removed
# in a specific order, based on the number of players

PLAYERS = 476
LAST_MARBLE = 71657

if __name__ == '__main__':
    print("Starting Day9-1")

    # There is no real setup for this one, we just need to keep track of the marbles in play and what
    # each player currently has for score
    player_scores = [0]*PLAYERS
    current_marble = 0
    marbles = [0]

    # Start the loop with marble 1, finish the loop when the last marble pulled is equal to the expected
    last_marble = 0
    marble_number = 1
    while marble_number <= LAST_MARBLE:
        #print("[{0}]".format(','.join(map(str, marbles))))
        if marble_number % 10000 == 0:
            print(str(marble_number))
        # If the marble number is a multiple of 23, we do different things
        if marble_number % 23 == 0:
            marble_to_remove = current_marble - 7
            if marble_to_remove < 0:
                marble_to_remove += len(marbles)
            removed_marble = marbles.pop(marble_to_remove)

            # Determine which player is currently going
            current_player = marble_number % PLAYERS - 1
            player_scores[current_player] += removed_marble + marble_number
            last_marble = removed_marble
            current_marble = marble_to_remove
        else:
            # Otherwise, just do a standard insert
            new_marble = current_marble + 2
            if current_marble + 1 >= len(marbles):
                new_marble -= len(marbles)
            elif current_marble + 2 >= len(marbles):
                new_marble = len(marbles)

            marbles.insert(new_marble, marble_number)
            current_marble = new_marble
        marble_number += 1
        #print("[{0}]".format(','.join(map(str, marbles))))

    # Print out answer
    print("The final scores of the players is: [{0}]".format(','.join(map(str, player_scores))))
    high_score = 0
    for player_score in player_scores:
        if player_score > high_score:
            high_score = player_score
    print("The highest score is: {0!s}".format(high_score))

