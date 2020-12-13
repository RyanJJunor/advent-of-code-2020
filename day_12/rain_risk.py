import math

f = open("navigation_instructions", "r").read().splitlines()

input = []
for i in f:
    input.append(i)


class Ferry:
    x = 0
    y = 0
    facing = 90

    def north(self, value):
        self.y = self.y + value

    def south(self, value):
        self.y = self.y - value

    def east(self, value):
        self.x = self.x + value

    def west(self, value):
        self.x = self.x - value

    def left(self, value):
        self.facing = (self.facing - value) % 360

    def right(self, value):
        self.facing = (self.facing + value)  % 360

    def forward(self, value):
        if self.facing == 0:
            self.north(value)
        elif self.facing == 90:
            self.east(value)
        elif self.facing == 180:
            self.south(value)
        elif self.facing == 270:
            self.west(value)

    def calc_manhattan(self):
        return abs(self.x) + abs(self.y)


def parse(ferry, command):
    action = command[0]
    value = int(command[1:])

    if action == "N":
        ferry.north(value)
    elif action == "S":
        ferry.south(value)
    elif action == "E":
        ferry.east(value)
    elif action == "W":
        ferry.west(value)
    elif action == "L":
        ferry.left(value)
    elif action == "R":
        ferry.right(value)
    elif action == "F":
        ferry.forward(value)


ferry = Ferry()

for i in input:
    parse(ferry, i)

print(ferry.calc_manhattan())