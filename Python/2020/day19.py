# Determine how many possible messages match the rules

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


def match_rules(values, use_part2=False):
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

    if not use_part2:
        # Finally, iterate through the messages and determine how many are in rule 0
        count = 0
        for message in messages:
            if message in rules['0'].options:
                count += 1

        return count

    # Finally, iterate through the messages and determine how many are in rule 0
    # For ease of use for this one, we just check each substring to see if it fits in either rule 42 or 31 (looping)
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
            count += 1

    return count


def part1(values):
    return match_rules(values)


def part2(values):
    return match_rules(values, True)
