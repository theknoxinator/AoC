# Determine the outcome of combat between elves and goblins using simple pathfinding and combat mechanics
from collections import deque


def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.rstrip())

    return values


def test_data():
    # return ["#######",
    #         "#.G...#",
    #         "#...EG#",
    #         "#.#.#G#",
    #         "#..G#E#",
    #         "#.....#",
    #         "#######"]

    # return ["#######",
    #         "#G..#E#",
    #         "#E#E.E#",
    #         "#G.##.#",
    #         "#...#E#",
    #         "#...E.#",
    #         "#######"]

    # return ["#######",
    #         "#E..EG#",
    #         "#.#G.E#",
    #         "#E.##E#",
    #         "#G..#.#",
    #         "#..E#.#",
    #         "#######"]

    # return ["#######",
    #         "#E.G#.#",
    #         "#.#G..#",
    #         "#G.#.G#",
    #         "#G..#.#",
    #         "#...E.#",
    #         "#######"]

    # return ["#######",
    #         "#.E...#",
    #         "#.#..G#",
    #         "#.###.#",
    #         "#E#G#G#",
    #         "#...#G#",
    #         "#######"]

    return ["#########",
            "#G......#",
            "#.E.#...#",
            "#..##..G#",
            "#...##..#",
            "#...#...#",
            "#.G...G.#",
            "#.....G.#",
            "#########"]

ATTACK_POWER = 19

