program = "3,8,1001,8,10,8,105,1,0,0,21,34,51,68,89,98,179,260,341,422,99999,3,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,1002,9,5,9,1001,9,2,9,1002,9,2,9,4,9,99,3,9,1001,9,3,9,102,3,9,9,101,4,9,9,4,9,99,3,9,102,2,9,9,101,2,9,9,1002,9,5,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99"
_data = [int(i) for i in program.split(",")]


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
    i[a] = values.pop(0)
    # print("pop", i[a])


def output(i, a, ip):
    try:
        values[1] = i[a]
        # print(values, i[a])
    except:
        # print(i[a])
        values.append(i[a])


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


from io import StringIO
from contextlib import redirect_stdout
from copy import deepcopy

out = StringIO()
# with redirect_stdout(out):
#     for i in {0, 1, 2, 3, 4}:
#         for j in {0, 1, 2, 3, 4} - {i}:
#             for k in {0, 1, 2, 3, 4} - {i, j}:
#                 for l in {0, 1, 2, 3, 4} - {i, j, k}:
#                     for m in {0, 1, 2, 3, 4} - {i, j, k, l}:
#                         # print("---", i, j, k, l, m, "---")
#                         values = [i, 0, j, 0, k, 0, l, 0, m, 0]
#                         for _ in range(5):
#                             data = deepcopy(_data)
#                             codes = [
#                                 lambda i, ip: None,
#                                 add,
#                                 mul,
#                                 take_input,
#                                 output,
#                                 jnz,
#                                 jz,
#                                 tlt,
#                                 teq,
#                             ]
#                             offsets = [0, 4, 4, 2, 2, 3, 3, 4, 4]
#                             position = IP()
#                             opcode = data[position.get()]
#                             while True:
#                                 third_param_mode, opcode = divmod(opcode, 10000)
#                                 second_param_mode, opcode = divmod(opcode, 1000)
#                                 first_param_mode, opcode = divmod(opcode, 100)
#                                 # print(opcode)
#                                 parameters = data[
#                                     position.get()
#                                     + 1 : position.get()
#                                     + offsets[opcode]
#                                 ]
#                                 # print(opcode, parameters)
#                                 if first_param_mode:
#                                     parameters[0] = data.index(parameters[0])
#                                 if len(parameters) > 1:
#                                     if second_param_mode:
#                                         parameters[1] = data.index(parameters[1])
#                                     if third_param_mode:
#                                         parameters[2] = data.index(parameters[2])
#                                 # print(codes[opcode].__name__, parameters)
#                                 codes[opcode](data, *parameters, position)
#                                 position.set(position.get() + offsets[opcode])
#                                 opcode = data[position.get()]
#                                 if opcode == 99:
#                                     break
# out.seek(0)
# print(max(map(int, out.read().splitlines())))
from sys import stdout

with redirect_stdout(out):
    for i in {5, 6, 7, 8, 9}:
        for j in {5, 6, 7, 8, 9} - {i}:
            for k in {5, 6, 7, 8, 9} - {i, j}:
                for l in {5, 6, 7, 8, 9} - {i, j, k}:
                    for m in {5, 6, 7, 8, 9} - {i, j, k, l}:
                        # print("---", i, j, k, l, m, "---")
                        values = [i, 0, j, 0, k, 0, l, 0, m, 0]
                        thrusters = [_data.copy() for _ in range(5)]
                        thruster_ips = [IP() for _ in range(5)]
                        while True:
                            for _ in range(5):
                                data = thrusters[_]
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
                                ]
                                offsets = [0, 4, 4, 2, 2, 3, 3, 4, 4]
                                position = thruster_ips[_]
                                opcode = data[position.get()]
                                while True:
                                    third_param_mode, opcode = divmod(opcode, 10000)
                                    second_param_mode, opcode = divmod(opcode, 1000)
                                    first_param_mode, opcode = divmod(opcode, 100)
                                    # print(opcode)
                                    if opcode == 99:
                                        break
                                    # print(
                                    #     len(data), position.get(), opcode, file=stdout
                                    # )
                                    parameters = data[
                                        position.get()
                                        + 1 : position.get()
                                        + offsets[opcode]
                                    ]
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
                                    # print(opcode)
                                    position.set(position.get() + offsets[opcode])
                                    if opcode == 4:
                                        break
                                    opcode = data[position.get()]
                                    if (opcode % 100) == 99:
                                        break
                                if (opcode % 100) == 99:
                                    break
                            else:
                                continue
                            break
                        print(values[0])

out.seek(0)
print(max(map(int, out.read().splitlines())))
