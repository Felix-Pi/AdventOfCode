import re


def readInput(file):
    f = open(file)
    entries = f.read().split('\n\n')
    return [line.replace('\n', ' ') for line in entries]


def parse_value(passport):
    for key in passport:
        value = passport[key]
        if key == 'byr':
            if not (int(value) and len(value) == 4 and (1920 <= int(value) <= 2002)):
                return False
        if key == 'iyr':
            if not (int(value) and len(value) == 4 and (2010 <= int(value) <= 2020)):
                return False
        if key == 'eyr':
            if not (int(value) and len(value) == 4 and (2020 <= int(value) <= 2030)):
                return False
        if key == 'hgt':
            unit = value[-2:]
            unit_val = value[:-2]
            if unit == 'cm':
                if not (int(unit_val) and (150 <= int(unit_val) <= 193)):
                    return False
            if unit == 'in':
                if not (int(unit_val) and (59 <= int(unit_val) <= 76)):
                    return False
            if unit not in ['in', 'cm']:
                return False
        if key == 'hcl':
            if re.search('#[0-9a-f]{6}', value) is None or len(value) != 7:
                return False
        if key == 'ecl':
            if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        if key == 'pid':
            if re.search('[0-9]{9}', value) is None or len(value) != 9:
                return False
    return True


def validate(entries, cid_is_optional=True):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

    valid_entries = 0
    valid_passports = 0

    for entry in entries:
        attributes = entry.split()
        passport = {}

        for attribute in attributes:
            key, value = attribute.split(':')
            passport[key] = value

        missing_keys = [x for x in required_fields if x not in passport]

        isValid = True

        # ToDo: move to function
        if len(missing_keys) > 0:
            if len(missing_keys) == 1 and missing_keys[0] == 'cid' and cid_is_optional is True:
                isValid = True
            else:
                isValid = False

        if isValid is True:
            if parse_value(passport) is True:
                valid_passports += 1

            valid_entries += 1

    return valid_entries, valid_passports


def test():
    input_example = readInput('input_example.txt')
    result = validate(input_example, cid_is_optional=True)

    # part1
    print('part1 valid_entries: {}'.format(result[0]))

    # part2
    print('part2 valid_passports: {}\n'.format(result[1]))


if __name__ == '__main__':
    test()

    # part1
    input = readInput('input.txt')
    result = validate(input, cid_is_optional=True)
    print('part1 valid_entries: {}'.format(result[0]))

    # part2
    print('part2 valid_passports: {}\n'.format(result[1]))
