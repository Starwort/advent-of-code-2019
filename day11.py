from intcode_computer_rewrite import Computer
from collections import defaultdict
from itertools import zip_longest

robodir = 0  # up
roboloc = 0, 0
panels = defaultdict(int)  # type: ignore
turn_this_out = False
painted = set()


def handle_out(out):
    global roboloc, turn_this_out, robodir
    if not turn_this_out:
        panels[roboloc] = out
        painted.add(roboloc)
        turn_this_out = True
    else:
        robodir -= (-1) ** out
        robodir %= 4
        if robodir == 0:
            roboloc = (roboloc[0], roboloc[1] - 1)
        if robodir == 1:
            roboloc = (roboloc[0] + 1, roboloc[1])
        if robodir == 2:
            roboloc = (roboloc[0], roboloc[1] + 1)
        if robodir == 3:
            roboloc = (roboloc[0] - 1, roboloc[1])
        turn_this_out = False


def handle_in():
    return panels[roboloc]


data = "3,8,1005,8,336,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,28,1006,0,36,1,2,5,10,1006,0,57,1006,0,68,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,63,2,6,20,10,1,106,7,10,2,9,0,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,97,1006,0,71,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,122,2,105,20,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,148,2,1101,12,10,1006,0,65,2,1001,19,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,181,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1002,8,1,204,2,7,14,10,2,1005,20,10,1006,0,19,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,236,1006,0,76,1006,0,28,1,1003,10,10,1006,0,72,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,271,1006,0,70,2,107,20,10,1006,0,81,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,303,2,3,11,10,2,9,1,10,2,1107,1,10,101,1,9,9,1007,9,913,10,1005,10,15,99,109,658,104,0,104,1,21101,0,387508441896,1,21102,1,353,0,1106,0,457,21101,0,937151013780,1,21101,0,364,0,1105,1,457,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,179490040923,1,1,21102,411,1,0,1105,1,457,21101,46211964123,0,1,21102,422,1,0,1106,0,457,3,10,104,0,104,0,3,10,104,0,104,0,21101,838324716308,0,1,21101,0,445,0,1106,0,457,21102,1,868410610452,1,21102,1,456,0,1106,0,457,99,109,2,22101,0,-1,1,21101,40,0,2,21101,0,488,3,21101,478,0,0,1106,0,521,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,483,484,499,4,0,1001,483,1,483,108,4,483,10,1006,10,515,1101,0,0,483,109,-2,2105,1,0,0,109,4,2101,0,-1,520,1207,-3,0,10,1006,10,538,21101,0,0,-3,22102,1,-3,1,21202,-2,1,2,21101,0,1,3,21101,557,0,0,1105,1,562,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,585,2207,-4,-2,10,1006,10,585,22101,0,-4,-4,1106,0,653,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,604,1,0,1106,0,562,21202,1,1,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,623,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,645,21202,-1,1,1,21101,0,645,0,106,0,520,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0"

comp = Computer(data, in_function=handle_in, out_function=handle_out)
comp.run_until_complete()

print(len(painted))

# reset and run part 2

robodir = 0  # up
roboloc = 0, 0
panels = defaultdict(int)  # type: ignore
turn_this_out = False
painted = set()

panels[0, 0] = 1

comp = Computer(data, in_function=handle_in, out_function=handle_out)
comp.run_until_complete()

min_x = min(i[0] for i in panels.keys())
max_x = max(i[0] for i in panels.keys())
min_y = min(i[1] for i in panels.keys())
max_y = max(i[1] for i in panels.keys())


def group(iterable, n):
    return zip_longest(*[iter(iterable)] * n, fillvalue=0)


def quad_to_char(tl: int, tr: int, bl: int, br: int) -> str:
    char = {
        0: {
            0: {0: {0: " ", 1: "▗"}, 1: {0: "▖", 1: "▄"}},
            1: {0: {0: "▝", 1: "▐"}, 1: {0: "▞", 1: "▟"}},
        },
        1: {
            0: {0: {0: "▘", 1: "▚"}, 1: {0: "▌", 1: "▙"}},
            1: {0: {0: "▀", 1: "▜"}, 1: {0: "▛", 1: "█"}},
        },
    }
    try:
        return char[tl][tr][bl][br]
    except:
        print(tl, tr, bl, br)
        raise


try:
    import colorama as colour  # type: ignore

    colour.init(autoreset=True)
    line_start = colour.Fore.WHITE + colour.Back.BLACK
    # black = colour.Back.BLACK + "  "
    # white = colour.Back.WHITE + "  "
except ImportError:
    line_start = ""
    # black = "  "
    # white = "██"
    pass

for y1 in range(min_y, max_y + 1, 2):
    y2 = y1 + 1
    for x1 in range(min_x, max_x + 1, 2):
        x2 = x1 + 1
        print(
            line_start
            + quad_to_char(
                panels[x1, y1], panels[x2, y1], panels[x1, y2], panels[x2, y2]
            ),
            end="",
        )
    print()
