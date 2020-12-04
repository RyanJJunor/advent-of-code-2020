import re

f = open("passports", "r").read().splitlines()

list = []
for x in f:
    line = x.split(" ")
    for y in line:
        list.append(y)


def count_valid(list):
    passports = []
    count = 0

    new_passport = True

    for x in list:

        if new_passport:
            passports.append([])
            new_passport = False

        if x == '':
            count = count + 1
            new_passport = True
            continue

        passports[count].append(x.split(":")[0])

    valid = 0

    # Checks if all required fields are in passport
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in passports:
        print(passport)
        if all(x in passport for x in required_fields):
            valid = valid + 1

    return valid


def validate_byr(byr):
    if re.fullmatch("\\d{4}", byr) is not None:
        if 1920 <= int(byr) <= 2002:
            return True

    return False


def validate_iyr(iyr):
    if re.fullmatch("\\d{4}", iyr) is not None:
        if 2010 <= int(iyr) <= 2020:
            return True

    return False


def validate_eyr(eyr):
    if re.fullmatch("\\d{4}", eyr) is not None:
        if 2020 <= int(eyr) <= 2030:
            return True

    return False


def validate_hgt(hgt):
    if re.fullmatch("\\d{3}cm", hgt) is not None:
        if 150 <= int(hgt.split("cm")[0]) <= 193:
            return True
    if re.fullmatch("\\d{2}in", hgt) is not None:
        if 59 <= int(hgt.split("in")[0]) <= 76:
            return True
    return False


def validate_hcl(hcl):
    if re.fullmatch("#[0-9a-f]{6}", hcl) is not None:
        return True


def validate_ecl(ecl):
    if re.fullmatch("(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)", ecl) is not None:
        return True

    return False


def validate_pid(pid):
    if re.fullmatch("\\d{9}", pid) is not None:
        return True

    return False


def count_valid_with_validation(list):
    # Get a list of passports without the spaces and new lines
    passports = []
    count = 0

    new_passport = True

    for x in list:

        if new_passport:
            passports.append([])
            new_passport = False

        if x == '':
            count = count + 1
            new_passport = True
            continue

        passports[count].append(x)

    valid = 0

    # Checks if all required fields are in passport
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for passport in passports:
        # Create dictionary
        items = {}
        for item in passport:
            split = item.split(":")
            items[split[0]] = split[1]

        # Checking if all required fields are present
        if all(x in items for x in required_fields):

            # Validate each field, and if all are true increment valid counter
            if all([validate_byr(items.get("byr")), validate_iyr(items.get("iyr")), validate_eyr(items.get("eyr")),
                    validate_hgt(items.get("hgt")), validate_hcl(items.get("hcl")), validate_ecl(items.get("ecl")),
                    validate_pid(items.get("pid"))]):
                valid = valid + 1

    return valid


print(count_valid_with_validation(list))
