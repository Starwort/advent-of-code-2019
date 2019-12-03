import random
from functools import lru_cache
import typing


def generate_input(
    lower_bound: int, upper_bound: int, quantity: int
) -> typing.Tuple[typing.List[int], typing.Tuple[int, int]]:
    rv = []
    for _ in range(5):
        rv.append(random.randint(lower_bound, lower_bound + 10))
        rv.append(random.randint(upper_bound - 10, upper_bound))
    for _ in range(quantity - 10):
        rv.append(random.randint(lower_bound, upper_bound))
    rv = rv[:quantity]
    for _ in range(7):
        random.shuffle(rv)
    print("generated input, solving")
    return rv, solve(rv)


@lru_cache()
def get_fuel(mass: int) -> int:
    rv = mass // 3 - 2
    if rv < 0:
        rv = 0
    if rv:
        rv += get_fuel(rv)
    return rv


def solve(ints: typing.List[int]) -> typing.Tuple[int, int]:
    return sum([max(i // 3 - 2, 0) for i in ints]), sum([get_fuel(i) for i in ints])


if __name__ == "__main__":
    input = generate_input(0, 100000000000000000, 10000000)
    with open("upping_the_ante_input.txt", "w") as file:
        file.write("\n".join(map(str, input[0])))
    with open("upping_the_ante_solutions.txt", "w") as file:
        file.write("Part 1: {}\nPart 2: {}".format(*input[1]))

