# Determine how many possible messages match the rules

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["42: 9 14 | 10 1",
            "9: 14 27 | 1 26",
            "10: 23 14 | 28 1",
            '1: "a"',
            "11: 42 31",
            "5: 1 14 | 15 1",
            "19: 14 1 | 14 14",
            "12: 24 14 | 19 1",
            "16: 15 1 | 14 14",
            "31: 14 17 | 1 13",
            "6: 14 14 | 1 14",
            "2: 1 24 | 14 4",
            "0: 8 11",
            "13: 14 3 | 1 12",
            "15: 1 | 14",
            "17: 14 2 | 1 7",
            "23: 25 1 | 22 14",
            "28: 16 1",
            "4: 1 1",
            "20: 14 14 | 1 15",
            "3: 5 14 | 16 1",
            "27: 1 6 | 14 18",
            '14: "b"',
            "21: 14 1 | 1 14",
            "25: 1 1 | 1 14",
            "22: 14 14",
            "8: 42",
            "26: 14 22 | 1 20",
            "18: 15 15",
            "7: 14 5 | 1 21",
            "24: 14 1",
            "",
            "abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa",
            "bbabbbbaabaabba",
            "babbbbaabbbbbabbbbbbaabaaabaaa",
            "aaabbbbbbaaaabaababaabababbabaaabbababababaaa",
            "bbbbbbbaaaabbbbaaabbabaaa",
            "bbbababbbbaaaaaaaabbababaaababaabab",
            "ababaaaaaabaaab",
            "ababaaaaabbbaba",
            "baabbaaaabbaaaababbaababb",
            "abbbbabbbbaaaababbbbbbaaaababb",
            "aaaaabbaabaaaaababaa",
            "aaaabbaaaabbaaa",
            "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa",
            "babaaabbbaaabaababbaabababaaab",
            "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"]


print("Starting Day19-2")
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
            options.add(self.definition.strip().replace('"', ''))
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
# For ease of use for this one, we just check each substring to see if it fits in either rule 42 or 31 (looping)
print(rules['42'])
print(rules['31'])
count = 0
for message in messages:
    remaining = message[:]
    switched = False
    chunks_42 = 0
    chunks_31 = 0
    matches = True
    while remaining:
        chunk = remaining[:8]
        if not switched:
            if chunk not in rules['42'].options:
                switched = True
            else:
                chunks_42 += 1
        if switched:
            if chunk not in rules['31'].options:
                matches = False
            else:
                chunks_31 += 1
        if not matches:
            break
        remaining = remaining[8:]
    if matches and chunks_42 > 0 and chunks_31 > 0 and chunks_42 >= chunks_31 + 1:
        print(message)
        count += 1

print("The number of messages that match rule 0: {0!s}".format(count))
