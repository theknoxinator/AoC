# Determine the winning bingo board based on a list of numbers to be called
class BingoBoard:
    def __init__(self, board_lines):
        self.rows = []
        for line in board_lines:
            self.rows.append([int(x) for x in line.split()])
        self.marked = [[False] * 5 for _ in range(5)]
        self.row_marked = [0] * 5
        self.col_marked = [0] * 5
        self.number_set = set()
        for row in self.rows:
            for number in row:
                self.number_set.add(number)

    def mark(self, number):
        if number not in self.number_set:
            return
        for row_index, row in enumerate(self.rows):
            for col_index, col in enumerate(row):
                if col == number:
                    self.marked[row_index][col_index] = True
                    self.row_marked[row_index] += 1
                    self.col_marked[col_index] += 1
                    return

    def has_bingo(self):
        return 5 in self.row_marked or 5 in self.col_marked

    def get_score(self):
        score = 0
        for row_index, row in enumerate(self.rows):
            for col_index, col in enumerate(row):
                if not self.marked[row_index][col_index]:
                    score += col
        return score

    def print(self):
        print('')
        for row_index, row in enumerate(self.rows):
            print(' '.join(map(str, row)))


def parse_boards(values):
    bingo_numbers = [int(x) for x in values[0].split(',')]
    bingo_boards = []
    board_count = int((len(values) - 1) / 6)
    for board_index in range(board_count):
        board_start = board_index * 6 + 2
        bingo_boards.append(BingoBoard(values[board_start:board_start + 5]))
    # print(f'Bingo numbers: {",".join(map(str, bingo_numbers))}')
    # for bingo_board in bingo_boards:
    #     bingo_board.print()

    return bingo_numbers, bingo_boards


def part1(values):
    # First we parse the file for the list of numbers followed by the boards
    bingo_numbers, bingo_boards = parse_boards(values)

    # Next we iterate through the list of bingo numbers and mark them off on each board
    winning_board = None
    last_bingo_number = -1
    for current_bingo_number in bingo_numbers:
        for bingo_board in bingo_boards:
            bingo_board.mark(current_bingo_number)
            if bingo_board.has_bingo():
                winning_board = bingo_board
                break
        if winning_board:
            last_bingo_number = current_bingo_number
            break
    winning_score = winning_board.get_score()
    print(f'Last bingo number: {last_bingo_number!s}')
    print(f'Winning score: {winning_score!s}')

    return winning_score * last_bingo_number


def part2(values):
    # First we parse the file for the list of numbers followed by the boards
    bingo_numbers, bingo_boards = parse_boards(values)

    # Next we iterate through the list of bingo numbers and mark them off on each board
    # We only stop once all boards have won
    winning_boards = []
    last_bingo_number = -1
    for current_bingo_number in bingo_numbers:
        for bingo_board in bingo_boards:
            if bingo_board.has_bingo():
                continue
            bingo_board.mark(current_bingo_number)
            if bingo_board.has_bingo():
                winning_boards.append(bingo_board)
        if len(winning_boards) == len(bingo_boards):
            last_bingo_number = current_bingo_number
            break
    winning_score = winning_boards[-1].get_score()
    print(f'Last bingo number: {last_bingo_number!s}')
    print(f'Winning score: {winning_score!s}')

    return winning_score * last_bingo_number
