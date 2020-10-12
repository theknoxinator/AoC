# Sum up all the numbers found in the given JSON document
import json

def read_file(filename):
    with open(filename, 'r') as f:
        return json.loads(f.readline())

def test_data():
    #return '[1,2,3]'
    #return '{"a":2,"b":4}'
    #return '[[[3]]]'
    #return '{"a":{"b":4},"c":-1}'
    #return '{"a":[-1,1]}'
    #return '[-1,{"a":1}]'
    #return '[]'
    return '{}'

if __name__ == '__main__':
    print("Starting Day12-1")
    # Read file into value
    json = read_file('input.txt')
    #json = json.loads(test_data())

    # Find all the numbers in the document
    def recurse_json(json_part):
        subtotal = 0
        if isinstance(json_part, int):
            print(str(json_part))
            subtotal += json_part
        elif isinstance(json_part, str):
            pass
        elif isinstance(json_part, list):
            for value in json_part:
                subtotal += recurse_json(value)
        elif isinstance(json_part, dict):
            for value in json_part.values():
                subtotal += recurse_json(value)
        return subtotal

    total = recurse_json(json)

    # Print out answer
    print("The sum of all numbers in the JSON doc is: {0}".format(str(total)))