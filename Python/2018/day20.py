# Part 1: Using a long regex expression of possible paths in a maze, determine the longest path without repeating rooms
# Part 2: With same regex expression, find all rooms that take at least 1000 steps to get to

class RegexParser:
    def __init__(self, start_regex):
        self.start_regex = start_regex

    def get_longest(self):
        return self._parse_regex(self.start_regex)

    def _parse_regex(self, regex):
        index = 0
        left_parens = []
        # Use a forever loop here since the size of the regex expression will constantly be in flux, we just exit once
        # index has exceeded the final length
        while True:
            if regex[index] == '(':
                left_parens.append(index)
                index += 1
            elif regex[index] == ')':
                left, right = left_parens.pop(), index
                regex = regex[:left] + self._get_longest_option(regex[left + 1:right]) + regex[right + 1:]
                # Move index back to the beginning of the new section
                index = left
            else:
                index += 1

            if index >= len(regex):
                return regex

    def _get_longest_option(self, regex):
        options = regex.split('|')
        longest = options[0]
        for option in options:
            if len(option) > len(longest) or len(option) == 0:
                longest = option
        return longest


def find_longest_path(values):
    # Get regex and trim off the first and last chars
    regex = values[0][1:-1]

    # Parse the regex and get the longest possible option
    parser = RegexParser(regex)
    result = parser.get_longest()

    return len(result)


def find_far_rooms(values):
    # I tried for a long while to come up with a way to use a tree or something to find paths, but eventually gave up
    # and searched for help. Graph theory is a weak part of my knowledge so this is based on other solutions using that.
    regex = values[0][1:-1]
    target_distance = 10 if len(regex) < 100 else 1000

    # This algorithm uses a stack of positions where the path branches, so that once we hit a pipe or right paren we can
    # pop back to the previous position. I had this idea for my tree solution but this is just easier to do.
    directions = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
    positions = []
    x, y = 0, 0
    prev_x, prev_y = x, y
    distances = dict()
    distances[(x, y)] = 0
    for val in regex:
        if val == '(':
            # Starting a branch, so add to positions
            positions.append((x, y))
        elif val == ')':
            # Done branching in this subpath, go back to start of branch and remove from stack
            x, y = positions.pop()
        elif val == '|':
            # Subpath is done but still more branches to check, go back to start but do not remove from stack yet
            x, y = positions[-1]
        else:
            # Otherwise we are moving in a direction, get the offset and add it to the current x, y
            dx, dy = directions[val]
            x += dx
            y += dy
            if (x, y) in distances:
                distances[(x, y)] = min(distances[(x, y)], distances[(prev_x, prev_y)] + 1)
            else:
                distances[(x, y)] = distances[(prev_x, prev_y)] + 1

        prev_x, prev_y = x, y

    # Now tally up all the rooms in distances map that have a distance of 1000 or higher
    return len([x for x in distances.values() if x >= target_distance])


def part1(values):
    return find_longest_path(values)


def part2(values):
    return find_far_rooms(values)
