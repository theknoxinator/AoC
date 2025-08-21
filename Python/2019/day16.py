# Part 1: Given an input, execute the FFT algorithm on it 100 times
# Part 2: Do the same thing but the input is now 10,000 times longer and the output is slightly different

def run_fft_algo(values, use_part2=False):
    # Read in the signal as just a string, we will break this into pieces later
    signal = values[0]

    # This problem feels very much like matrix math to me, but I don't remember much about stuff I did 20 years ago so
    # we will approach this from a different angle
    # Based on the way the sequence of multiplication works, we know that the start position of every row is also the
    # col, so [0,0], [1,1], [2,2], etc. Then we will get (row + 1) copies of 1, (row + 1) copies of 0, (row + 1) copies
    # of -1, and so on until the end of the row. Since this effectively makes half the signal matrix useless, we won't
    # worry about storing the full matrix and only store the summed result of each row
    multipliers = [0, 1, 0, -1]
    for loop in range(100):
        int_list_signal = list(map(int, list(signal)))
        row_sums = []
        for row in range(len(signal)):
            repeat = row + 1
            current_count = repeat
            current_multiplier = 1
            current_sum = 0
            for col in range(row, len(signal)):
                current_sum += (int_list_signal[col] * multipliers[current_multiplier])
                current_count -= 1
                if current_count == 0:
                    current_multiplier = (current_multiplier + 1) % 4
                    current_count = repeat
            row_sums.append(str(abs(current_sum) % 10))

        # Once all the rows are done, combine the digits into a new signal
        signal = ''.join(row_sums)

    # After 100 loops, output the result, which is just the first 8 digits
    return signal[:8]


def run_fft_algo2(values):
    # Read in the signal as a string and multiply it out 10,000 times
    signal = values[0] * 10000

    # Knowing that a brute force wouldn't work with a 6.5 million digit signal, I couldn't come up with a way to do it
    # so ended up looking it up again (this year is kicking my butt). Working off what I said before where half of the
    # signal matrix is useless, it is also true that for the entire second half of the signal, none of the numbers are
    # multiplied by 0 or -1, so it's just pure sums where the sum is getting smaller and smaller every row by one digit
    # So this version takes advantage of that by taking the sum of the row starting at the offset and subtracting the
    # digit missing from the next row until the end
    # Since this part of the signal is isolated, we also don't care about everything before the offset either, which
    # speeds things up a lot too
    offset = int(signal[0:7])
    signal = signal[offset:]
    for loop in range(100):
        row_sums = []
        col = 0
        total = 0
        while col < len(signal):
            if col == 0:
                # For the first row, we just sum up all digits
                for digit in signal:
                    total += int(digit)
            else:
                # For all other rows, subtract the digit right before the col
                total -= int(signal[col - 1])
            # Append just the last digit of the current sum
            row_sums.append(str(total)[-1])
            col += 1
        signal = ''.join(row_sums)

    # After 100 loops, output the result, which is the first 8 digits of the offset signal
    return signal[:8]


def part1(values):
    return run_fft_algo(values)


def part2(values):
    return run_fft_algo2(values)
