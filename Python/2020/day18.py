# DO SOME MATHS

# Looks like we get to do some expression parsing
class ExprParser:
    def __init__(self, start_expr, swap=False):
        self.start_expr = start_expr
        self.swap = swap

    def calc(self):
        return self.parse_expr(self.start_expr)

    def parse_expr(self, expression):
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
        if operator == '+':
            value = int(left) + int(right)
            return self.calc_expr(str(value) + remainder)
        elif operator == '*':
            if self.swap:
                value = int(left) * int(self.calc_expr(right + remainder))
                return str(value)
            else:
                value = int(left) * int(right)
                return self.calc_expr(str(value) + remainder)

    def parse_number(self, expression):
        index = 0
        while index < len(expression) and expression[index] in "0123456789":
            index += 1
        return expression[:index], expression[index:]


def calculate_patterns(values, use_part2=False):
    sum_of_all = 0
    for val in values:
        start_expr = val.replace(' ', '')
        parser = ExprParser(start_expr, use_part2)
        sum_of_all += int(parser.calc())

    return sum_of_all


def part1(values):
    return calculate_patterns(values)


def part2(values):
    return calculate_patterns(values, True)
