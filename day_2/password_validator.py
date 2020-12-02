import re

f = open("passwords", "r")

list = []
for x in f:
    list.append(x)


def validate_password(list):
    count = 0

    for x in list:
        line = x.split(" ")
        limits = line[0].split("-")

        char = line[1][0]
        password = line[2].split("\\")[0]
        lower = int(limits[0])
        upper = int(limits[1])

        num = len(re.findall(char, password))
        if lower <= num <= upper:
            count = count + 1

    return count


def validate_password_part_2(list):
    count = 0

    for x in list:
        line = x.split(" ")
        limits = line[0].split("-")

        char = line[1][0]
        password = line[2].split("\\")[0]
        lower = int(limits[0])
        upper = int(limits[1])

        index1 = lower - 1
        index2 = upper - (lower + 2)

        if re.match(f"((^.{{{index1}}}{char}.{{{index2}}}[^{char}])|(^.{{{index1}}}[^{char}].{{{index2}}}{char}))",
                    password):
            count = count + 1

    return count


print(validate_password(list))
print(validate_password_part_2(list))
