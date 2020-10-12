# Figure out the next ten recipes after a given number of recipes where new recipes are created based on
# existing ones

TARGET_RECIPE = 765071

if __name__ == '__main__':
    print("Starting Day 14-1")

    # Due to the nature of the algorithm involved, it makes the most sense to just use a singly-linked list
    class Node:
        def __init__(self, index, value, next=None):
            self.index = index
            self.value = value
            self.next = next

    # We start with 3 and 7 already defined as the head and tail, and list circles so tail always has head
    # as the next node
    head = Node(1, 3)
    tail = Node(2, 7)
    head.next = tail
    tail.next = head

    # Our end condition is to get the ten recipes following the TARGET, so we want to capture those as
    # soon as they become available
    ten_recipes = []
    first = head
    second = tail
    while len(ten_recipes) < 10:
        # Debug print out the list
        # runner = head
        # while runner != tail:
        #     print(str(runner.value), end='')
        #     runner = runner.next
        # print(str(tail.value))

        # Get the two recipes being looked at by the first and second runners
        first_recipe = first.value
        second_recipe = second.value
        sum = first_recipe + second_recipe

        # If there are two digits, we need to add the tens digit first
        if sum >= 10:
            new_recipe = int(sum / 10)
            new_index = tail.index + 1
            if new_index > TARGET_RECIPE:
                # We are beyond the target, so append this to the end recipes
                ten_recipes.append(new_recipe)
            new_node = Node(new_index, new_recipe, head)
            tail.next = new_node
            tail = new_node
            sum = sum % 10

        # In all cases, add the ones digit as a new recipe
        new_index = tail.index + 1
        if new_index > TARGET_RECIPE:
            # We are beyond the target, so append this to the end recipes
            ten_recipes.append(sum)
        new_node = Node(new_index, sum, head)
        tail.next = new_node
        tail = new_node

        # New recipes are added, so move up each runner
        first_moves = first.value + 1
        for i in range(first_moves):
            first = first.next
        second_moves = second.value + 1
        for i in range(second_moves):
            second = second.next

    # Print out answer
    ten_recipes = ten_recipes[0:10] # Trim in case there's more than ten
    print("The ten recipes are: {0}".format(''.join(map(str, ten_recipes))))
