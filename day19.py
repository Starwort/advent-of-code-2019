from intcode_computer_rewrite import Computer
from collections import deque

data = "109,424,203,1,21101,0,11,0,1105,1,282,21101,18,0,0,1105,1,259,2101,0,1,221,203,1,21102,1,31,0,1105,1,282,21101,0,38,0,1106,0,259,21002,23,1,2,22101,0,1,3,21101,0,1,1,21102,1,57,0,1106,0,303,2102,1,1,222,21001,221,0,3,20102,1,221,2,21101,0,259,1,21101,80,0,0,1106,0,225,21101,0,23,2,21102,91,1,0,1106,0,303,1201,1,0,223,20101,0,222,4,21101,0,259,3,21102,1,225,2,21102,1,225,1,21102,1,118,0,1105,1,225,20102,1,222,3,21101,0,87,2,21101,133,0,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21101,0,148,0,1105,1,259,2101,0,1,223,20102,1,221,4,21002,222,1,3,21101,0,9,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,1,195,0,106,0,109,20207,1,223,2,21001,23,0,1,21102,1,-1,3,21101,0,214,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2102,1,-4,249,21201,-3,0,1,22101,0,-2,2,21202,-1,1,3,21102,250,1,0,1106,0,225,21202,1,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2105,1,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,21202,-2,1,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22102,1,-2,3,21102,1,343,0,1106,0,303,1106,0,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21201,-4,0,1,21102,384,1,0,1105,1,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21202,1,1,-4,109,-5,2106,0,0"

in_queue = deque()  # type: ignore
x, y = -1, 0
all_valid = deque()  # type: ignore
testing_opposite_side = False
SQUARE_SIZE = 99
opposite = (1418, 706)


def inp():
    global x, y, testing_opposite_side, opposite
    if in_queue:
        return in_queue.popleft()
    else:
        if not testing_opposite_side:
            if last_space == 1:
                all_valid.append((x, y))

                if y >= 100:
                    in_queue.extend([x + SQUARE_SIZE, y - SQUARE_SIZE])
                    opposite = x + SQUARE_SIZE, y - SQUARE_SIZE
                    testing_opposite_side = True
                else:
                    in_queue.extend([x, y + 1])

                y += 1
            else:
                x += 1
                in_queue.extend([x, y])
        else:
            if last_space == 1:
                print(x * 10000 + (y - SQUARE_SIZE - 1))
                raise StopIteration
            testing_opposite_side = False
            in_queue.extend([x, y])

        return in_queue.popleft()


spaces = 0
last_space = 0


def out(i):
    global spaces, last_space

    spaces += i
    last_space = i


for x in range(50):
    for y in range(50):
        computer = Computer(data, in_function=deque([x, y]).popleft, out_function=out,)
        computer.run_until_complete()

print(spaces)

try:
    while True:
        computer = Computer(data, in_function=inp, out_function=out,)
        computer.run_until_complete()
except StopIteration:
    pass
