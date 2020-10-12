# Calculate the appropriate code based on a table of generated values using a given algorithm

TARGET_ROW = 2947 - 1 # Target is given with starting points of 1,1
TARGET_COL = 3029 - 1
GRID_SIZE = TARGET_ROW + TARGET_COL + 2

if __name__ == '__main__':
    print("Starting Day25-1")

    # First, create the table so that it doesn't have to constantly expand
    code_table = [[0]*GRID_SIZE for i in range(GRID_SIZE)]

    # Initialize the first spot
    last_value = 20151125
    code_table[0][0] = last_value

    # Now we construct the table
    for row in range(1, GRID_SIZE):
        for col in range(row + 1):
            last_value = (last_value * 252533) % 33554393
            code_table[row-col][col] = last_value

    # Print out answer
    print("The value at row 2947 and column 3029 is: {0!s}".format(code_table[TARGET_ROW][TARGET_COL]))
