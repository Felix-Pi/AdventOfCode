from day04.Day04 import parse_value

if __name__ == '__main__':
    assert (parse_value({'byr': '2003'}) is False)
    assert (parse_value({'byr': '200'}) is False)
    assert (parse_value({'byr': '2003'}) is False)
    assert (parse_value({'byr': '2003'}) is False)
    assert (parse_value({'hgt': '190in'}) is False)
    assert (parse_value({'hgt': '190'}) is False)

# ToDo
