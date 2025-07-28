# Determine the number of times we get caught in the firewall

def firewall(values, use_part2=False):
    layers = []
    for val in values:
        layers.append((int(x) for x in val.strip().replace(' ', '').split(':')))

    # Since we only get caught at the top of the layer, we only need to know on which seconds the top is occupied
    # This can be calculated as (layer_depth - 2) * 3 + 2
    # As the layers never change, we can store this is a list of tuples
    loop_lengths = [(x, y, (y - 2) * 2 + 2) for x, y in layers]

    # To go through the firewall, we check each loop length against the offset + layer_depth
    # Put this check in a function so that it can be reused for part 2 where offset increments
    offset = 0
    def get_violations(offset, loop_lengths, interrupt=False):
        violations = []
        for layer, depth, loop in loop_lengths:
            if (offset + layer) % loop == 0:
                # We have a collision, add to violations list
                violations.append((layer, depth))
            if violations and interrupt:
                break
        return violations

    if not use_part2:
        violations = get_violations(offset, loop_lengths)
        severity = 0
        for layer, depth in violations:
            severity += layer * depth

        return severity

    # For part 2, we increase offset until we get a set with no violations (runs at O(n^2))
    # Since we know layer 1 is only 2 depth (in real problem and sample), we can rule out all odd seconds
    while True:
        violations = get_violations(offset, loop_lengths, True)
        if violations:
            offset += 2
        else:
            return offset


def part1(values):
    return firewall(values)


def part2(values):
    return firewall(values, True)
