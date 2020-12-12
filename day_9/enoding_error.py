f = open("port_outputs", "r").read().splitlines()

list = []
for i in f:
    list.append(int(i))


def contains_sum(num, list):

    for i in list:
        if ((num - i) in list) and (i != (num / 2)):
            return True

    return False


def find_invalid_number(list, preamble, numbers_before):
    current_numbers = []
    preamble_passed = False

    for i in list:
        if preamble_passed:
            if not contains_sum(i, current_numbers):
                return i

        if len(current_numbers) == numbers_before:
            current_numbers.pop()
        if len(current_numbers) < numbers_before:
            current_numbers.insert(0, i)

        if len(current_numbers) == preamble:
            preamble_passed = True





def find_weakness(list, number_to_find):
    number_found = False
    start = 0
    counter = 0
    number = 0
    while not number_found:
        if number == 0:
            number = number + list[start]

        counter = counter + 1
        number = number + list[counter]


        if number > number_to_find:
            start = start + 1
            counter = start
            number = 0

        if number == number_to_find:
            return sorted(list[start:counter + 1])

weakness = find_weakness(list, find_invalid_number(list, 25, 25))

print(weakness[0] + weakness[len(weakness) - 1])
