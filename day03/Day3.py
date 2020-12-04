def readInput(file):
    f = open(file)
    return [line.strip() for line in f.readlines()]


def get_pos_x(cols, pos_x):
    return pos_x % cols


def move(map, steps_right, steps_down):
    TREE = '#'

    rows = len(map)
    cols = len(map[0])
    pos_x = 0
    pos_y = 0

    tree_counter = 0

    while pos_y < rows:
        if map[pos_y][pos_x] == TREE:
            tree_counter += 1

        pos_x = get_pos_x(cols, pos_x + steps_right)
        pos_y += steps_down

    return tree_counter


def multipleMoves(map, steps):
    trees = 1

    for i in range(len(steps)):
        trees *= move(map, steps[i][0], steps[i][1])

    return trees


def test():
    input_example = readInput('example_input.txt')

    # part1
    print('Test move: {}'.format(move(input_example, 3, 1)))

    # part2
    moves = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

    print('Test multipleMoves: {}\n'.format(multipleMoves(input_example, moves)))


if __name__ == '__main__':
    test()

    # part1
    input = readInput('input.txt')
    print('part1 move: {}'.format(move(input, 3, 1)))

    # part2
    moves = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    print('part2 move: {}'.format(multipleMoves(input, moves)))
