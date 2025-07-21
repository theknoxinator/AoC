# Determine the number of invalid tickets based on rules for what numbers are allowed
import re

def invalid_tickets(values):
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

    return sum(invalid_fields)


def valid_tickets(values):
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
            regex_result = re.search("([\w\s]+): ([0-9]+-[0-9]+) or ([0-9]+-[0-9]+)", val)
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

    # Now do the processing, in this case we are determining which field is which
    # First we need to get rid of the invalid tickets
    valid_tickets = []
    for ticket in nearby_tickets:
        valid_ticket = True
        for field in ticket:
            matches_rule = False
            for rule in rules.values():
                if rule['bot_low'] <= field <= rule['bot_high'] or rule['top_low'] <= field <= rule['top_high']:
                    matches_rule = True
            if not matches_rule:
                valid_ticket = False
        if valid_ticket:
            valid_tickets.append(ticket)

    # Now that we have the valid tickets, we will add each field for each ticket into separate buckets for determining
    # which field each is
    tickets_by_fields = []
    for field in your_ticket:
        tickets_by_fields.append([field])
    for ticket in valid_tickets:
        for i, field in enumerate(ticket):
            tickets_by_fields[i].append(field)

    column_by_rule = dict()
    for i, field_column in enumerate(tickets_by_fields):
        for name, rule in rules.items():
            matches_rule = True
            for field in field_column:
                if not (rule['bot_low'] <= field <= rule['bot_high'] or rule['top_low'] <= field <= rule['top_high']):
                    matches_rule = False
                    break
            if matches_rule:
                if name not in column_by_rule:
                    column_by_rule[name] = []
                column_by_rule[name].append(i)

    # Our columns can apply to multiple rules, so we need to iterate through until each column has only one rule
    rule_matched = set()
    while len(rule_matched) < len(rules):
        for columns in column_by_rule.values():
            if len(columns) == 1:
                rule_matched.add(columns[0])
            else:
                for matched in rule_matched:
                    if matched in columns:
                        columns.remove(matched)

    # Now that we have the rules, we can finally determine the fields with "departure" in the name
    result = 1
    for rule, columns in column_by_rule.items():
        if "departure" in rule:
            result *= your_ticket[columns[0]]

    return result


def part1(values):
    return invalid_tickets(values)


def part2(values):
    return valid_tickets(values)
