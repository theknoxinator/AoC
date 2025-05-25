# Determine the number of invalid tickets based on rules for what numbers are allowed
import re


def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["class: 1-3 or 5-7",
            "row: 6-11 or 33-44",
            "seat: 13-40 or 45-50",
            "",
            "your ticket:",
            "7,1,14",
            "",
            "nearby tickets:",
            "7,3,47",
            "40,4,50",
            "55,2,20",
            "38,6,12"]


print("Starting Day16-1")
values = read_file("input.txt")
# values = test_data()

# Before we do any processing, we need to just parse the file into appropriate parts
breaks = 0
rules = dict()
your_ticket = []
nearby_tickets = []
for val in values:
    if val == "":
        # We have a break
        breaks += 1
        continue
    if breaks == 0:
        # We are in the rules section, so split it up
        regex_result = re.search("(\w+): ([0-9]+-[0-9]+) or ([0-9]+-[0-9]+)", val)
        rules[regex_result.group(1)] = {'bot_low': int(regex_result.group(2).split('-')[0]),
                                        'bot_high': int(regex_result.group(2).split('-')[1]),
                                        'top_low': int(regex_result.group(3).split('-')[0]),
                                        'top_high': int(regex_result.group(3).split('-')[1])}
    elif breaks == 1:
        # This should be the your ticket section
        if "your ticket" in val:
            continue
        else:
            your_ticket = [int(x) for x in val.split(',')]
    elif breaks == 2:
        # This should be the nearby tickets section
        if "nearby tickets" in val:
            continue
        else:
            nearby_tickets.append([int(x) for x in val.split(',')])

print(rules)
print(your_ticket)
print(nearby_tickets)

# Now do the processing, in this case we are detecting which values cannot fit in any rule and track them
invalid_fields = []
for ticket in nearby_tickets:
    for field in ticket:
        matches_rule = False
        for rule in rules.values():
            if rule['bot_low'] <= field <= rule['bot_high'] or rule['top_low'] <= field <= rule['top_high']:
                matches_rule = True
        if not matches_rule:
            invalid_fields.append(field)

print(invalid_fields)
print("The ticket scanning error rate is: {0!s}".format(sum(invalid_fields)))
