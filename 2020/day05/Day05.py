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


def part02(seatIds):
    seatIds.sort()

    lastSeatId = 0
    for seat in seatIds:
        if seat - 2 == lastSeatId:
            return lastSeatId + 1

        lastSeatId = seat


def test():
    seats = {'FBFBBFFRLR': 357, 'BFFFBBFRRR': 567, 'FFFBBBFRRR': 119, 'BBFFBBFRLL': 820}

    for seatSpecification in seats:
        row = calcPartition(seatSpecification[:7], 0, 127)
        col = calcPartition(seatSpecification[7:], 0, 7)

        assert (seats[seatSpecification] == row * 8 + col)


def binaryApproach():
    f = open('input.txt')
    seats = [int(line.replace('\n', '').replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2) for
             line in
             f.readlines()]

    lastSeatId = 0

    seats.sort()

    for seat in seats:
        if seat - 2 == lastSeatId:
            return max(seats), lastSeatId + 1
        lastSeatId = seat


if __name__ == '__main__':
    test()

    print('part01: Highest seatId: {}'.format(max(part01())))
    print('part02: My seatId: {}\n'.format(part02(part01())))

    binaryRes = binaryApproach()
    print('binaryApproach: Highest seatId: {}, My seatId {}'.format(binaryRes[0], binaryRes[1]))
