# Determine the shortest route such that all locations gets visited once
import sys

def parse_distance(distance):
    return distance.split()


def generate_routes(values):
    locations = []
    distances = {}
    for distance in values:
        parts = parse_distance(distance)
        if parts[0] not in locations:
            locations.append(parts[0])
        if parts[2] not in locations:
            locations.append(parts[2])
        distances[(parts[0], parts[2])] = int(parts[4])

    # Print out distances
    # for key, value in distances.items():
    #     print("{0} -> {1}: {2}".format(key[0], key[1], str(value)))

    # Compile all the different possible route permutations
    routes = []
    for location in locations:
        if len(routes) == 0:
            # First case
            routes.append([location])
            continue
        new_routes = []
        for route in routes:
            for index in range(len(route) + 1):
                new_route = route.copy()
                new_route.insert(index, location)
                new_routes.append(new_route)

        routes = new_routes

    # Print out routes
    # for route in routes:
    #    print(" -> ".join(route))
    print("Total number of routes: {0}".format(str(len(routes))))

    return locations, distances, routes


def part1(values):
    # Compile the distances as start,end tuples within a dictionary for easy lookup
    locations, distances, routes = generate_routes(values)

    # Calculate the shortest distance
    shortest = sys.maxsize
    shortest_route = []

    def calc_route(route):
        distance = 0
        for index in range(len(route) - 1):
            if (route[index], route[index + 1]) in distances:
                distance += distances[(route[index], route[index + 1])]
            elif (route[index + 1], route[index]) in distances:
                distance += distances[(route[index + 1], route[index])]
            else:
                return 0
        return distance

    count = 0
    valid_routes = 0
    for route in routes:
        count += 1
        route_length = calc_route(route)
        if route_length == 0:
            continue
        valid_routes += 1
        if route_length < shortest:
            shortest = route_length
            shortest_route = route

    print("The shortest route is {0}, which is {1}".format(" -> ".join(shortest_route), str(shortest)))
    return shortest


def part2(values):
    # Compile the distances as start,end tuples within a dictionary for easy lookup
    locations, distances, routes = generate_routes(values)

    # Calculate the longest distance
    longest = 0
    longest_route = []

    def calc_route(route):
        distance = 0
        for index in range(len(route) - 1):
            if (route[index], route[index + 1]) in distances:
                distance += distances[(route[index], route[index + 1])]
            elif (route[index + 1], route[index]) in distances:
                distance += distances[(route[index + 1], route[index])]
            else:
                return 0
        return distance

    count = 0
    valid_routes = 0
    for route in routes:
        count += 1
        route_length = calc_route(route)
        if route_length == 0:
            continue
        valid_routes += 1
        if route_length > longest:
            longest = route_length
            longest_route = route

    print("The longest route is {0}, which is {1}".format(" -> ".join(longest_route), str(longest)))
    return longest
