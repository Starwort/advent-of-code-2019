from utils import permutations_of, float_range, deep_loop
import sys
from collections import defaultdict

DEBUG = False
if "--debug" in sys.argv or "-d" in sys.argv:
    print("Entering debug mode")
    DEBUG = True


class InfiniteTape:
    def __init__(self, items):
        self.data = defaultdict(int)
        for index, i in enumerate(items):
            self.data[index] = i

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self.data[i] for i in range(key.start, key.stop)]
        else:
            return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value


data = InfiniteTape(int(i) for i in input("Enter the intcode program\n>>> ").split(","))


class IP:
    def __init__(self):
        self.address = 0

    def set(self, new_address):
        self.address = new_address

    def get(self):
        return self.address


def add(i, a, b, c, ip):
    i[c] = a + b


def mul(i, a, b, c, ip):
    i[c] = a * b


def take_input(i, a, ip):
    i[a] = int(input("Program is requesting input\n>>> "))


def output(i, a, ip):
    print(a)


def jnz(i, a, b, ip):
    if a:
        ip.set(b - 3)


def jz(i, a, b, ip):
    if not a:
        ip.set(b - 3)


def tlt(i, a, b, c, ip):
    if a < b:
        i[c] = 1
    else:
        i[c] = 0


def teq(i, a, b, c, ip):
    if a == b:
        i[c] = 1
    else:
        i[c] = 0


def mod_base(i, a, ip):
    global relative_base
    relative_base += a


relative_base = 0
codes = [
    lambda i, ip: None,
    add,
    mul,
    take_input,
    output,
    jnz,
    jz,
    tlt,
    teq,
    mod_base,
]
offsets = [1, 4, 4, 2, 2, 3, 3, 4, 4, 2]
position = IP()
opcode = data[position.get()]
while True:
    # if DEBUG:
    #     print(data)
    #     input()
    third_param_mode, opcode = divmod(opcode, 10000)
    second_param_mode, opcode = divmod(opcode, 1000)
    first_param_mode, opcode = divmod(opcode, 100)
    # print(opcode)
    parameters = data[position.get() + 1 : position.get() + offsets[opcode]]
    # print(opcode, parameters)
    # if len(parameters) == 0:
    #     print(opcode)
    if first_param_mode == 0:
        if opcode != 3:
            parameters[0] = data[parameters[0]]
    if first_param_mode == 2:
        # print(opcode, *parameters)
        # print(relative_base)
        parameters[0] = parameters[0] + relative_base
        if opcode != 3:
            parameters[0] = data[parameters[0]]
    if len(parameters) > 1:
        if second_param_mode == 0:
            parameters[1] = data[parameters[1]]
        if second_param_mode == 2:
            parameters[1] = data[parameters[1] + relative_base]
    if len(parameters) > 2:
        # if third_param_mode == 0:
        #     parameters[2] = data[parameters[2]]
        if third_param_mode == 2:
            parameters[2] = parameters[2] + relative_base
    # print(codes[opcode].__name__, parameters)
    codes[opcode](data, *parameters, position)
    position.set(position.get() + offsets[opcode])
    opcode = data[position.get()]
    if opcode == 99:
        break