if __name__ == '__main__':
    print("Starting Day 15-2")
    # Read file into list of values
    values = read_file('input.txt')
    # values = test_data()


    # First we want to translate the starting map into a grid that we can use for computing, so instead of
    # simple characters we will use objects
    class Space:
        def __init__(self):
            pass

        def as_char(self):
            return '.'


    class Wall(Space):
        def __init__(self):
            super().__init__()

        def as_char(self):
            return '#'


    class Elf(Space):
        def __init__(self):
            super().__init__()
            self.hit_points = 200
            self.turns = 0
            self.attack = ATTACK_POWER

        def as_char(self):
            return 'E'

        def is_enemy(self, other):
            return isinstance(other, Goblin)

        def is_ally(self, other):
            return isinstance(other, Elf)


    class Goblin(Space):
        def __init__(self):
            super().__init__()
            self.hit_points = 200
            self.turns = 0
            self.attack = 3

        def as_char(self):
            return 'G'

        def is_enemy(self, other):
            return isinstance(other, Elf)

        def is_ally(self, other):
            return isinstance(other, Goblin)


    # Now translate the map into objects in a grid
    grid = []
    starting_elves = 0
    for val in values:
        row = []
        for char in val:
            if char == '#':
                row.append(Wall())
            elif char == 'E':
                row.append(Elf())
                starting_elves += 1
            elif char == 'G':
                row.append(Goblin())
            else:
                row.append(Space())
        grid.append(row)

    # Debug print out starting map
    for row in grid:
        chars = []
        for cell in row:
            if isinstance(cell, (Elf, Goblin)):
                chars.append(cell)
            print(cell.as_char(), end='')
        print("   {0}".format(','.join([char.as_char() + '(' + str(char.hit_points) + ')' for char in chars])))
    print()


    # Now for the big algorithm to determine what each character on the field does
    # First, check to see if they are next to an enemy already and then attack the weakest one according to
    # the priority rules
    # Second, if no enemies are adjacent, do the pathfinding portion to see if an enemy can be moved to
    # Third, if there is a path, take the quickest one according to the priority rules
    # To make sure each character only takes one turn, a turn tracker will be used on each object since we
    # will not be replacing the whole map each time
    def attempt_attack(current_char, char_point):
        # Check adjacencies for enemies
        x, y = char_point
        point_to_attack = None
        smallest_hp = 999

        points = [
            (x, y - 1),
            (x - 1, y),
            (x + 1, y),
            (x, y + 1)
        ]
        for point in points:
            new_x, new_y = point
            space = grid[new_y][new_x]
            if current_char.is_enemy(space) and (point_to_attack is None or space.hit_points < smallest_hp):
                point_to_attack = (new_x, new_y)
                smallest_hp = space.hit_points

        if point_to_attack:
            # There is an enemy to attack, so do so and move to next character
            enemy = grid[point_to_attack[1]][point_to_attack[0]]
            enemy.hit_points -= current_char.attack
            if enemy.hit_points <= 0:
                grid[point_to_attack[1]][point_to_attack[0]] = Space()
            return True

        return False


    def find_path(current_char, start):
        # For this pathfinding, we are going to use a simple breadth-first search, using a queue to track
        # which spaces and current paths are still valid. A set will be used to determine which spaces
        # have already been visited. A shortest path will keep track of the shortest path to an enemy
        # found so far. Due to the way the paths are created, any valid path should already follow the
        # rules for priority movement.
        shortest_path = None
        closest_space = None
        visited = set()
        queue = deque()

        # Put the start space in the queue to get it going
        queue.append((start[0], start[1], []))
        while len(queue) > 0:
            x, y, path = queue.popleft()
            # Get all points to check
            points = [
                (x, y - 1, 'U'),
                (x - 1, y, 'L'),
                (x + 1, y, 'R'),
                (x, y + 1, 'D')
            ]

            # Go through each point
            for point in points:
                new_x, new_y, dir = point
                # First check to make sure it hasn't been visited already
                if (new_x, new_y) in visited:
                    continue
                else:
                    visited.add((new_x, new_y))

                space = grid[new_y][new_x]
                if current_char.is_enemy(space):
                    # Enemy found, so check to see if it's the shortest path
                    new_path = path.copy()
                    if shortest_path is None or len(new_path) < len(shortest_path):
                        # No existing path or path is shorter
                        shortest_path = new_path
                        closest_space = (x, y)
                    elif len(new_path) == len(shortest_path) and (
                            y < closest_space[1] or (y == closest_space[1] and x < closest_space[0])):
                        # Path has the same length as previous one, but space is higher priority
                        shortest_path = new_path
                        closest_space = (x, y)
                    break
                elif current_char.is_ally(space) or isinstance(space, Wall):
                    # Ally or wall found, cannot move this way so ignore
                    pass
                else:
                    # Space found, so add it to the path and put back on queue
                    new_path = path + [dir]
                    queue.append((new_x, new_y, new_path))

        return shortest_path


    def move(start_point, path_result):
        x, y = start_point
        char_to_move = grid[y][x]
        grid[y][x] = Space()
        if path_result[0] == 'U':
            y -= 1
        elif path_result[0] == 'D':
            y += 1
        elif path_result[0] == 'L':
            x -= 1
        elif path_result[0] == 'R':
            x += 1
        grid[y][x] = char_to_move
        return (x, y)


    turns = 0
    while True:
        turns += 1
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if not isinstance(grid[y][x], (Elf, Goblin)):
                    # Space or wall, so just continue
                    continue

                # Get the current character and check to make sure they didn't take a turn already
                current_char = grid[y][x]
                if current_char.turns >= turns:
                    continue

                # Try to attack if an enemy is adjacent
                if attempt_attack(current_char, (x, y)):
                    current_char.turns += 1
                    continue

                # No enemy adjacent, so we need to find one
                path_result = find_path(current_char, (x, y))
                if path_result:
                    new_x, new_y = move((x, y), path_result)
                    # Now that character has moved, check again for enemies to attack
                    attempt_attack(current_char, (new_x, new_y))

                current_char.turns += 1

        print("Turn {0!s}".format(turns))
        for row in grid:
            chars = []
            for cell in row:
                if isinstance(cell, (Elf, Goblin)):
                    chars.append(cell)
                print(cell.as_char(), end='')
            print("   {0}".format(','.join([char.as_char() + '(' + str(char.hit_points) + ')' for char in chars])))
        print()

        # At the end of the turn, we need to check to see if one side has won or not
        num_elves = 0
        num_goblins = 0
        for row in grid:
            for cell in row:
                if isinstance(cell, Elf):
                    num_elves += 1
                elif isinstance(cell, Goblin):
                    num_goblins += 1

        if num_elves == 0 or num_goblins == 0:
            # Combat has ended
            break

    # Figure out the outcome, which is turns times HP left on remaining characters
    total_hp = 0
    ending_elves = 0
    for row in grid:
        for cell in row:
            if isinstance(cell, Elf):
                ending_elves += 1
            if isinstance(cell, (Elf, Goblin)):
                total_hp += cell.hit_points
    print("The outcome of the battle is: {0!s} or {1!s}".format(total_hp * (turns - 1), total_hp * turns))
    print("The battle started with {0!s} elves and ended with {1!s} at attack power: {2!s}".format(
        starting_elves, ending_elves, ATTACK_POWER))
