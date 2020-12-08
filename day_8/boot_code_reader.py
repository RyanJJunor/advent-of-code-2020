f = open("boot_code", "r").read().splitlines()

list = []
for i in f:
    list.append(i)


class BootCode:

    def __init__(self, commands):
        self.accumulator = 0
        self.index = 0
        self.max_index = len(commands)
        self.commands_ran = []
        self.commands = commands

    def acc(self, num):
        self.accumulator = self.accumulator + int(num)
        self.index = self.index + 1

    def jmp(self, skips):
        self.index = self.index + skips

    def nop(self):
        self.index = self.index + 1
        return

    def parse(self, command):
        command = command.split()
        command_name = command[0]
        command_value = int(command[1])

        if command_name == "acc":
            self.acc(command_value)
        if command_name == "jmp":
            self.jmp(command_value)
        if command_name == "nop":
            self.nop()

    def parse(self, command, swap, counter):
        command = command.split()
        command_name = command[0]
        command_value = int(command[1])

        if command_name == "acc":
            self.acc(command_value)
        if command_name == "jmp" and swap == counter:
            self.jmp(command_value)
            counter = counter + 1
        if command_name == "nop":
            self.nop()
            counter = counter + 1

    def run(self):
        swap = 1
        counter = 1
        while self.index != self.max_index:
            if self.index not in self.commands_ran:
                self.commands_ran.append(self.index)
                self.parse(self.commands[self.index], swap, counter)
            else:
                swap = swap + 1
                self.commands_ran.clear()
                self.index = 0


class BootCode2:

    def __init__(self, commands):
        self.accumulator = 0
        self.index = 0
        self.max_index = len(commands)
        self.commands_ran = []
        self.commands = commands
        self.counter = 0
        self.swap = 0

    def acc(self, num):
        self.accumulator = self.accumulator + int(num)
        self.index = self.index + 1

    def jmp(self, skips):
        self.index = self.index + skips

    def nop(self):
        self.index = self.index + 1
        return

    def parse(self, command):
        command = command.split()
        command_name = command[0]
        command_value = int(command[1])

        if command_name == "acc":
            self.acc(command_value)
        if (command_name == "jmp") and (self.swap != self.counter):
            self.jmp(command_value)
            self.counter = self.counter + 1
        elif command_name == "jmp":
            self.nop()
            self.counter = self.counter + 1
        if (command_name == "nop") and (self.swap != self.counter):
            self.nop()
            self.counter = self.counter + 1
        elif command_name == "nop":
            self.jmp(command_value)
            self.counter = self.counter + 1

    def run(self):
        while self.index != self.max_index:
            if (self.index not in self.commands_ran) and (self.index < self.max_index + 1):
                self.commands_ran.append(self.index)
                self.parse(self.commands[self.index])
            else:
                self.swap = self.swap + 1
                self.commands_ran = []
                self.counter = 0
                self.index = 0
                self.accumulator = 0


bootCode = BootCode2(list)

bootCode.run()

print(bootCode.accumulator)
