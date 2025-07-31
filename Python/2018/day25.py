# Part 1: Given a large set of stars in 4D space, determine how many constellations can be formed based on proximity
# Part 2: FREE STAR
from collections import defaultdict, deque


def make_constellations(values):
    # First get the star coordinates and put them into a map that we'll use for storing which constellation they are in
    star_map = dict()
    for val in values:
        coordinate = tuple(map(int, val.split(',')))
        star_map[coordinate] = 0

    # I'm sure there is a better algorithm for this for people who have done a lot of graph theory and such, but my
    # approach is going to be to just find all the edges between stars (where Manhattan distance is 3 or shorter),
    # which is just a double loop to figure out. After we have all the edges, we can use a queue with the edge map
    # to assign constellation numbers to each grouping.
    edge_map = defaultdict(set)
    star_list = list(star_map.keys())
    for i in range(len(star_list)):
        for j in range(i + 1, len(star_list)):
            distance = sum(abs(star_list[i][k] - star_list[j][k]) for k in [0, 1, 2, 3])
            if distance <= 3:
                edge_map[star_list[i]].add(star_list[j])
                edge_map[star_list[j]].add(star_list[i])

    queue = deque()
    c_id = 1
    # Now iterate through each star and process it and its neighbors until all stars have a constellation assigned
    for star in star_list:
        # Skip if the star already has a constellation assigned
        if star_map[star] > 0:
            continue
        queue.append(star)
        while queue:
            s1 = queue.popleft()
            if star_map[s1] > 0:
                continue
            star_map[s1] = c_id
            for s2 in edge_map[s1]:
                queue.append(s2)
        c_id += 1

    # With all stars assigned, the highest constellation ID should be the number of total constellations
    return max(star_map.values())


def part1(values):
    return make_constellations(values)
