# Determine which point has the largest surrounding area that is closest to that point and no other points
# Areas that stretch out infinitely do not count

def find_point(values):
    # First, compile values into list of coordinates
    coordinates = []
    for val in values:
        items = val.replace(',','').split()
        x = int(items[0])
        y = int(items[1])
        coordinates.append((x,y))

    # Create a grid and iterate through each cell, finding the closest coordinate to it and filling it in
    grid_size = 400
    grid = [['']*grid_size for i in range(grid_size)]
    for grid_y in range(grid_size):
        for grid_x in range(grid_size):
            shortest_dist = 99999
            shortest_coords = []
            for index in range(len(coordinates)):
                coordinate = coordinates[index]
                distance = abs(grid_x - coordinate[0]) + abs(grid_y - coordinate[1])
                if distance == shortest_dist:
                    shortest_coords.append(index)
                elif distance < shortest_dist:
                    shortest_dist = distance
                    shortest_coords = [index]

            if len(shortest_coords) > 1:
                grid[grid_y][grid_x] = '.'
            else:
                grid[grid_y][grid_x] = shortest_coords[0]

    # Determine which coordinates are infinitely spreading and count the size of each area
    area_sizes = {}
    infinite_coords = set()
    for grid_y in range(grid_size):
        for grid_x in range(grid_size):
            coordinate_index = grid[grid_y][grid_x]
            if coordinate_index == '.':
                continue
            coordinate = coordinates[coordinate_index]
            if coordinate not in area_sizes:
                area_sizes[coordinate] = 1
            else:
                area_sizes[coordinate] += 1
            if (grid_x == 0 or grid_x == grid_size - 1) or (grid_y == 0 or grid_y == grid_size - 1):
                infinite_coords.add(coordinate)

    # Print out answer
    largest_area = 0
    for key,value in area_sizes.items():
        if key not in infinite_coords:
            if value > largest_area:
                largest_area = value
    return largest_area


def find_area(values):
    max_distance = 10000
    if len(values) < 10:
        max_distance = 32

    # First, compile values into list of coordinates
    coordinates = []
    for val in values:
        items = val.replace(',', '').split()
        x = int(items[0])
        y = int(items[1])
        coordinates.append((x, y))

    # Create a grid and iterate through each cell, finding the closest coordinate to it and filling it in
    grid_size = 400
    grid = [[''] * grid_size for i in range(grid_size)]
    for grid_y in range(grid_size):
        for grid_x in range(grid_size):
            total_distance = 0
            for index in range(len(coordinates)):
                coordinate = coordinates[index]
                distance = abs(grid_x - coordinate[0]) + abs(grid_y - coordinate[1])
                total_distance += distance

            if total_distance < max_distance:
                grid[grid_y][grid_x] = '#'
            else:
                grid[grid_y][grid_x] = '.'

    # Print out answer
    total_area = 0
    for row in grid:
        for cell in row:
            if cell == '#':
                total_area += 1
    return total_area


def part1(values):
    return find_point(values)


def part2(values):
    return find_area(values)
