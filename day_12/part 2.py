import math

f = open("navigation_instructions", "r").read().splitlines()

input = []
for i in f:
    input.append(i)


class Ferry:
    ferry_x = 0
    ferry_y = 0

    waypoint_x = 10
    waypoint_y = 1


    facing = 90

    def north(self, value):
        self.waypoint_y = self.waypoint_y + value

    def south(self, value):
        self.waypoint_y = self.waypoint_y - value

    def east(self, value):
        self.waypoint_x = self.waypoint_x + value

    def west(self, value):
        self.waypoint_x = self.waypoint_x - value

    def left(self, value):
        # if value == 90:
        #     temp = self.waypoint_x
        #     self.waypoint_x = self.waypoint_y
        #     self.waypoint_y = temp
        # elif value == 180:
        #     self.waypoint_x = self.waypoint_x * -1
        #     self.waypoint_y = self.waypoint_y * -1
        # elif value == 270:
        #     temp = self.waypoint_x
        #     self.waypoint_x = self.waypoint_y
        #     self.waypoint_y = temp

        if value == 90:
            temp = self.waypoint_x
            self.waypoint_x = self.waypoint_y
            self.waypoint_y = temp
            self.waypoint_x = self.waypoint_x * -1
        elif value == 180:
            self.waypoint_x = self.waypoint_x * -1
            self.waypoint_y = self.waypoint_y * -1
        elif value == 270:
            temp = self.waypoint_x
            self.waypoint_x = self.waypoint_y
            self.waypoint_y = temp
            self.waypoint_y = self.waypoint_y * -1

    def right(self, value):
        if value == 90:
            temp = self.waypoint_x
            self.waypoint_x = self.waypoint_y
            self.waypoint_y = temp
            self.waypoint_y = self.waypoint_y * -1
        elif value == 180:
            self.waypoint_x = self.waypoint_x * -1
            self.waypoint_y = self.waypoint_y * -1
        elif value == 270:
            temp = self.waypoint_x
            self.waypoint_x = self.waypoint_y
            self.waypoint_y = temp
            self.waypoint_x = self.waypoint_x * -1


    def forward(self, value):
        self.ferry_x = self.ferry_x + (self.waypoint_x * value)
        self.ferry_y = self.ferry_y + (self.waypoint_y * value)

    def calc_manhattan(self):
        return abs(self.ferry_x) + abs(self.ferry_y)


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