from intcode_computer_rewrite import Computer
from collections import defaultdict

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

PRETTY_PRINT_MAP = False

try:
    import colorama as colour  # type: ignore

    colour.init(autoreset=True)
    empty = colour.Back.BLACK + "　"
    wall = colour.Back.WHITE + "　"
    oxy = colour.Back.LIGHTBLUE_EX + "O\u2082"
    start = colour.Back.GREEN + "Ｓ"
    droid = colour.Back.RED + "Ｄ"
    unexplored = colour.Back.LIGHTBLACK_EX + "　"
    cursor_pos = colour.Cursor.POS()
except:
    empty = "　"
    wall = "██"
    unexplored = "░░"
    oxy = "O\u2082"
    start = "Ｓ"
    droid = "Ｄ"
    cursor_pos = ""

map = defaultdict(lambda: -1)  # type: ignore
data = "3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,1001,1034,0,1039,102,1,1036,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1105,1,124,1001,1034,0,1039,1001,1036,0,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1106,0,124,1001,1034,-1,1039,1008,1036,0,1041,101,0,1035,1040,101,0,1038,1043,1001,1037,0,1042,1105,1,124,1001,1034,1,1039,1008,1036,0,1041,102,1,1035,1040,102,1,1038,1043,102,1,1037,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,39,1032,1006,1032,165,1008,1040,1,1032,1006,1032,165,1102,1,2,1044,1105,1,224,2,1041,1043,1032,1006,1032,179,1101,1,0,1044,1105,1,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,53,1044,1105,1,224,1101,0,0,1044,1105,1,224,1006,1044,247,1002,1039,1,1034,1002,1040,1,1035,1001,1041,0,1036,1002,1043,1,1038,102,1,1042,1037,4,1044,1106,0,0,75,19,3,12,33,54,92,8,21,31,54,5,92,12,60,36,59,17,50,64,6,67,13,45,33,33,6,76,60,41,97,33,8,19,78,23,28,64,22,49,25,77,58,85,19,83,48,69,66,27,18,23,60,25,13,52,71,49,88,74,21,93,89,22,60,89,12,78,8,17,98,68,14,29,57,90,31,57,13,2,48,60,18,17,80,6,96,37,55,99,44,64,67,79,27,61,96,36,97,47,48,82,96,19,19,99,35,78,41,90,21,6,87,86,6,44,49,14,88,79,42,65,73,96,8,3,13,17,80,68,35,21,54,71,49,2,48,4,95,83,24,43,74,24,70,37,47,98,92,47,76,42,39,94,86,1,64,47,83,11,71,21,90,44,58,95,67,28,23,58,58,39,52,82,18,95,83,4,91,22,91,59,32,75,64,51,99,19,79,74,22,65,34,28,77,37,13,67,18,63,16,73,33,72,20,97,41,83,26,64,81,42,75,97,36,59,25,45,75,2,47,88,98,48,52,67,6,72,24,56,96,65,19,37,10,83,91,15,86,25,16,46,45,90,31,76,18,49,82,49,99,91,49,7,33,55,94,23,13,92,27,19,96,65,26,50,90,2,79,19,28,90,5,60,15,84,33,85,9,69,84,77,34,39,54,64,8,6,79,85,17,78,69,99,49,64,8,86,72,10,80,10,97,38,6,42,79,84,12,70,75,12,45,6,9,62,45,90,46,39,67,44,92,56,29,96,94,38,40,66,8,4,27,66,34,40,59,38,99,97,48,45,89,72,62,47,73,51,43,90,10,11,55,69,36,99,86,46,90,20,20,43,1,32,70,20,24,31,63,15,90,74,51,97,60,94,17,30,76,57,7,25,75,9,20,8,75,11,84,10,31,71,46,34,83,7,76,68,74,75,14,63,76,54,26,79,71,67,67,14,93,69,46,32,21,21,91,2,48,84,36,88,2,80,34,75,57,47,74,19,74,47,56,11,29,81,28,23,98,7,57,50,21,88,85,33,46,40,24,17,60,79,80,22,79,72,38,80,92,90,52,88,79,80,43,5,65,47,27,92,94,7,84,97,9,44,68,61,12,60,54,51,6,54,30,64,20,75,68,10,54,52,54,92,1,43,78,41,98,42,83,7,7,77,55,44,14,24,97,15,48,35,63,4,91,54,22,69,26,47,56,35,74,34,82,61,7,68,41,32,72,19,36,70,68,21,44,78,18,40,63,63,34,93,16,87,45,52,99,81,49,77,21,98,12,35,9,62,25,64,59,36,76,82,86,44,37,96,79,38,62,89,14,35,56,3,72,68,81,30,9,44,43,31,37,90,55,29,15,62,65,85,13,76,59,99,9,26,75,82,43,72,3,41,12,92,32,45,84,14,36,54,68,3,91,23,41,6,98,18,58,33,94,30,23,27,23,70,48,25,68,35,57,51,96,28,92,94,8,38,59,48,67,93,4,45,66,91,41,72,61,17,20,83,36,90,51,58,62,90,37,72,26,3,58,66,88,19,77,97,41,82,37,67,35,11,75,15,45,92,38,10,86,17,83,60,48,43,45,72,29,60,74,45,97,96,14,62,13,90,81,51,12,47,91,34,65,60,31,30,92,46,18,64,85,22,77,94,42,32,68,80,94,47,1,81,98,88,31,12,54,20,96,90,31,9,99,50,70,51,83,68,40,99,26,65,19,66,93,68,49,92,36,96,6,66,48,95,57,76,14,85,12,98,32,61,36,71,58,72,15,74,19,90,49,69,7,58,18,57,0,0,21,21,1,10,1,0,0,0,0,0,0"

