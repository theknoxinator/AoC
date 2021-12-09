# Determine the number of overlapping spaces on a grid of lines
def get_coord_count(values, count_diags=False):
    # First we parse the file into lines and store the coordinates in a map
    coord_counter = dict()
    for line_coords in values:
        start, end = line_coords.split(' -> ')
        start_x, start_y = (int(x) for x in start.split(','))
        end_x, end_y = (int(y) for y in end.split(','))
        # Depending on what kind of line it is, generate the coordinates between points
        if start_x == end_x:
            min_y = min(start_y, end_y)
            max_y = max(start_y, end_y)
            for next_y in range(min_y, max_y + 1):
                next_coord = (start_x, next_y)
                if next_coord in coord_counter:
                    coord_counter[next_coord] += 1
                else:
                    coord_counter[next_coord] = 1
        elif start_y == end_y:
            min_x = min(start_x, end_x)
            max_x = max(start_x, end_x)
            for next_x in range(min_x, max_x + 1):
                next_coord = (next_x, start_y)
                if next_coord in coord_counter:
                    coord_counter[next_coord] += 1
                else:
                    coord_counter[next_coord] = 1
        elif count_diags:
            step_x = 1
            if end_x > start_x:
                end_x += 1
            elif end_x < start_x:
                step_x = -1
                end_x -= 1
            x_coords = list(range(start_x, end_x, step_x))
            step_y = 1
            if end_y > start_y:
                end_y += 1
            elif end_y < start_y:
                step_y = -1
                end_y -= 1
            y_coords = list(range(start_y, end_y, step_y))
            for index in range(len(x_coords)):
                next_coord = (x_coords[index], y_coords[index])
                if next_coord in coord_counter:
                    coord_counter[next_coord] += 1
                else:
                    coord_counter[next_coord] = 1

    return coord_counter


def get_overlap_count(coord_counter):
    overlap_count = 0
    for coord, count in coord_counter.items():
        if count > 1:
            overlap_count += 1
    return overlap_count


def part1(values):
    coord_counter = get_coord_count(values)

    return get_overlap_count(coord_counter)


def part2(values):
    # This is exactly the same as part1 but with diagonals added
    coord_counter = get_coord_count(values, True)

    return get_overlap_count(coord_counter)
