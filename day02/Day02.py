import re


def readInput():
    f = open('input.txt')
    return [line[:-1] for line in f.readlines()]


def part1_parse(input):
    valid_counter = 0
    line_regex = re.compile('(\d*)-(\d*)\s(\w):\s(\w*)')  # '1-3 a: abcde'

    for line in input:
        min, max, char, pw = line_regex.match(line).groups()

        char_count = pw.count(char)

        if int(min) <= char_count <= int(max):
            valid_counter += 1

    return valid_counter


def part2_parse(input):
    valid_counter = 0
    line_regex = re.compile('(\d*)-(\d*)\s(\w):\s(\w*)')  # '1-3 a: abcde'

    for line in input:
        first_occurence, second_occurence, char, pw = line_regex.match(line).groups()

        first_char = pw[int(first_occurence) - 1]
        second_char = pw[int(second_occurence) - 1]

        if (first_char is char) ^ (second_char is char):
            valid_counter += 1

    return valid_counter


def test():
    input = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
    print('Test parse: {}'.format(part1_parse(input)))
    print('Test parse: {}'.format(part2_parse(input)))


if __name__ == '__main__':
    test()

    input = readInput()
    print('parse: {}'.format(part1_parse(input)))
    print('parse: {}'.format(part2_parse(input)))
