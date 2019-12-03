data = [
    int(i)
    for i in "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,6,23,27,1,6,27,31,2,31,9,35,1,35,6,39,1,10,39,43,2,9,43,47,1,5,47,51,2,51,6,55,1,5,55,59,2,13,59,63,1,63,5,67,2,67,13,71,1,71,9,75,1,75,6,79,2,79,6,83,1,83,5,87,2,87,9,91,2,9,91,95,1,5,95,99,2,99,13,103,1,103,5,107,1,2,107,111,1,111,5,0,99,2,14,0,0".split(
        ","
    )
]
# data = [1, 0, 0, 0, 99]


def add(i, a, b, c):
    i[c] = i[a] + i[b]


def mul(i, a, b, c):
    i[c] = i[a] * i[b]


data[1] = 12
data[2] = 2

codes = [None, add, mul]
position = 0
opcode = data[position]
while opcode in (1, 2, 99):
    # print(opcode, position + 1, position + 2, position + 3)
    # print(opcode, data[position + 1], data[position + 2], data[position + 3])
    codes[opcode](data, data[position + 1], data[position + 2], data[position + 3])
    position += 4
    opcode = data[position]
    if opcode == 99:
        print(data[0])
        # print(data)
        break
# print("err")
# print(data)
for i in range(100):
    for j in range(100):
        data = [
            int(i)
            for i in "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,6,23,27,1,6,27,31,2,31,9,35,1,35,6,39,1,10,39,43,2,9,43,47,1,5,47,51,2,51,6,55,1,5,55,59,2,13,59,63,1,63,5,67,2,67,13,71,1,71,9,75,1,75,6,79,2,79,6,83,1,83,5,87,2,87,9,91,2,9,91,95,1,5,95,99,2,99,13,103,1,103,5,107,1,2,107,111,1,111,5,0,99,2,14,0,0".split(
                ","
            )
        ]
        data[1] = i
        data[2] = j
        position = 0
        opcode = data[position]
        while opcode in (1, 2, 99):
            # print(opcode, position + 1, position + 2, position + 3)
            # print(opcode, data[position + 1], data[position + 2], data[position + 3])
            codes[opcode](
                data, data[position + 1], data[position + 2], data[position + 3]
            )
            position += 4
            opcode = data[position]
            if opcode == 99:
                if data[0] == 19690720:
                    print(i * 100 + j)
                # print(data)
                break
