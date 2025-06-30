# Determine the time when a capsule can be dropped based on the rotation of several discs

class Disc:
    def __init__(self, positions, start):
        self.positions = positions
        self.current = start


def get_discs(values):
    discs = []
    for val in values:
        pos,start = val.split(',')
        discs.append(Disc(int(pos), int(start)))
    return discs


def rotate_discs(values):
    discs = get_discs(values)
    # For this we can just start at a certain time, check where each disc will be at each following second and see if
    # they all end up being zero using modulo math
    start_time = 0
    got_through = False
    while not got_through:
        got_through = True
        time = start_time + 1
        for index in range(len(discs)):
            position = (discs[index].current + time + index) % discs[index].positions
            if position != 0:
                got_through = False
                break

        if not got_through:
            start_time += 1

    return start_time


def part1(values):
    return rotate_discs(values)


def part2(values):
    values.append("11,0")
    return rotate_discs(values)
