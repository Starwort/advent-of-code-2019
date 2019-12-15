from intcode_computer_rewrite import Computer
from collections import defaultdict
import colorama as colour

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
colour.init()

map = defaultdict(lambda: -1)
data = "3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,1001,1034,0,1039,102,1,1036,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1105,1,124,1001,1034,0,1039,1001,1036,0,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1106,0,124,1001,1034,-1,1039,1008,1036,0,1041,101,0,1035,1040,101,0,1038,1043,1001,1037,0,1042,1105,1,124,1001,1034,1,1039,1008,1036,0,1041,102,1,1035,1040,102,1,1038,1043,102,1,1037,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,39,1032,1006,1032,165,1008,1040,1,1032,1006,1032,165,1102,1,2,1044,1105,1,224,2,1041,1043,1032,1006,1032,179,1101,1,0,1044,1105,1,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,53,1044,1105,1,224,1101,0,0,1044,1105,1,224,1006,1044,247,1002,1039,1,1034,1002,1040,1,1035,1001,1041,0,1036,1002,1043,1,1038,102,1,1042,1037,4,1044,1106,0,0,75,19,3,12,33,54,92,8,21,31,54,5,92,12,60,36,59,17,50,64,6,67,13,45,33,33,6,76,60,41,97,33,8,19,78,23,28,64,22,49,25,77,58,85,19,83,48,69,66,27,18,23,60,25,13,52,71,49,88,74,21,93,89,22,60,89,12,78,8,17,98,68,14,29,57,90,31,57,13,2,48,60,18,17,80,6,96,37,55,99,44,64,67,79,27,61,96,36,97,47,48,82,96,19,19,99,35,78,41,90,21,6,87,86,6,44,49,14,88,79,42,65,73,96,8,3,13,17,80,68,35,21,54,71,49,2,48,4,95,83,24,43,74,24,70,37,47,98,92,47,76,42,39,94,86,1,64,47,83,11,71,21,90,44,58,95,67,28,23,58,58,39,52,82,18,95,83,4,91,22,91,59,32,75,64,51,99,19,79,74,22,65,34,28,77,37,13,67,18,63,16,73,33,72,20,97,41,83,26,64,81,42,75,97,36,59,25,45,75,2,47,88,98,48,52,67,6,72,24,56,96,65,19,37,10,83,91,15,86,25,16,46,45,90,31,76,18,49,82,49,99,91,49,7,33,55,94,23,13,92,27,19,96,65,26,50,90,2,79,19,28,90,5,60,15,84,33,85,9,69,84,77,34,39,54,64,8,6,79,85,17,78,69,99,49,64,8,86,72,10,80,10,97,38,6,42,79,84,12,70,75,12,45,6,9,62,45,90,46,39,67,44,92,56,29,96,94,38,40,66,8,4,27,66,34,40,59,38,99,97,48,45,89,72,62,47,73,51,43,90,10,11,55,69,36,99,86,46,90,20,20,43,1,32,70,20,24,31,63,15,90,74,51,97,60,94,17,30,76,57,7,25,75,9,20,8,75,11,84,10,31,71,46,34,83,7,76,68,74,75,14,63,76,54,26,79,71,67,67,14,93,69,46,32,21,21,91,2,48,84,36,88,2,80,34,75,57,47,74,19,74,47,56,11,29,81,28,23,98,7,57,50,21,88,85,33,46,40,24,17,60,79,80,22,79,72,38,80,92,90,52,88,79,80,43,5,65,47,27,92,94,7,84,97,9,44,68,61,12,60,54,51,6,54,30,64,20,75,68,10,54,52,54,92,1,43,78,41,98,42,83,7,7,77,55,44,14,24,97,15,48,35,63,4,91,54,22,69,26,47,56,35,74,34,82,61,7,68,41,32,72,19,36,70,68,21,44,78,18,40,63,63,34,93,16,87,45,52,99,81,49,77,21,98,12,35,9,62,25,64,59,36,76,82,86,44,37,96,79,38,62,89,14,35,56,3,72,68,81,30,9,44,43,31,37,90,55,29,15,62,65,85,13,76,59,99,9,26,75,82,43,72,3,41,12,92,32,45,84,14,36,54,68,3,91,23,41,6,98,18,58,33,94,30,23,27,23,70,48,25,68,35,57,51,96,28,92,94,8,38,59,48,67,93,4,45,66,91,41,72,61,17,20,83,36,90,51,58,62,90,37,72,26,3,58,66,88,19,77,97,41,82,37,67,35,11,75,15,45,92,38,10,86,17,83,60,48,43,45,72,29,60,74,45,97,96,14,62,13,90,81,51,12,47,91,34,65,60,31,30,92,46,18,64,85,22,77,94,42,32,68,80,94,47,1,81,98,88,31,12,54,20,96,90,31,9,99,50,70,51,83,68,40,99,26,65,19,66,93,68,49,92,36,96,6,66,48,95,57,76,14,85,12,98,32,61,36,71,58,72,15,74,19,90,49,69,7,58,18,57,0,0,21,21,1,10,1,0,0,0,0,0,0"
location = [0, 0]
undo_history = []
direction = UP
backtracking = False