x = 0  # current position of robot
y = 0
min_x = 0  # bounds of the map
max_x = 0
min_y = 0
max_y = 0
d = UP  # current direction of the robot
last_out = None  # most recent output value from the robot
stack = []  # stack of visited positions which still need exploring

# All the AI is in the input function.  The output function just
# stores the value for later.
def output_fn(val):
    global last_out
    last_out = val


# Provisionally move the robot in the given direction; return the new position
def move(dd):
    global min_x, max_x, min_y, max_y
    x1 = x
    y1 = y
    if dd == UP:
        y1 -= 1
    elif dd == DOWN:
        y1 += 1
    elif dd == LEFT:
        x1 -= 1
    elif dd == RIGHT:
        x1 += 1
    else:
        raise ValueError("Invalid direction")
    if x1 < min_x:
        min_x = x1
    if x1 > max_x:
        max_x = x1
    if y1 < min_y:
        min_y = y1
    if y1 > max_y:
        max_y = y1
    return (x1, y1)


# All the map exploring AI lives here
def input_fn():
    global x, y, d
    # First input of the run, just start with UP
    if last_out is None:
        d = UP
        return d
    # Move in the last-given direction
    (x1, y1) = move(d)
    if map[x1, y1] == -1:
        # New location explored so fill in the map
        map[x1, y1] = last_out
        # also if we moved remember the old location for further exploration
        if last_out != 0:
            stack.append((x, y))
    # update the robot's position if it didn't hit a wall
    if last_out != 0:
        x = x1
        y = y1
    # decide where to explore next
    new_d = None
    if map[x, y - 1] == -1:
        new_d = UP
    elif map[x + 1, y] == -1:
        new_d = RIGHT
    elif map[x - 1, y] == -1:
        new_d = LEFT
    elif map[x, y + 1] == -1:
        new_d = DOWN
    if new_d is not None:
        d = new_d
        return d
    # no location left to explore, so backtrack through saved positions
    while len(stack) > 0:
        (x2, y2) = stack.pop()
        # calculate which direction to move in to backtrack to this location
        if y2 < y:
            d = UP
        elif y2 > y:
            d = DOWN
        elif x2 < x:
            d = LEFT
        elif x2 > x:
            d = RIGHT
        else:
            continue
        # sanity-check the move and then return it
        if move(d) != (x2, y2):
            raise AssertionError(
                "Backtrack error from "
                + str(x)
                + ","
                + str(y)
                + " to "
                + str(x2)
                + ","
                + str(y2)
            )
        return d
    # If we got here, the stack is empty; map has been explored
    # returning a non-direction makes the computer halt
    return 0


computer = Computer(data, in_function=input_fn, out_function=output_fn)
computer.run_until_complete()

print(cursor_pos)

if PRETTY_PRINT_MAP:
    for row in range(min_y, max_y + 1):
        print(
            "".join(
                (
                    [wall, empty, oxy, unexplored][map[col, row]]
                    if not (col == row == 0)
                    else start
                )
                if not ([x, y] == [col, row])
                else droid
                for col in range(min_x, max_x + 1)
            )
        )

map_search = defaultdict(lambda: -1)  # type: ignore


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


map_oxy = defaultdict(lambda: -1)  # type: ignore
search_map(map_oxy, x, y, 0, False)

print(max(map_oxy.values()))

