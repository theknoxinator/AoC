# Parse bulk file of passport info and determine valid passports
import re

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    # return ["eyr:1972 cid:100",
    #         "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
    #         "",
    #         "iyr:2019",
    #         "hcl:#602927 eyr:1967 hgt:170cm",
    #         "ecl:grn pid:012533040 byr:1946",
    #         "",
    #         "hcl:dab227 iyr:2012",
    #         "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
    #         "",
    #         "hgt:59cm ecl:zzz",
    #         "eyr:2038 hcl:74454a iyr:2023",
    #         "pid:3556412378 byr:2007"]
    #
    return ["pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
            "hcl:#623a2f",
            "",
            "eyr:2029 ecl:blu cid:129 byr:1989",
            "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
            "",
            "hcl:#888785",
            "hgt:164cm byr:2001 iyr:2015 cid:88",
            "pid:545766238 ecl:hzl",
            "eyr:2022",
            "",
            "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"]


print("Starting Day4-2")
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
        print(current_passport)
        for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if key not in current_passport:
                is_valid = False
                break
            else:
                value = current_passport[key]
                if key == "byr":
                    birth_year = int(value)
                    if birth_year < 1920 or birth_year > 2002:
                        is_valid = False
                        break
                elif key == "iyr":
                    issue_year = int(value)
                    if issue_year < 2010 or issue_year > 2020:
                        is_valid = False
                        break
                elif key == "eyr":
                    exp_year = int(value)
                    if exp_year < 2020 or exp_year > 2030:
                        is_valid = False
                        break
                elif key == "hgt":
                    htype = value[-2:]
                    if htype == "in":
                        height = int(value[:-2])
                        if height < 59 or height > 76:
                            is_valid = False
                            break
                    elif htype == "cm":
                        height = int(value[:-2])
                        if height < 150 or height > 193:
                            is_valid = False
                            break
                    else:
                        is_valid = False
                        break
                elif key == "hcl":
                    if not re.match("^#[0-9a-f]{6}$", value):
                        is_valid = False
                        break
                elif key == "ecl":
                    if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        is_valid = False
                        break
                elif key == "pid":
                    if not re.match("^[0-9]{9}$", value):
                        is_valid = False
                        break

        if is_valid:
            valid_passports += 1
        else:
            print("Not a valid passport: ", current_passport)
        current_passport = {}
    else:
        # Split current line into key-value pairs and add them to passport
        pairs = line.split(' ')
        for pair in pairs:
            key, value = pair.split(':')
            current_passport[key] = value

print("The number of valid passports is: {0!s}".format(valid_passports))
