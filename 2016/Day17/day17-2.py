# Determine the longest path through a set of doors by using incrementing MD5 hashes to see which doors are open in each
# room
from collections import deque
import hashlib

# input_key = "ihgpwlah"
# input_key = "kglvqrro"
# input_key = "ulqzkmiv"
input_key = "ioramepc"
valid_chars = ['b','c','d','e','f']


if __name__ == "__main__":
    print("Starting Day 17-2")

    # Define a grid and start at 0,0 within it, we need to get to the opposite corner, or N,N where N is size-1
    # We don't need to create a grid, just the boundaries to make sure we don't go outside it
    grid_size = 4
    position = (0,0)

    # We need to keep track of each possible path to determine the longest at the end
    paths = []

    # Since this is path finding problem, we should have a queue that holds each possible state. State includes the
    # current position and the path used to get there.
    queue = deque()
    queue.append((position, ''))

    def get_hash(path):
        md5 = hashlib.new('md5')
        value = input_key + path
        md5.update(value.encode('utf-8'))
        return md5.hexdigest()

    # Now start finding paths
    while len(queue) > 0:
        position,path = queue.popleft()
        if position == (grid_size - 1, grid_size - 1):
            # We have reached the vault, so add path to list of paths
            paths.append(path)
            continue

        # First, get the MD5 hash for the current room
        hash = get_hash(path)

        # Second, determine which doors are valid
        # Try up
        if hash[0] in valid_chars and position[1] > 0:
            # We can go up, so add it to the queue
            new_position = (position[0], position[1] - 1)
            queue.append((new_position, path + 'U'))

        # Try down
        if hash[1] in valid_chars and position[1] < grid_size - 1:
            # We can go down, so add it to the queue
            new_position = (position[0], position[1] + 1)
            queue.append((new_position, path + 'D'))

        # Try left
        if hash[2] in valid_chars and position[0] > 0:
            # We can go left, so add it to the queue
            new_position = (position[0] - 1, position[1])
            queue.append((new_position, path + 'L'))

        # Try right
        if hash[3] in valid_chars and position[0] < grid_size - 1:
            # We can go right, so add it to the queue
            new_position = (position[0] + 1, position[1])
            queue.append((new_position, path + 'R'))

    # Now we are out of paths to find, determine the longest one
    longest_path = paths[0]
    for path in paths:
        if len(path) > len(longest_path):
            longest_path = path

    print("The longest path to the vault is: {0!s} steps long".format(len(longest_path)))
