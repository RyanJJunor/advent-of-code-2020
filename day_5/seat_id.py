import math

f = open("boarding_passes", "r").read().splitlines()

list = []
for i in f:
    list.append(i)

rows = 127
columns = 7


def calc_lower(upper, lower):
    return upper, math.ceil(upper - ((upper - lower) / 2))


def calc_upper(upper, lower):
    return math.floor(upper - ((upper - lower) / 2)), lower


def calculate_highest_id(list, rows, columns):
    ids = []
    highest_id = 0

    for boarding_pass in list:
        rows_lower = 0
        rows_upper = rows
        columns_lower = 0
        columns_upper = columns
        for char in boarding_pass:
            if char == "F":
                rows_upper, rows_lower = calc_upper(rows_upper, rows_lower)
            if char == "B":
                rows_upper, rows_lower = calc_lower(rows_upper, rows_lower)
            if char == "L":
                columns_upper, columns_lower = calc_upper(columns_upper, columns_lower)
            if char == "R":
                columns_upper, columns_lower = calc_lower(columns_upper, columns_lower)

        id = (rows_upper * 8) + columns_upper
        ids.append(id)

        if id > highest_id:
            highest_id = id

    ids = sorted(ids)

    expected = ids[0]

    for i in ids:

        if i != expected:
            break

        expected = expected + 1
    return highest_id, expected


def calculate_highest_id_2(list, rows, columns):
    ids = []
    highest_id = 0

    for boarding_pass in list:
        boarding_pass = boarding_pass.replace("F", "0")
        boarding_pass = boarding_pass.replace("B", "1")
        boarding_pass = boarding_pass.replace("L", "0")
        boarding_pass = boarding_pass.replace("R", "1")

        row_string = boarding_pass[0:7]
        column_string = boarding_pass[7:10]

        id = (int(row_string, 2) * 8) + int(column_string, 2)
        ids.append(id)

        if id > highest_id:
            highest_id = id

    # Finding my id
    ids = sorted(ids)

    expected = ids[0]

    for i in ids:
        if i != expected:
            break

        expected = expected + 1
    return highest_id, expected


print(calculate_highest_id(list, rows, columns))
print(calculate_highest_id_2(list, rows, columns))

