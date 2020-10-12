# Determine the shortest route such that all locations gets visited once
import sys

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.split())

    return values

def test_data():
    return [["London","to","Dublin","=","464"],
            ["London","to","Belfast","=","518"],
            ["Dublin","to","Belfast","=","141"]]

if __name__ == '__main__':
    print("Starting Day9-1")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Compile the distances as start,end tuples within a dictionary for easy lookup
    locations = []
    distances = {}
    for val in values:
        if val[0] not in locations:
            locations.append(val[0])
        if val[2] not in locations:
            locations.append(val[2])
        distances[(val[0], val[2])] = int(val[4])

    # Print out distances
    for key,value in distances.items():
        print("{0} -> {1}: {2}".format(key[0], key[1], str(value)))

    # Compile all the different possible route permutations
    routes = []
    for location in locations:
        if len(routes) == 0:
            # First case
            routes.append([location])
            continue
        new_routes = []
        for route in routes:
            for index in range(len(route)+1):
                new_route = route.copy()
                new_route.insert(index, location)
                new_routes.append(new_route)

        routes = new_routes

    # Print out routes
    #for route in routes:
    #    print(" -> ".join(route))
    print("Total number of routes: {0}".format(str(len(routes))))

    # Calculate the shortest distance
    shortest = sys.maxsize
    shortest_route = []
    def calc_route(route):
        distance = 0
        for index in range(len(route)-1):
            if (route[index], route[index+1]) in distances:
                distance += distances[(route[index], route[index+1])]
            elif (route[index+1], route[index]) in distances:
                distance += distances[(route[index+1], route[index])]
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
    print("Number of routes calculated: {0}".format(str(count)))
    print("Number of valid routes: {0}".format(str(valid_routes)))

    # Print out answer
    print("The shortest route is {0}, which is {1}".format(" -> ".join(shortest_route), str(shortest)))
