# Determine which bot is handling the target microchips based on starting chips and instructions on
# how they get passed around

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["value 5 goes to bot 2",
            "bot 2 gives low to bot 1 and high to bot 0",
            "value 3 goes to bot 1",
            "bot 1 gives low to output 1 and high to bot 0",
            "bot 0 gives low to output 2 and high to output 0",
            "value 2 goes to bot 2"]


if __name__ == '__main__':
    print("Starting Day 10-1")
    values = read_file('input.txt')
    # values = test_data()

    # First, create the classes we need for bots and outputs, and create a bucket for each type so that
    # we can interact with them
    # Maximum bots is 220, maximum output is 30
    class Output:
        def __init__(self):
            self.chips = []

    class Bot:
        def __init__(self):
            self.low_target = None
            self.high_target = None
            self.chips = []

        def can_act(self):
            return len(self.chips) == 2

        def transfer(self):
            if self.can_act():
                low_chip = min(self.chips)
                high_chip = max(self.chips)
                self.low_target.chips.append(low_chip)
                self.high_target.chips.append(high_chip)
                self.chips.clear()

    outputs = [Output() for i in range(30)]
    bots = [Bot() for i in range(220)]

    # Now we can iterate through the instructions and determine the rules and initial state
    for val in values:
        if "value" in val:
            # This sets an initial chip to a bot
            items = val.split()
            chip = int(items[1])
            target_bot = int(items[5])

            bots[target_bot].chips.append(chip)
        else:
            # This is an instruction for a bot who has two chips
            items = val.split()
            target_bot = int(items[1])
            if items[5] == "output":
                bots[target_bot].low_target = outputs[int(items[6])]
            elif items[5] == "bot":
                bots[target_bot].low_target = bots[int(items[6])]
            if items[10] == "output":
                bots[target_bot].high_target = outputs[int(items[11])]
            elif items[10] == "bot":
                bots[target_bot].high_target = bots[int(items[11])]

    # Now that we have everything setup, walk through each bot and perform an action if they can
    # and keep repeating until we find our end condition
    had_action = True
    while had_action:
        had_action = False
        for index in range(len(bots)):
            # Our end condition for this problem is if a bot has chips 17 and 61
            if 17 in bots[index].chips and 61 in bots[index].chips:
                print("The bot with chips 17 and 61 is: {0!s}".format(index))

            if bots[index].can_act():
                bots[index].transfer()
                had_action = True

    # Print out the outputs
    for index in range(len(outputs)):
        print("Output [{0!s}]: {1!s}".format(index, outputs[index].chips))
