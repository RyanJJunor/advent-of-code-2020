import time

f = open("expense_report", "r")

list = []
for x in f:
    list.append(int(x))


def find_multiple_value(list):
    for x in list:
        for y in list:
            if (x + y) == 2020:
                return x * y


def find_multiple_value_other(list):
    for x in list:
        if (2020 - x) in list:
            return x * list[list.index(2020 - x)]


def find_multiple_value_part_2(list):
    for x in list:
        for y in list:
            for z in list:
                if (x + y + z) == 2020:
                    return x * y * z


def find_multiple_value_other_part_2(list):
    for x in list:
        for y in list:
            if (2020 - x - y) in list:
                return x * y * list[list.index(2020 - x - y)]


start_time = time.time()
print(find_multiple_value_part_2(list))
print("--- first function took %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(find_multiple_value_other_part_2(list))
print("--- second function took %s seconds ---" % (time.time() - start_time))
