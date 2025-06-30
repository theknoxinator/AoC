# Determine which bot is handling the target microchips based on starting chips and instructions on
# how they get passed around

def run_program(values):
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
    solution_bot = -1
    had_action = True
    while had_action:
        had_action = False
        for index in range(len(bots)):
            # Our end condition for this problem is if a bot has chips 17 and 61
            if 17 in bots[index].chips and 61 in bots[index].chips:
                solution_bot = index

            if bots[index].can_act():
                bots[index].transfer()
                had_action = True

    return solution_bot, (outputs[0].chips[0] * outputs[1].chips[0] * outputs[2].chips[0])


def part1(values):
    return run_program(values)[0]


def part2(values):
    return run_program(values)[1]
