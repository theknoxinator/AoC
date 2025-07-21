# Parse bulk file of passport info and determine valid passports
import re


def check_passports(values, use_part2=False):
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
                elif use_part2:
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
            current_passport = {}
        else:
            # Split current line into key-value pairs and add them to passport
            pairs = line.split(' ')
            for pair in pairs:
                key, value = pair.split(':')
                current_passport[key] = value

    return valid_passports


def part1(values):
    return check_passports(values)


def part2(values):
    return check_passports(values, True)
