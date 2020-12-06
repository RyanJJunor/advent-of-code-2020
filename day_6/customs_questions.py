f = open("declarations", "r").read().splitlines()

list = []
for i in f:
    list.append(i)

def sum_of_yes(list):
    answers = []
    num_of_people = []
    group = 0
    for i in list:
        if len(answers) == 0:
            answers.append(i)
            continue

        if i == "":
            group = group + 1
            answers.append(i)
            continue

        answers[group] = answers[group] + i


    total = 0
    for i in answers:

        total = total + len(set(i))

    return total



def find_all_yes(answers, num_of_people):

    total = 0

    for i in answers:

        if answers[i] == num_of_people:
            total = total + 1

    return total



def sum_of_all_yes(list):
    answers = []
    num_of_people = []
    group = 0
    for i in list:
        if len(answers) == 0:
            answers.append(i)
            num_of_people.append(1)
            continue

        if i == "":
            group = group + 1
            answers.append(i)
            num_of_people.append(0)
            continue

        answers[group] = answers[group] + i
        num_of_people[group] = num_of_people[group] + 1


    total = 0


    for i in range(len(answers)):
        all_answers = {}
        for j in answers[i]:
            if j not in all_answers:
                all_answers[j] = 1
            else:
                all_answers[j] = all_answers[j] + 1

        total = total + find_all_yes(all_answers, num_of_people[i])

    return total




print(sum_of_yes(list))
print(sum_of_all_yes(list))
