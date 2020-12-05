from y2020.day04.Day04 import parse_value, parse_passport, validate

if __name__ == '__main__':
    # passport
    assert parse_passport('ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm')[0] is True
    assert parse_passport('iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929')[0] is False
    assert parse_passport('hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm')[0] is True
    assert parse_passport('hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm', False)[0] is False
    assert parse_passport('hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in')[0] is False

    #   invalid
    assert validate(['eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926'])[1] == 0
    assert validate(['iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946'])[1] == 0
    assert validate(['hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277'])[1] == 0
    assert validate(['hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007'])[1] == 0

    #   valid
    assert validate(['pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f'])[1] == 1
    assert validate(['eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm'])[1] == 1
    assert validate(['hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022'])[1] == 1
    assert validate(['iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'])[1] == 1

    # byr
    assert (parse_value({'byr': '2003'}) is False)
    assert (parse_value({'byr': '1919'}) is False)
    assert (parse_value({'byr': '1929'}) is True)

    # hgt
    assert (parse_value({'hgt': '190in'}) is False)
    assert (parse_value({'hgt': '190'}) is False)
    assert (parse_value({'hgt': '60in'}) is True)
    assert (parse_value({'hgt': '190cm'}) is True)

    # hcl
    assert (parse_value({'hcl': '#123abc'}) is True)
    assert (parse_value({'hcl': '#123abz'}) is False)
    assert (parse_value({'hcl': '123abc'}) is False)

    # ecl
    assert (parse_value({'ecl': 'brn'}) is True)
    assert (parse_value({'ecl': 'wat'}) is False)

    # pid
    assert (parse_value({'pid': '000000001'}) is True)
    assert (parse_value({'pid': '0123456789'}) is False)
