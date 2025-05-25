# Determine the number of Conway cubes there are after some iterations of an algo in 3D space

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return [".#.",
            "..#",
            "###"]


print("Starting Day17-1")
values = read_file("input.txt")
# values = test_data()

# Here we have another problem where we change spaces in a grid based on adjacent spaces, but this time it's in 3
# dimensions so everything is tripled. Instead of 8 checks we make 26 per space.
# Because we start at 0,0,0 and the algo expands out, we will want to use coordinates in a map instead of an array
cube_map = dict()

# To start, parse the input into the z=0 grid, we are only going to store coordinates with a cube to make calcs easier
for y, val in enumerate(values):
    for x, space in enumerate(val):
        if space == '#':
            cube_map[(x, y, 0)] = '#'


# Define our helper functions here
def is_active_cube(check_map, x, y, z):
    return (x, y, z) in check_map


def check_cube(check_map, x, y, z):
    active = 0
    for check_x in range(x - 1, x + 2):
        for check_y in range(y - 1, y + 2):
            for check_z in range(z - 1, z + 2):
                if (x, y, z) != (check_x, check_y, check_z) and is_active_cube(check_map, check_x, check_y, check_z):
                    active += 1
    return active


# Now we execute the algo for a number of cycles
cycles = 6
for cycle in range(cycles):
    print("The number of active cubes after {0!s} cycles is: {1!s}".format(cycle, len(cube_map)))
    print(cube_map)
    # First thing we want to do is get the min/max for each axis so we can determine what we need to loop over
    min_x, max_x, min_y, max_y, min_z, max_z = 999, -999, 999, -999, 999, -999
    for coord in cube_map.keys():
        min_x = min(min_x, coord[0])
        max_x = max(max_x, coord[0])
        min_y = min(min_y, coord[1])
        max_y = max(max_y, coord[1])
        min_z = min(min_z, coord[2])
        max_z = max(max_z, coord[2])
    print(min_x, max_x, min_y, max_y, min_z, max_z)

    # Now we do our loop through the 3D space, checking to see if the coordinate should change its cube status
    new_map = dict()
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                active_adjacencies = check_cube(cube_map, x, y, z)
                # print("Space {0!s}, {1!s}, {2!s} has {3!s} active adjacencies".format(x, y, z, active_adjacencies))
                if is_active_cube(cube_map, x, y, z):
                    if 2 <= active_adjacencies <= 3:
                        # Active cube stays active
                        new_map[(x, y, z)] = '#'
                else:
                    if active_adjacencies == 3:
                        # Inactive cube becomes active
                        new_map[(x, y, z)] = '#'
    cube_map = new_map

print(cube_map)
print("The number of active cubes after {0!s} cycles is: {1!s}".format(cycles, len(cube_map)))
