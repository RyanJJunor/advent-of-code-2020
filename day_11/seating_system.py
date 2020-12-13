f = open("layout", "r").read().splitlines()

input = []
for i in f:
    input.append(i)


# def check_surrounding(layout, row, column, checkEmpty):
#     change = True
#
#     if checkEmpty:
#         char = '#'
#     else:
#         char = '#'
#         count = 0
#
#     if row > 0 and column > 0:
#         if layout[row - 1][column - 1] == char:
#             if checkEmpty:
#                 change = False
#             else:
#                 count = count + 1
#     if row > 0:
#         if layout[row - 1][column] == char:
#             if checkEmpty:
#                 change = False
#             else:
#                 count = count + 1
#     if row > 0 and column < (len(layout[row])) - 1:
#         if layout[row - 1][column + 1] == char:
#             if checkEmpty:
#                 change = False
#             else:
#                 count = count + 1
#
#     if column > 0:
#         if layout[row][column - 1] == char:
#             if checkEmpty:
#                 change = False
#             else:
#                 count = count + 1
#     if column < len(layout[row]) - 1:
#         if layout[row][column + 1] == char:
#             if checkEmpty:
#                 change = False
#             else:
#                 count = count + 1
#
#     if row < len(layout) - 1 and column > 0:
#         if layout[row + 1][column - 1] == char:
#             if checkEmpty:
#                 change = False
#             else:
#                 count = count + 1
#     if row < len(layout) - 1:
#         if layout[row + 1][column] == char:
#             if checkEmpty:
#                 change = False
#             else:
#                 count = count + 1
#     if row < len(layout) - 1 and column < len(layout[row]) - 1:
#         if layout[row + 1][column + 1] == char:
#             if checkEmpty:
#                 change = False
#             else:
#                 count = count + 1
#
#     if not checkEmpty:
#         if count < 4:
#             change = False
#
#     return change
#
#
# def get_char(input, i, j):
#     if input[i][j] == 'L':
#         if check_surrounding(input, i, j, True):
#             return '#', True
#     if input[i][j] == '#':
#         if check_surrounding(input, i, j, False):
#             return 'L', True
#
#     return input[i][j], False
#
#
# def update(input):
#     updated = []
#     stabilised = True
#
#     for i in range(len(input)):
#         updated.append("")
#         for j in range(len(input[i])):
#             char, changed = get_char(input, i, j)
#             updated[i] = updated[i] + char
#             if changed:
#                 stabilised = False
#
#     return updated, stabilised
#
#
# stabilised = False
# updated = []
#
# while not stabilised:
#
#     input, stabilised = update(input)
#
# occupied = 0
# for i in input:
#     occupied = occupied + i.count("#")
#
# print(occupied)
