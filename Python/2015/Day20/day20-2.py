# Calculate the lowest house number that gets a given number of presents assuming that elves are visiting
# houses in ascending orders
# Second part: each elf only visits the first 50 houses but leaves more presents

TARGET = 36000000

if __name__ == '__main__':
    print("Starting Day20-2")

    # Iterate through each house, determine which elves visit it, and tally up the presents
    for house in range(1000080, 100000, -2):
        total_presents = house * 11
        for elf in range(1, int(house / 2) + 1):
            if house % elf == 0 and int(house / elf) <= 50:
                total_presents += elf * 11

        #print("House {0!s:>2}: {1!s}".format(house, total_presents))

        if total_presents >= TARGET:
            print("House {0!s}: {1!s} presents".format(house, total_presents))
