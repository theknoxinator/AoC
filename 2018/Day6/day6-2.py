# Determine a region where the total distance from it to each given point is less than a given value when
# summed up

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["1, 1",
            "1, 6",
            "8, 3",
            "3, 4",
            "5, 5",
            "8, 9"]

if __name__ == '__main__':
    print("Starting Day6-2")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # First, compile values into list of coordinates
    coordinates = []
    for val in values:
        items = val.replace(',','').split()
        x = int(items[0])
        y = int(items[1])
        coordinates.append((x,y))

    # Debug print out coordinates
    for coordinate in coordinates:
        print("({0},{1})".format(coordinate[0], coordinate[1]))

    # Create a grid and iterate through each cell, finding the closest coordinate to it and filling it in
    grid_size = 400
    grid = [['']*grid_size for i in range(grid_size)]
    for grid_y in range(grid_size):
        for grid_x in range(grid_size):
            total_distance = 0
            for index in range(len(coordinates)):
                coordinate = coordinates[index]
                distance = abs(grid_x - coordinate[0]) + abs(grid_y - coordinate[1])
                total_distance += distance

            if total_distance < 10000:
                grid[grid_y][grid_x] = '#'
            else:
                grid[grid_y][grid_x] = '.'

    # Debug print out grid
    for row in grid:
        print("{0}".format(''.join(map(str, row))))

    '''
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

    # Debug print out area sizes and infinite coords
    for key,value in area_sizes.items():
        print("{0} has area: {1}".format(str(key), str(value)))
    print("Coords with no bounds: [{0}]".format(','.join(map(str, infinite_coords))))
    '''

    # Print out answer
    total_area = 0
    for row in grid:
        for cell in row:
            if cell == '#':
                total_area += 1
    print("The area is: {0!s}".format(total_area))