# Parse bulk file of passport info and determine valid passports

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
            "byr:1937 iyr:2017 cid:147 hgt:183cm",
            "",
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
            "hcl:#cfa07d byr:1929",
            "",
            "hcl:#ae17e1 iyr:2013",
            "eyr:2024",
            "ecl:brn pid:760753108 byr:1931",
            "hgt:179cm",
            "",
            "hcl:#cfa07d eyr:2025 pid:166559648",
            "iyr:2011 ecl:brn hgt:59in"]


print("Starting Day4-1")
values = read_file("input.txt")
# values = test_data()

# We are going to parse the passports and determine their validity in place, so we know that it's the end of the current
# passport when we see an empty line
values.append("")
valid_passports = 0
current_passport = {}
for line in values:
    if len(line) < 1:
        # We have reached an empty line, so compute current passport
        is_valid = True
        for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if key not in current_passport:
                is_valid = False
                break
        if is_valid:
            valid_passports += 1
        else:
            print("Not a valid passport: ", sorted(current_passport))
        current_passport = {}
    else:
        # Split current line into key-value pairs and add them to passport
        pairs = line.split(' ')
        for pair in pairs:
            key, value = pair.split(':')
            current_passport[key] = value

print("The number of valid passports is: {0!s}".format(valid_passports))
