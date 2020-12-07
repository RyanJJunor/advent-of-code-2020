import re

f = open("baggage_rules", "r").read().splitlines()

list = []
for i in f:
    list.append(i)


def how_many_bags(bag_colour):
    bags = {}
    for i in list:
        colour = i.split(" bags")[0]
        x = i.split(",")

        for i in x:
            if re.search("(\\d) (\\w+ \\w+)", i) is None:
                continue
            if colour not in bags.keys():
                bags[colour] = [re.search("(\\d) (\\w+ \\w+)", i).groups()]
            else:
                bags[colour].append(re.search("(\\d) (\\w+ \\w+)", i).groups())

    outer_bags = set()
    outer_bags = calculation(bag_colour, bags, outer_bags)
    return len(outer_bags)


def calculation(bag_colour, bags, outer_bags):
    for i in bags.keys():
        for j in bags[i]:
            if j[1] == bag_colour:
                outer_bags.add(i)
                calculation(i, bags, outer_bags)
    return outer_bags


def how_many_bags_2(bag_colour):
    bags = {}
    for i in list:
        colour = i.split(" bags")[0]
        x = i.split(",")

        for i in x:
            if re.search("(\\d) (\\w+ \\w+)", i) is None:
                continue
            if colour not in bags.keys():
                bags[colour] = [re.search("(\\d) (\\w+ \\w+)", i).groups()]
            else:
                bags[colour].append(re.search("(\\d) (\\w+ \\w+)", i).groups())

    total = calculation_2(bag_colour, bags)
    return total


def calculation_2(bag_colour, bags):

    total = 0
    if bag_colour not in bags:
        return total
    for i in bags[bag_colour]:
        this_total = int(i[0])
        total = total + (this_total + (this_total * calculation_2(i[1], bags)))
    return total


print((how_many_bags("shiny gold")))
print((how_many_bags_2("shiny gold")))

