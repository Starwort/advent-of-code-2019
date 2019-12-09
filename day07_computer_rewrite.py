from intcode_computer_rewrite import Computer
from itertools import permutations
from typing import List
from collections import deque

tape = "3,8,1001,8,10,8,105,1,0,0,21,34,51,68,89,98,179,260,341,422,99999,3,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,1002,9,5,9,1001,9,2,9,1002,9,2,9,4,9,99,3,9,1001,9,3,9,102,3,9,9,101,4,9,9,4,9,99,3,9,102,2,9,9,101,2,9,9,1002,9,5,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99"

all_outs: List[int] = []
for i, j, k, l, m in permutations({0, 1, 2, 3, 4}):
    queue = [i, 0, j]
    computer_1_part_1 = Computer(
        tape, in_function=lambda: queue.pop(0), out_function=queue.append
    )
    computer_1_part_1.run_until_complete()
    queue.append(k)
    computer_2_part_1 = Computer(
        tape, in_function=lambda: queue.pop(0), out_function=queue.append
    )
    computer_2_part_1.run_until_complete()
    queue.append(l)
    computer_3_part_1 = Computer(
        tape, in_function=lambda: queue.pop(0), out_function=queue.append
    )
    computer_3_part_1.run_until_complete()
    queue.append(m)
    computer_4_part_1 = Computer(
        tape, in_function=lambda: queue.pop(0), out_function=queue.append
    )
    computer_4_part_1.run_until_complete()
    computer_5_part_1 = Computer(
        tape, in_function=lambda: queue.pop(0), out_function=all_outs.append
    )
    computer_5_part_1.run_until_complete()
print(max(all_outs))

all_outs_p2: List[int] = []
for i, j, k, l, m in permutations({5, 6, 7, 8, 9}):
    computer_1_queue = deque([i, 0])
    computer_2_queue = deque([j])
    computer_3_queue = deque([k])
    computer_4_queue = deque([l])
    computer_5_queue = deque([m])
    computer_1_part_2 = Computer(
        tape,
        in_function=computer_1_queue.popleft,
        out_function=computer_2_queue.append,
    )
    computer_2_part_2 = Computer(
        tape,
        in_function=computer_2_queue.popleft,
        out_function=computer_3_queue.append,
    )
    computer_3_part_2 = Computer(
        tape,
        in_function=computer_3_queue.popleft,
        out_function=computer_4_queue.append,
    )
    computer_5_part_2 = Computer(
        tape,
        in_function=computer_5_queue.popleft,
        out_function=computer_1_queue.append,
    )
    computer_4_part_2 = Computer(
        tape,
        in_function=computer_4_queue.popleft,
        out_function=computer_5_queue.append,
    )
    while not computer_5_part_2.halted:
        computer_1_part_2.run_until_instruction(4)
        computer_2_part_2.run_until_instruction(4)
        computer_3_part_2.run_until_instruction(4)
        computer_4_part_2.run_until_instruction(4)
        computer_5_part_2.run_until_instruction(4)
    all_outs_p2.append(computer_1_queue[0])
print(max(all_outs_p2))
