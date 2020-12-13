f = open("layout", "r").read().splitlines()

input = []
for i in f:
    input.append(i)


def get_curr(layout, y, x, y_in, x_in):
    x_max = len(layout[0]) - 1
    y_max = len(layout) - 1

    if x_in == 1:
        if x == x_max:
            return None, None

    if x_in == -1:
        if x == 0:
            return None, None

    if y_in == 1:
        if y == y_max:
            return None, None

    if y_in == -1:
        if y == 0:
            return None, None

    y = y + y_in
    x = x + x_in

    return y, x


def check_surrounding(layout, row, column, checkEmpty):
    change = True

    if checkEmpty:
        char = '#'
    else:
        char = '#'

        count = 0

    if row > 0 and column > 0:
        y, x = row - 1, column - 1
        curr = layout[y][x]
        while curr == '.':
            y, x = get_curr(layout, y, x, -1, -1)
            if y is None or x is None:
                break
            else:
                curr = layout[y][x]
        if curr == char:
            if checkEmpty:
                change = False
            else:
                count = count + 1

    if row > 0:
        y, x = row - 1, column
        curr = layout[y][x]
        while curr == '.':
            y, x = get_curr(layout, y, x, -1, 0)
            if y is None or x is None:
                break
            else:
                curr = layout[y][x]
        if curr == char:
            if checkEmpty:
                change = False
            else:
                count = count + 1

    if row > 0 and column < (len(layout[row])) - 1:
        y, x = row - 1, column + 1
        curr = layout[y][x]
        while curr == '.':
            y, x = get_curr(layout, y, x, -1, 1)
            if y is None or x is None:
                break
            else:
                curr = layout[y][x]
        if curr == char:
            if checkEmpty:
                change = False
            else:
                count = count + 1

    if column > 0:
        y, x = row, column - 1
        curr = layout[y][x]
        while curr == '.':
            y, x = get_curr(layout, y, x, 0, -1)
            if y is None or x is None:
                break
            else:
                curr = layout[y][x]
        if curr == char:
            if checkEmpty:
                change = False
            else:
                count = count + 1

    if column < len(layout[row]) - 1:
        y, x = row, column + 1
        curr = layout[y][x]
        while curr == '.':
            y, x = get_curr(layout, y, x, 0, 1)
            if y is None or x is None:
                break
            else:
                curr = layout[y][x]
        if curr == char:
            if checkEmpty:
                change = False
            else:
                count = count + 1

    if row < len(layout) - 1 and column > 0:
        y, x = row + 1, column - 1
        curr = layout[y][x]
        while curr == '.':
            y, x = get_curr(layout, y, x, 1, - 1)
            if y is None or x is None:
                break
            else:
                curr = layout[y][x]
        if curr == char:
            if checkEmpty:
                change = False
            else:
                count = count + 1

    if row < len(layout) - 1:
        y, x = row + 1, column
        curr = layout[y][x]
        while curr == '.':
            y, x = get_curr(layout, y, x, 1, 0)
            if y is None or x is None:
                break
            else:
                curr = layout[y][x]
        if curr == char:
            if checkEmpty:
                change = False
            else:
                count = count + 1

    if row < len(layout) - 1 and column < len(layout[row]) - 1:
        y, x = row + 1, column + 1
        curr = layout[y][x]
        while curr == '.':
            y, x = get_curr(layout, y, x, 1, 1)
            if y is None or x is None:
                break
            else:
                curr = layout[y][x]
        if curr == char:
            if checkEmpty:
                change = False
            else:
                count = count + 1

    if not checkEmpty:
        if count < 5:
            change = False

    return change


def get_char(input, i, j):
    if input[i][j] == 'L':
        if check_surrounding(input, i, j, True):
            return '#', True
    if input[i][j] == '#':
        if check_surrounding(input, i, j, False):
            return 'L', True

    return input[i][j], False


def update(input):
    updated = []
    stabilised = True

    for i in range(len(input)):
        updated.append("")
        for j in range(len(input[i])):
            char, changed = get_char(input, i, j)
            updated[i] = updated[i] + char
            if changed:
                stabilised = False

    return updated, stabilised


stabilised = False
updated = []

while not stabilised:
    input, stabilised = update(input)

occupied = 0
for i in input:
    occupied = occupied + i.count("#")

print(occupied)
