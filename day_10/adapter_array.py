import time
start = time.time()

f = open("output_joltage", "r").read().splitlines()

input = []
for i in f:
    input.append(int(i))


def find_diffs(input):
    adapters = sorted(input)

    diff_1 = 0
    diff_2 = 0
    diff_3 = 0

    previous = 0

    for i in range(len(adapters)):

        if (adapters[i] - previous) == 1:
            diff_1 = diff_1 + 1
        elif (adapters[i] - previous) == 2:
            diff_2 = diff_2 + 1
        elif (adapters[i] - previous) == 3:
            diff_3 = diff_3 + 1

        previous = adapters[i]

    return diff_1, diff_2, diff_3 + 1


def add_dict(tree ,num, x, y, z):

    one = num+1
    two = num+2
    three = num+3

    if x in [one, two, three]:
        if(num not in tree):
            tree[num] = [x]
        else:
            tree[num].append(x)

    if y in [one, two, three]:
        if (num not in tree):
            tree[num] = [y]
        else:
            tree[num].append(y)

    if z in [one, two, three]:
        if (num not in tree):
            tree[num] = [z]
        else:
            tree[num].append(z)


def generate_tree(input):

    input.append(0)
    input.append(max(input) + 3)
    adapters = sorted(input)

    tree = {}

    for i in range(len(adapters)):

        if i == len(adapters) - 3:
            add_dict(tree, adapters[i], adapters[i+1], adapters[i+2], -1)
            continue

        if i == len(adapters) - 2:
            add_dict(tree, adapters[i], adapters[i+1], -1, -1)
            continue

        if i == len(adapters) - 1:
            add_dict(tree, adapters[i], -1, -1, -1)
            continue

        add_dict(tree, adapters[i], adapters[i + 1], adapters[i + 2], adapters[i +3])
    return tree




#RECURSION< TOO LONG
# def find_path(key, tree):
#
#     total = 0
#
#     for i in tree[key]:
#         if i == max(tree.keys()):
#             total = total + 1
#         if i != max(tree.keys()):
#             total = total + find_path(i, tree)
#
#     return total



diff1, diff2, diff3 = find_diffs(input)
print(diff1 * diff3)


tree = generate_tree(input)
#print(find_path(0, tree))



def find_number_of_permutations(tree):

    # vals = []
    vals = {}
    for i in tree:

        print(i)

        # vals.extend(tree[i])
        # vals.extend((tree[i]) * (vals.count(i) - 1))

        for j in tree[i]:
            if j not in vals.keys():
                if i in vals.keys():
                    vals[j] = vals[i]
                else: vals[j] = 1
            else:
                vals[j] = vals[j] + (vals[i])

    return vals[max(vals)]

print(find_number_of_permutations(tree))

#print(vals.count(max(vals)))
# total = 1
# for i in tree:
#     size = len(tree[i])
#     if size > 1:
#         occurrences = 0
#         for j in tree.values():
#             if i in j:
#                 occurrences = occurrences + 1
#
#         total = total + (occurrences * (size - 1))

#print(total)
print(f"Time taken: {time.time() - start} seconds")


