grid = [
    [int(i == "#") for i in j]
    for j in """#..#.
#.#.#
...#.
....#
#.#.#""".splitlines()
]
previous_grids = set()
while True:
    rating = 0
    for y in range(5):
        for x in range(5):
            rating += grid[y][x] * 2 ** (y * 5 + x)
    # print(rating)
    # print("\n".join("".join(".#"[i] for i in row) for row in grid))
    if rating in previous_grids:
        print(rating)
        break
    previous_grids.add(rating)

    def get_surrounding(x, y):
        surrounding = []
        try:
            assert y > 0
            surrounding.append(grid[y - 1][x])
        except:
            pass
        try:
            surrounding.append(grid[y + 1][x])
        except:
            pass
        try:
            assert x > 0
            surrounding.append(grid[y][x - 1])
        except:
            pass
        try:
            surrounding.append(grid[y][x + 1])
        except:
            pass
        # print(sum(surrounding), end="" if x != 4 else "\n")
        return surrounding

    next_grid = [
        [
            (1 if sum(get_surrounding(x, y)) == 1 else 0)
            if grid[y][x] == 1
            else (1 if sum(get_surrounding(x, y)) in {1, 2} else 0)
            for x in range(5)
        ]
        for y in range(5)
    ]
    grid = next_grid
layers = [
    [[0 for i in range(5)] for i in range(5)],
    [
        [int(i == "#") for i in j]
        for j in """#..#.
#.#.#
...#.
....#
#.#.#""".splitlines()
    ],
    [[0 for i in range(5)] for i in range(5)],
]
for i in range(200):

    def get_surrounding_2(x, y, layer):
        surrounding = []
        try:
            if y > 0:
                surrounding.append(layers[layer][y - 1][x])
            else:
                if layer != 0:
                    surrounding.append(layers[layer - 1][1][2])
        except:
            pass
        try:
            if y < 4:
                surrounding.append(layers[layer][y + 1][x])
            else:
                if layer != 0:
                    surrounding.append(layers[layer - 1][3][2])
        except:
            pass
        try:
            if x > 0:
                surrounding.append(layers[layer][y][x - 1])
            else:
                if layer != 0:
                    surrounding.append(layers[layer - 1][2][1])
        except:
            pass
        try:
            if x < 4:
                surrounding.append(layers[layer][y][x + 1])
            else:
                if layer != 0:
                    surrounding.append(layers[layer - 1][2][3])
        except:
            pass
        if x == y == 2:
            return []
        if layer != len(layers) - 1:
            if (x, y) == (2, 1):
                surrounding.extend(layers[layer + 1][0])
            if (x, y) == (2, 3):
                surrounding.extend(layers[layer + 1][-1])
            if (x, y) == (1, 2):
                surrounding.extend(i[0] for i in layers[layer + 1])
            if (x, y) == (3, 2):
                surrounding.extend(i[-1] for i in layers[layer + 1])
        # print(sum(surrounding), end="" if x != 4 else "\n")
        return surrounding

    layers_len = len(layers)
    next_layers = [[[0 for i in range(5)] for i in range(5)]]
    for i in range(layers_len):
        layer = layers[i]
        next_grid = [
            [
                (1 if sum(get_surrounding_2(x, y, i)) == 1 else 0)
                if layer[y][x] == 1
                else (1 if sum(get_surrounding_2(x, y, i)) in {1, 2} else 0)
                for x in range(5)
            ]
            for y in range(5)
        ]
        next_layers.append(next_grid)
    next_layers.append([[0 for i in range(5)] for i in range(5)])
    layers = next_layers
print(sum(sum(sum(row) for row in layer) for layer in layers))
