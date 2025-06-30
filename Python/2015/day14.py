# Determine which reindeer has flown the furthest after an amount of time

class Reindeer:
    def __init__(self, name, fly_speed, max_fly, max_rest):
        self.name = name
        self.fly_speed = fly_speed
        self.max_fly = max_fly
        self.max_rest = max_rest
        self.fly_cycle = self.max_fly
        self.rest_cycle = 0

    def is_resting(self):
        return self.rest_cycle > 0

    def rest(self):
        self.rest_cycle -= 1
        if self.rest_cycle == 0:
            self.fly_cycle = self.max_fly

    def is_flying(self):
        return self.fly_cycle > 0

    def fly(self):
        self.fly_cycle -= 1
        if self.fly_cycle == 0:
            self.rest_cycle = self.max_rest
        return self.fly_speed


def calc_distance(values):
    # First, create a list of reindeer objects that holds their stats and current status
    reindeer_list = []
    for val in values:
        items = val.split()
        reindeer_list.append(Reindeer(items[0], int(items[3]), int(items[6]), int(items[13])))

    # Create tracker for current distances of each reindeer
    distance = {}
    points = {}
    for reindeer in reindeer_list:
        distance[reindeer.name] = 0
        points[reindeer.name] = 0

    # Now go through each second and tally up the flight and rest
    for _ in range(2503):
        for reindeer in reindeer_list:
            if reindeer.is_resting():
                reindeer.rest()
            elif reindeer.is_flying():
                distance[reindeer.name] += reindeer.fly()

        leader = ""
        farthest = 0
        for key,value in distance.items():
            if value > farthest:
                farthest = value
                leader = key
        points[leader] += 1

    return max(distance.values()), max(points.values())


def part1(values):
    return calc_distance(values)[0]


def part2(values):
    return calc_distance(values)[1]
