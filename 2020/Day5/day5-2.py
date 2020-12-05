# Determine the your seat ID based on boarding pass input

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


print("Starting Day5-2")
values = read_file("input.txt")
# values = test_data()


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
all_seat_ids = []
for val in values:
    row_id = val[:7]
    col_id = val[-3:]
    row = tree_find(0, 127, 128, row_id)
    col = tree_find(0, 7, 8, col_id)
    seat_id = row * 8 + col
    print("{0} - Row: {1!s}, Col: {2!s}, Seat ID: {3!s}".format(val, row, col, seat_id))
    all_seat_ids.append(seat_id)

my_seat = 0
for id in sorted(all_seat_ids):
    if my_seat == 0 or my_seat + 1 == int(id):
        my_seat = int(id)
    elif my_seat + 1 < int(id):
        my_seat = int(id) - 1
        break

print("My seat:", my_seat)
