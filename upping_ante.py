with open("upping_the_ante_input.txt") as file:
    data = file.read()

ints = [int(i) for i in data.splitlines()]


def get_fuel(mass):
    rv = mass // 3 - 2
    if rv < 0:
        rv = 0
    if rv:
        rv += get_fuel(rv)
    return rv


# fmt: off
# print(sum([i // 3 - 2 for i in ints])) or ((get_fuel_1l := lambda mass: ((rv := max(mass//3-2, 0)) + (get_fuel_1l(rv) if rv else 0))) and print(sum([get_fuel_1l(i) for i in ints])))
# # print(sum([i // 3 - 2 for i in [int(i) for i in '<snip>'.splitlines()]])) or ((get_fuel_1l := lambda mass: ((rv := max(mass//3-2, 0)) + (get_fuel_1l(rv) if rv else 0))) and print(sum([get_fuel_1l(i) for i in [int(i) for i in '<snip>'.splitlines()]])))
# # fmt: on
# print(sum([i // 3 - 2 for i in ints])) or (
#     (
#         get_fuel_1l := lambda mass: (
#             (rv := max(mass // 3 - 2, 0)) + (get_fuel_1l(rv) if rv else 0)
#         )
#     )
#     and print(sum([get_fuel_1l(i) for i in ints]))
# )

print(sum([i // 3 - 2 for i in ints]))
print(sum([get_fuel(i) for i in ints]))
