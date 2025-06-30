# Determine how many triangle length sets are valid triangle lengths

def get_valid_triangles(values, use_vertical=False):
    # Convert the values into a table that can be read either way
    table = []
    for val in values:
        table.append(list(map(int, val.split())))

    all_triangles = []
    if not use_vertical:
        all_triangles = table
    else:
        for offset in range(0, len(table), 3):
            for col in range(3):
                all_triangles.append((table[offset][col], table[offset + 1][col], table[offset + 2][col]))

    # Iterate and check to see if each set of values makes a valid triangle
    valid_triangles = 0
    for sides in all_triangles:
        # Check each way is valid
        one_valid = sides[0] < (sides[1] + sides[2])
        two_valid = sides[1] < (sides[0] + sides[2])
        thr_valid = sides[2] < (sides[0] + sides[1])

        if one_valid and two_valid and thr_valid:
            valid_triangles += 1

    return valid_triangles


def part1(values):
    return get_valid_triangles(values)


def part2(values):
    return get_valid_triangles(values, True)
