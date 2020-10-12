# Determine which reindeer has flown the furthest after an amount of time

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
            "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."]

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

if __name__ == '__main__':
    print("Starting Day14-1")
    # Read file into list of descriptions
    values = read_file('input.txt')
    #values = test_data()

    # First, create a list of reindeer objects that holds their stats and current status
    reindeer_list = []
    for val in values:
        items = val.split()
        reindeer_list.append(Reindeer(items[0], int(items[3]), int(items[6]), int(items[13])))

    # Print out reindeer
    for reindeer in reindeer_list:
        print("{0}: fly speed - {1}, max fly - {2}, max rest - {3}".format(reindeer.name, str(reindeer.fly_speed),
                                                                           str(reindeer.max_fly), str(reindeer.max_rest)))

    # Create tracker for current distances of each reindeer
    distance = {}
    for reindeer in reindeer_list:
        distance[reindeer.name] = 0

    # Now go through each second and tally up the flight and rest
    for _ in range(2503):
        for reindeer in reindeer_list:
            if reindeer.is_resting():
                reindeer.rest()
            elif reindeer.is_flying():
                distance[reindeer.name] += reindeer.fly()

    # Print out answer
    for key,value in distance.items():
        print("{0} went {1} km".format(key, str(value)))