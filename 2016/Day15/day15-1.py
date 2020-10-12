# Determine the time when a capsule can be dropped based on the rotation of several discs


class Disc:
    def __init__(self, positions, start):
        self.positions = positions
        self.current = start


'''
discs = [
    Disc(5, 4),
    Disc(2, 1)
]
'''

'''
Disc #1 has 13 positions; at time=0, it is at position 11.
Disc #2 has 5 positions; at time=0, it is at position 0.
Disc #3 has 17 positions; at time=0, it is at position 11.
Disc #4 has 3 positions; at time=0, it is at position 0.
Disc #5 has 7 positions; at time=0, it is at position 2.
Disc #6 has 19 positions; at time=0, it is at position 17.
'''
discs = [
    Disc(13, 11),
    Disc(5, 0),
    Disc(17, 11),
    Disc(3, 0),
    Disc(7, 2),
    Disc(19, 17),
    Disc(11, 0) # This is new for part 2
]


if __name__ == '__main__':
    print("Starting Day 15-1/2")

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

    # Print out answer
    print("The first start time that works is {0!s}".format(start_time))
