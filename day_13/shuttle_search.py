f = open("buses", "r").read().splitlines()

input = []
for i in f:
    input.append(i)


arrival = int(input[0])
schedule = input[1].split(",")
buses = []
original = []
for bus in schedule:
    if bus != 'x':
        temp = int(bus)
        while temp <= arrival:
            temp = temp + int(bus)
        buses.append(temp)
        original.append(int(bus))

print(buses)
delays = {}
for i in range(len(original)):
    delays[buses[i] % arrival] = original[i]

print(delays)
shortest = min(delays.keys())
print(shortest)
print(shortest * delays.get(shortest))