def fill_in_map(output):
    if output == 0:
        print("wall")
        x, y = location
        if direction == DOWN:
            y += 1
        if direction == UP:
            y -= 1
        if direction == RIGHT:
            x += 1
        if direction == LEFT:
            x -= 1
        map[x, y] = output
    else:
        if direction == DOWN:
            if not backtracking:
                undo_history.append(location.copy())
            location[1] += 1
        if direction == UP:
            if not backtracking:
                undo_history.append(location.copy())
            location[1] -= 1
        if direction == RIGHT:
            if not backtracking:
                undo_history.append(location.copy())
            location[0] += 1
        if direction == LEFT:
            if not backtracking:
                undo_history.append(location.copy())
            location[0] -= 1
        map[tuple(location)] = output
    if output == 2:
        print("found")
    print(colour.Cursor.POS())
    min_x = min(x for x, y in map.keys())
    max_x = max(x for x, y in map.keys())
    min_y = min(y for x, y in map.keys())
    max_y = max(y for x, y in map.keys())
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(
                ("# O."[map[x, y]] if not (x == y == 0) else "X")
                if not ([x, y] == location)
                else "D",
                end="",
            )
        print()
    # if output == 0:
    #     input()


def explore_map():
    global direction, backtracking
    backtracking = False
    if location == [5, -2]:
        print(
            map[location[0], location[1] + 1],
            map[location[0], location[1] - 1],
            map[location[0] + 1, location[1]],
            map[location[0] - 1, location[1]],
        )
    if map[location[0], location[1] + 1] == -1:
        direction = DOWN
        return DOWN
    if map[location[0], location[1] - 1] == -1:
        direction = UP
        return UP
    if map[location[0] + 1, location[1]] == -1:
        direction = RIGHT
        return RIGHT
    if map[location[0] - 1, location[1]] == -1:
        direction = LEFT
        return LEFT
    print("explored region", location)
    # print(undo_history)
    backtracking = True
    print(undo_history)
    new_target = undo_history.pop()
    # print(undo_history)
    if location in [[4, -2], [5, -2], [6, -2]]:
        input()
    dx = new_target[0] - location[0]
    dy = new_target[1] - location[1]
    # print(dx, dy)
    # print(new_target, location)
    direction = [[None, DOWN, UP], [RIGHT], [LEFT]][dx][dy]
    # if location == [6, -2]:
    #     new_target = [6, -1]
    #     direction = DOWN
    location[0] = new_target[0]
    location[1] = new_target[1]
    return direction


map[0, 0] = 1
# computer = Computer(
#     data, in_function=explore_map, out_function=fill_in_map, unsafe=True
# )
# computer.run_until_complete()
# print("filled map")
offset_map = defaultdict(lambda: -1)
offset = (0, 0)
with open("day15walls.txt") as file:
    for y, line in enumerate(file.read().splitlines()):
        for x, tile in enumerate(line):
            if tile == "S":
                offset = (x, y)
                tile = "."
            if tile == ".":
                _tile = 1
            if tile == "#":
                _tile = 0
            if tile == "*":
                _tile = 2
            if tile == " ":
                _tile = -1
            offset_map[x, y] = _tile
for (x, y), tile in offset_map.items():
    map[x - offset[0], y - offset[1]] = tile
map_search = defaultdict(lambda: -1)


def search_map(map_search, x, y, n, stop=True):
    if map[x, y] == 2 and stop:
        raise StopIteration
    if map_search[x - 1, y] == -1 and map[x - 1, y] > 0:
        map_search[x - 1, y] = n + 1
        search_map(map_search, x - 1, y, n + 1, stop)
    if map_search[x + 1, y] == -1 and map[x + 1, y] > 0:
        map_search[x + 1, y] = n + 1
        search_map(map_search, x + 1, y, n + 1, stop)
    if map_search[x, y - 1] == -1 and map[x, y - 1] > 0:
        map_search[x, y - 1] = n + 1
        search_map(map_search, x, y - 1, n + 1, stop)
    if map_search[x, y + 1] == -1 and map[x, y + 1] > 0:
        map_search[x, y + 1] = n + 1
        search_map(map_search, x, y + 1, n + 1, stop)


map_search[0, 0] = 0
try:
    search_map(map_search, 0, 0, 0)
except:
    pass
oxy_loc = [i for i, j in map.items() if j == 2][0]
x, y = oxy_loc
print(map_search[oxy_loc])


map_oxy = defaultdict(lambda: -1)
search_map(map_oxy, x, y, 0, False)
print(max(map_oxy.values()))

