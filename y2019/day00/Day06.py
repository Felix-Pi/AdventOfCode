import math


def readInput():
    f = open('input.txt')
    return [int(line.replace('\n', '')) for line in f.readlines()]


def calcNeededFuel(mass):
    return math.floor(mass / 3) - 2


def part01():  # calc fuel for modules
    neededFuel = 0

    for mass in readInput():
        neededFuel += calcNeededFuel(mass)

    return neededFuel


def part02():
    return


def test():
    assert calcNeededFuel(12) == 2
    assert calcNeededFuel(14) == 2
    assert calcNeededFuel(1969) == 654
    assert calcNeededFuel(100756) == 33583


if __name__ == '__main__':
    test()

    print('part01: : {}'.format(part01()))
    print('part02: : {}\n'.format(part02()))
