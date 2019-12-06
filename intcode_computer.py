import sys

DEBUG = False
if "--debug" in sys.argv or "-d" in sys.argv:
    print("Entering debug mode")
    DEBUG = True
data = [int(i) for i in input("Enter the intcode program\n>>> ").split(",")]


class IP:
    def __init__(self):
        self.address = 0

    def set(self, new_address):
        self.address = new_address

    def get(self):
        return self.address


def add(i, a, b, c, ip):
    i[c] = i[a] + i[b]


def mul(i, a, b, c, ip):
    i[c] = i[a] * i[b]


def take_input(i, a, ip):
    i[a] = int(input("Program is requesting input\n>>> "))


def output(i, a, ip):
    print(i[a])


def jnz(i, a, b, ip):
    if i[a]:
        ip.set(i[b] - 3)


def jz(i, a, b, ip):
    if not i[a]:
        ip.set(i[b] - 3)


def tlt(i, a, b, c, ip):
    if i[a] < i[b]:
        i[c] = 1
    else:
        i[c] = 0


def teq(i, a, b, c, ip):
    if i[a] == i[b]:
        i[c] = 1
    else:
        i[c] = 0


codes = [lambda i, ip: None, add, mul, take_input, output, jnz, jz, tlt, teq]
offsets = [0, 4, 4, 2, 2, 3, 3, 4, 4]
position = IP()
opcode = data[position.get()]
while True:
    if DEBUG:
        print(data)
        input()
    third_param_mode, opcode = divmod(opcode, 10000)
    second_param_mode, opcode = divmod(opcode, 1000)
    first_param_mode, opcode = divmod(opcode, 100)
    # print(opcode)
    parameters = data[position.get() + 1 : position.get() + offsets[opcode]]
    # print(opcode, parameters)
    if first_param_mode:
        parameters[0] = data.index(parameters[0])
    if len(parameters) > 1:
        if second_param_mode:
            parameters[1] = data.index(parameters[1])
        if third_param_mode:
            parameters[2] = data.index(parameters[2])
    # print(codes[opcode].__name__, parameters)
    codes[opcode](data, *parameters, position)
    position.set(position.get() + offsets[opcode])
    opcode = data[position.get()]
    if opcode == 99:
        break
