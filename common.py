def read_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())

    return lines


def answer(a):
    print(f'The answer is: {a!s}')


def run(filename, call):
    answer(call(read_file(filename)))


def check(filename, call, expected):
    result = call(read_file(filename))
    answer(result)
    assert result == expected
