# Determine the best ratio of ingredients to make the highest scoring cookie

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
            "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"]

class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)

if __name__ == '__main__':
    print("Starting Day15-1")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # First, create a list of ingredient objects that holds their stats
    ingredient_list = []
    for val in values:
        items = val.replace(':','').replace(',','').split()
        ingredient_list.append(Ingredient(items[0], items[2], items[4], items[6], items[8], items[10]))

    # Print out ingredients
    for ingredient in ingredient_list:
        print("{0}: capacity {1}, durability {2}, flavor {3}, texture {4}, calories {5}"
              .format(ingredient.name, str(ingredient.capacity), str(ingredient.durability), str(ingredient.flavor),
                      str(ingredient.texture), str(ingredient.calories)))

    # Create tracker for current amount of each ingredient
    amounts = [int(100/len(ingredient_list))]*len(ingredient_list)

    # Calculate scores and shift amounts until maximum is reached
    def calculate_score():
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        for index in range(len(amounts)):
            amount = amounts[index]
            ingredient = ingredient_list[index]
            capacity += amount * ingredient.capacity
            durability += amount * ingredient.durability
            flavor += amount * ingredient.flavor
            texture += amount * ingredient.texture

        if capacity < 0:
            capacity = 0
        if durability < 0:
            durability = 0
        if flavor < 0:
            flavor = 0
        if texture < 0:
            texture = 0

        total = capacity * durability * flavor * texture
        print("{0}: {1}".format(','.join(map(str, amounts)), str(total)))

        return total

    highest = calculate_score()
    had_change = True
    count = 0
    while had_change:
        count += 1
        had_change = False
        for i in range(len(amounts)):
            for j in range(len(amounts)):
                if i == j:
                    continue
                go_up = True
                while go_up:
                    amounts[j] -= 1
                    amounts[i] += 1
                    current = calculate_score()
                    if current >= highest:
                        highest = current
                        had_change = True
                    else:
                        amounts[j] += 1
                        amounts[i] -= 1
                        go_up = False
                go_down = True
                while go_down:
                    amounts[i] -= 1
                    amounts[j] += 1
                    current = calculate_score()
                    if current >= highest:
                        highest = current
                        had_change = True
                    else:
                        amounts[i] += 1
                        amounts[j] -= 1
                        go_down = False


    # Print out answer
    print("The highest score is: {0}".format(str(highest)))
    print("Number of loops: {0}".format(str(count)))