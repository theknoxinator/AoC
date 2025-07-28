# Part 1: Using a pair of number generators, determine how many times they share the same lowest 16 bits
# Part 2: Using the same generators but with additional rules for valid output, do the same determinations

def generate_num(start, mult, mod_factor, mod_requirement=1):
    result = start
    while True:
        result = (result * mult) % mod_factor
        if result % mod_requirement == 0:
            return result


def generate_numbers(values, use_part2=False):
    # Starting values and constants
    gen_a = int(values[0])
    gen_b = int(values[1])
    mult_a = 16807
    mult_b = 48271
    mod_factor = 2147483647

    count = 0
    if not use_part2:
        # Iterate each generator 40 million times and compare the 16 bits
        for _ in range(40_000_000):
            gen_a = generate_num(gen_a, mult_a, mod_factor)
            gen_b = generate_num(gen_b, mult_b, mod_factor)

            if gen_a & 0xffff == gen_b & 0xffff:
                count += 1
    else:
        # Iterate each generator until we get 5 million valid pairs and compare the 16 bits
        for _ in range(5_000_000):
            gen_a = generate_num(gen_a, mult_a, mod_factor, 4)
            gen_b = generate_num(gen_b, mult_b, mod_factor, 8)

            if gen_a & 0xffff == gen_b & 0xffff:
                count += 1

    return count


def part1(values):
    return generate_numbers(values)


def part2(values):
    return generate_numbers(values, True)
