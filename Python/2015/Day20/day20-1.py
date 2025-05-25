# Calculate the lowest house number that gets a given number of presents assuming that elves are visiting
# houses in ascending orders

TARGET = 36000000

if __name__ == '__main__':
    print("Starting Day20-1")

    # Iterate through each house, determine which elves visit it, and tally up the presents
    for house in range(831600, 0, -1):
        total_presents = house * 10
        for elf in range(1, int(house / 2) + 1):
            if house % elf == 0:
                total_presents += elf * 10

        #print("House {0!s}: {1!s} presents".format(house, total_presents))

        if total_presents >= TARGET:
            print("House {0!s}: {1!s} presents".format(house, total_presents))
