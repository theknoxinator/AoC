# Determine the highest seat ID based on boarding pass input

def get_highest_id(values):
    # Implement a recursive function that finds a row/col using BST algo
    def tree_find(low, high, length, id):
        if not id:
            return low
        direction = id[0]
        if direction == 'F' or direction == 'L':
            return tree_find(low, high / 2, length / 2, id[1:])
        elif direction == 'B' or direction == 'R':
            return tree_find(low + length / 2, high, length / 2, id[1:])

    # This is pretty simple to start, we just iterate through the whole list find the seat ID for each one
    highest_seat = {}
    all_seat_ids = []
    for val in values:
        row_id = val[:7]
        col_id = val[-3:]
        row = tree_find(0, 127, 128, row_id)
        col = tree_find(0, 7, 8, col_id)
        seat_id = row * 8 + col
        all_seat_ids.append(seat_id)
        if "seat_id" not in highest_seat or highest_seat["seat_id"] < seat_id:
            highest_seat = {"id": val, "row": row, "col": col, "seat_id": seat_id}

    my_seat = 0
    for id in sorted(all_seat_ids):
        if my_seat == 0 or my_seat + 1 == int(id):
            my_seat = int(id)
        elif my_seat + 1 < int(id):
            my_seat = int(id) - 1
            break

    return int(highest_seat["seat_id"]), my_seat


def part1(values):
    return get_highest_id(values)[0]


def part2(values):
    return get_highest_id(values)[1]
