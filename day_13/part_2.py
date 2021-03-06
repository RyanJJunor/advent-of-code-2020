import time

start = time.time()
f = open("buses", "r").read().splitlines()

input = []
for i in f:
    input.append(i)

schedule = input[1].split(",")


print(schedule)
def check_valid_depart(timestamp, bus, offset):

    if bus == 'x':
        return True
    if ((timestamp + offset) % int(bus)) == 0:
        return True
    else:
        return False

valid_departures = False

timestamp = 0
while not valid_departures:
    valid_departures = True
    timestamp = timestamp + int(schedule[0])
    for i in range(len(schedule)):
        if (not check_valid_depart(timestamp, schedule[i], i)):
            valid_departures = False


print(timestamp)
print(f"Time taken: {time.time() - start} seconds")

