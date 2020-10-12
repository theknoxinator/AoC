# Determine how many lights are on for a 100x100 grid based on a starting state and lights are turned
# on or off after each step based on its state and its neighbors states

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return [".#.#.#",
            "...##.",
            "#....#",
            "..#...",
            "#.#..#",
            "####.."]

if __name__ == '__main__':
    print("Starting Day18-1")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Convert the values into a 2D array grid
    grid = []
    grid_size = len(values)
    for val in values:
        grid.append(list(val))

    #for row in grid:
    #    print(''.join(row))
    #print()

    # Make a helper to getting the number of neighbors that are on
    def get_neighbors(x, y):
        coords = []
        coords.append((x - 1, y))
        coords.append((x - 1, y - 1))
        coords.append((x - 1, y + 1))
        coords.append((x, y - 1))
        coords.append((x, y + 1))
        coords.append((x + 1, y))
        coords.append((x + 1, y - 1))
        coords.append((x + 1, y + 1))

        neighbors_on = 0
        for coord in coords:
            n_x = coord[0]
            n_y = coord[1]
            if n_x < 0 or n_x >= grid_size or n_y < 0 or n_y >= grid_size:
                continue
            if grid[n_y][n_x] == '#':
                neighbors_on += 1

        return neighbors_on

    # Iterate through the grid and determine which lights need to be changed, which is put into a new
    # grid to overwrite the old one
    for loop in range(100):
        new_grid = [['']*grid_size for i in range(grid_size)]
        for y in range(grid_size):
            for x in range(grid_size):
                neighbors_on = get_neighbors(x, y)
                if grid[y][x] == '#':
                    if neighbors_on == 2 or neighbors_on == 3:
                        new_grid[y][x] = '#'
                    else:
                        new_grid[y][x] = '.'
                else:
                    if neighbors_on == 3:
                        new_grid[y][x] = '#'
                    else:
                        new_grid[y][x] = '.'
        grid = new_grid

        #for row in grid:
        #    print(''.join(row))
        #print()

    # Print out answer
    total_on = 0
    for row in grid:
        for cell in row:
            if cell == '#':
                total_on += 1

    print("The number of lights on is: {0}".format(str(total_on)))
