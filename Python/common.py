def read_file(filename, strip_file=True):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            if strip_file:
                lines.append(line.strip())
            else:
                lines.append(line)

    return lines


def answer(a):
    print(f'The answer is: {a!s}')


def run(filename, call, strip_file=True):
    answer(call(read_file(filename, strip_file)))


def check(filename, call, expected, strip_file=True):
    result = call(read_file(filename, strip_file))
    answer(result)
    assert result == expected
