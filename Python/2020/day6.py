# Parse bulk file of customs answer and determine how many questions were answered yes

def do_customs(values, use_part2=False):
    # Just like with the passports, we parse each group in place and add their question total to a list that we will sum
    # at the end
    values.append("")
    groups = []
    current_group = None
    for line in values:
        if len(line) < 1:
            # We have reached an empty line, so compute current group
            groups.append(len(current_group))
            current_group = None
        else:
            # Depending on the part, we either union or intersect the set
            if current_group is None:
                current_group = set(line)
            else:
                if use_part2:
                    current_group = current_group & set(line)
                else:
                    current_group = current_group | set(line)

    return sum(groups)


def part1(values):
    return do_customs(values)


def part2(values):
    return do_customs(values, True)
