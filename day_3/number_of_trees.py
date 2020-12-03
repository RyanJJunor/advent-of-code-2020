import math
import time

f = open("map", "r").read().splitlines()

list = []
for x in f:
    list.append(x)


def part_one(list, down, right):
    length = (len(list[0]))

    iterations = int(math.floor(len(list) / down))

    multiples_needed = math.ceil(((iterations - 1) * right) / length)

    new_map = []
    for i in list:
        new_map.append(i * multiples_needed)

    trees = 0
    count_right = 0
    count_down = 0

    for i in range(down, iterations):
        count_right = count_right + right
        count_down = count_down + down
        if new_map[count_down][count_right] == "#":
            trees = trees + 1

    return trees


def part_two():
    answer = part_one(list, 1, 1) * part_one(list, 1, 3) * part_one(list, 1, 5) * part_one(list, 1, 7) * part_one(list,
                                                                                                                  2, 1)
    return answer


def part_one_2(list, down, right):
    length = (len(list[0]))
    iterations = int(math.floor(len(list) / down))

    trees = 0
    count_right = 0
    count_down = 0

    for i in range(down, iterations):
        count_right = count_right + right
        count_down = count_down + down

        count_right = (count_right % length)

        if list[count_down][count_right] == "#":
            trees = trees + 1

    return trees


def part_two_2():
    answer = part_one_2(list, 1, 1) * part_one_2(list, 1, 3) * part_one_2(list, 1, 5) * part_one_2(list, 1,
                                                                                                   7) * part_one_2(list,
                                                                                                                   2, 1)
    return answer


print(part_one(list, 1, 3))
print(part_two())

print(part_one_2(list, 1, 3))
print(part_two_2())
