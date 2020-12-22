# DO SOME MATHS

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    # return ["1 + 2 * 3 + 4 * 5 + 6"]
    # return ["1 + (2 * 3) + (4 * (5 + 6))"]
    # return ["2 * 3 + (4 * 5)"]
    # return ["5 + (8 * 3 + 9 + 3 * 4 * 3)"]
    # return ["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"]
    return ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]


print("Starting Day18-1")
values = read_file("input.txt")
# values = test_data()


# Looks like we get to do some expression parsing
class ExprParser:
    def __init__(self, start_expr):
        self.start_expr = start_expr

    def calc(self):
        return self.parse_expr(self.start_expr)

    def parse_expr(self, expression):
        print(expression)
        left_paren, right_paren, index = 0, 0, 0
        while index < len(expression):
            if expression[index] == '(':
                left_paren = index
            elif expression[index] == ')':
                right_paren = index
                break
            index += 1
        if left_paren < right_paren:
            expression = expression[:left_paren] + self.calc_expr(expression[left_paren + 1:right_paren]) + \
                         expression[right_paren + 1:]
            return self.parse_expr(expression)
        else:
            return self.calc_expr(expression)

    def calc_expr(self, expression):
        left, remainder = self.parse_number(expression)
        if not remainder:
            return left
        operator = remainder[0]
        right, remainder = self.parse_number(remainder[1:])
        value = 0
        if operator == '+':
            value = int(left) + int(right)
        elif operator == '*':
            value = int(left) * int(right)
        return self.calc_expr(str(value) + remainder)

    def parse_number(self, expression):
        index = 0
        while index < len(expression) and expression[index] in "0123456789":
            index += 1
        return expression[:index], expression[index:]


sum_of_all = 0
for val in values:
    start_expr = val.replace(' ', '')
    parser = ExprParser(start_expr)
    sum_of_all += int(parser.calc())

print("The sum of all values is: {0!s}".format(sum_of_all))
