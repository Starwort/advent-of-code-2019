data = """<x=-1, y=7, z=3>
<x=12, y=2, z=-13>
<x=14, y=18, z=-8>
<x=17, y=4, z=-4>""".splitlines()
from itertools import combinations
import re

pattern = re.compile(r"<x=(\-?\d+), y=(\-?\d+), z=(\-?\d+)>")

# moons = [
#     [[-1, 7, 3], [0, 0, 0]],
#     [[12, 2, -13], [0, 0, 0]],
#     [[14, 18, -8], [0, 0, 0]],
#     [[17, 4, 4], [0, 0, 0]],
# ]
# moons = [
#     [[-8, -10, 0], [0, 0, 0]],
#     [[5, 5, 10], [0, 0, 0]],
#     [[2, -7, 3], [0, 0, 0]],
#     [[9, -8, -3], [0, 0, 0]],
# ]
moons = [
    [
        [
            int((match := pattern.match(i)).group(1)),
            int(match.group(2)),
            int(match.group(3)),
        ],
        [0, 0, 0],
    ]
    for i in data
]
x_states = set()
y_states = set()
z_states = set()
x_loop = -1
y_loop = -1
z_loop = -1
step = 0
x_state = (
    moons[0][0][0],
    moons[1][0][0],
    moons[2][0][0],
    moons[0][1][0],
    moons[1][1][0],
    moons[2][1][0],
)
y_state = (
    moons[0][0][1],
    moons[1][0][1],
    moons[2][0][1],
    moons[0][1][1],
    moons[1][1][1],
    moons[2][1][1],
)
z_state = (
    moons[0][0][2],
    moons[1][0][2],
    moons[2][0][2],
    moons[0][1][2],
    moons[1][1][2],
    moons[2][1][2],
)
while -1 in [x_loop, y_loop, z_loop]:
    if x_state in x_states and x_loop == -1:
        x_loop = step
    else:
        x_states.add(x_state)
    if y_state in y_states and y_loop == -1:
        y_loop = step
    else:
        y_states.add(y_state)
    if z_state in z_states and z_loop == -1:
        z_loop = step
    else:
        z_states.add(z_state)
    # if step % 10 == 0:
    #     print(step)
    #     for moon in moons:
    #         print(moon)
    for moon, moon2 in combinations(moons, 2):
        x1, y1, z1 = moon[0]
        x2, y2, z2 = moon2[0]
        if x1 > x2:
            moon[1][0] -= 1
            moon2[1][0] += 1
        if x1 < x2:
            moon[1][0] += 1
            moon2[1][0] -= 1
        if y1 > y2:
            moon[1][1] -= 1
            moon2[1][1] += 1
        if y1 < y2:
            moon[1][1] += 1
            moon2[1][1] -= 1
        if z1 > z2:
            moon[1][2] -= 1
            moon2[1][2] += 1
        if z1 < z2:
            moon[1][2] += 1
            moon2[1][2] -= 1
    for moon in moons:
        moon[0][0] += moon[1][0]
        moon[0][1] += moon[1][1]
        moon[0][2] += moon[1][2]
    step += 1
    if step == 1000:
        print(sum(sum(abs(i) for i in j[0]) * sum(abs(i) for i in j[1]) for j in moons))

    x_state = (
        moons[0][0][0],
        moons[1][0][0],
        moons[2][0][0],
        moons[0][1][0],
        moons[1][1][0],
        moons[2][1][0],
    )
    y_state = (
        moons[0][0][1],
        moons[1][0][1],
        moons[2][0][1],
        moons[0][1][1],
        moons[1][1][1],
        moons[2][1][1],
    )
    z_state = (
        moons[0][0][2],
        moons[1][0][2],
        moons[2][0][2],
        moons[0][1][2],
        moons[1][1][2],
        moons[2][1][2],
    )
from math import gcd


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)


print(lcm(lcm(x_loop, y_loop), z_loop))
