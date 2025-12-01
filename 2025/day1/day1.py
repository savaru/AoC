dial = 50

def puzzle1():
    global dial
    zeroes = sum(1 for dial in dials() if dial == 0)
    print('Puzzle 1, password: ' + str(zeroes))
    dial = 50

def puzzle2():
    global dial
    print(sum(amount_of_zeroes for _, amount_of_zeroes in shift2()))


def shift2():
    global dial
    for direction, offset in shift():
        diff = direction * offset

        match direction:
            case 1:
                a, x = dial + direction, dial + diff
            case -1:
                a, x = dial + diff, dial + direction
            case _:
                assert False

        amount_of_zeroes = x // 100 + 1 - (a // 100 + 1 - (a % 100 == 0))
        dial = (dial + diff)  % 100
        yield dial, amount_of_zeroes

def shift():
    with open('input') as input:
        for line in input:
            direction = {'L': -1, 'R': 1}[line[0]]
            offset = int(line[1:])
            yield direction, offset

def dials():
    global dial

    for direction, offset in shift():
        dial = (dial + direction * offset) % 100
        yield dial


def main():
    puzzle1()
    puzzle2()
if __name__ == '__main__':
    main()
