def readInput():
    f = open('input.txt')
    return [line.replace('\n', '') for line in f.readlines()]


def calcPartition(input, lower, upper):
    for i in range(len(input)):
        if input[i] == 'F' or input[i] == 'L':
            lower = lower
            upper = upper - int((upper - lower) / 2) - 1
        if input[i] == 'B' or input[i] == 'R':
            upper = upper
            lower = lower + int((upper - lower) / 2) + 1
        if lower == upper:
            return lower


def part01():
    seatsIds = []

    for seat in readInput():
        row = calcPartition(seat[:7], 0, 127)
        col = calcPartition(seat[7:], 0, 7)

        seatsIds.append(row * 8 + col)

    return seatsIds


def part02():
    plane = part01()

    plane.sort()

    lastSeatId = 0
    for seat in plane:
        if seat - 2 == lastSeatId:
            return lastSeatId + 1

        lastSeatId = seat


def test():
    seats = {'FBFBBFFRLR': 357, 'BFFFBBFRRR': 567, 'FFFBBBFRRR': 119, 'BBFFBBFRLL': 820}

    for seatSpecification in seats:
        row = calcPartition(seatSpecification[:7], 0, 127)
        col = calcPartition(seatSpecification[7:], 0, 7)

        assert (seats[seatSpecification] == row * 8 + col)


if __name__ == '__main__':
    test()

    print('part01: Highest seatId: {}'.format(max(part01())))
    print('part02: My seatId: {}'.format(part02()))
