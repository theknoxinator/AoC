# Determine how many possible messages match the rules

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["0: 4 1 5",
            "1: 2 3 | 3 2",
            "2: 4 4 | 5 5",
            "3: 4 5 | 5 4",
            '4: "a"',
            '5: "b"',
            "",
            "ababbb",
            "bababa",
            "abbbab",
            "aaabbb",
            "aaaabbb"]


print("Starting Day19-1")
values = read_file("input.txt")
# values = test_data()


class Rule:
    def __init__(self, definition):
        self.definition = definition
        self.children = self.parse_children()
        self.options = self.parse_options()

    def __repr__(self):
        return str(self.options)

    def parse_children(self):
        children = []
        if '"' not in self.definition:
            for child_set in self.definition.split('|'):
                children.append(child_set.strip().split(' '))
        return children

    def parse_options(self):
        options = set()
        if '"' in self.definition:
            options.add(self.definition.strip().replace('"',''))
        return options


breaks = 0
rules = dict()
messages = []
# First we need to go through each line of rules and store them as rule objects, then store each message
for val in values:
    if val == "":
        # We have a break
        breaks += 1
        continue
    if breaks == 0:
        rule_name, rule_def = val[:val.find(':')], val[val.find(':') + 1:]
        rules[rule_name] = Rule(rule_def)
    elif breaks == 1:
        messages.append(val)


def process_options(children):
    options = {""}
    for child in children:
        new_options = set()
        for prefix in options:
            for option in rules[child].options:
                new_options.add(prefix + option)
        options = new_options
    return options


# Now we will iterate through the rules until all options have been processed
rules_filled = False
while not rules_filled:
    rules_filled = True
    print(rules)
    for rule in rules.values():
        if len(rule.options) > 0:
            continue
        else:
            rules_filled = False
        option_lengths = [len(rules[child].options) for child_set in rule.children for child in child_set]
        if all(option_lengths):
            for child_set in rule.children:
                rule.options = rule.options.union(process_options(child_set))

# Finally, iterate through the messages and determine how many are in rule 0
count = 0
for message in messages:
    if message in rules['0'].options:
        count += 1

print("The number of messages that match rule 0: {0!s}".format(count))
