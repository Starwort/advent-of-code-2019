from math import gcd, atan2, pi

map = """.#......##.#..#.......#####...#..
...#.....##......###....#.##.....
..#...#....#....#............###.
.....#......#.##......#.#..###.#.
#.#..........##.#.#...#.##.#.#.#.
..#.##.#...#.......#..##.......##
..#....#.....#..##.#..####.#.....
#.............#..#.........#.#...
........#.##..#..#..#.#.....#.#..
.........#...#..##......###.....#
##.#.###..#..#.#.....#.........#.
.#.###.##..##......#####..#..##..
.........#.......#.#......#......
..#...#...#...#.#....###.#.......
#..#.#....#...#.......#..#.#.##..
#.....##...#.###..#..#......#..##
...........#...#......#..#....#..
#.#.#......#....#..#.....##....##
..###...#.#.##..#...#.....#...#.#
.......#..##.#..#.............##.
..###........##.#................
###.#..#...#......###.#........#.
.......#....#.#.#..#..#....#..#..
.#...#..#...#......#....#.#..#...
#.#.........#.....#....#.#.#.....
.#....#......##.##....#........#.
....#..#..#...#..##.#.#......#.#.
..###.##.#.....#....#.#......#...
#.##...#............#..#.....#..#
.#....##....##...#......#........
...#...##...#.......#....##.#....
.#....#.#...#.#...##....#..##.#.#
.#.#....##.......#.....##.##.#.##""".splitlines()
width = height = len(map)


def get_line_of_sight(x, y):
    points = []
    for nx in range(x - 1, -1, -1):
        if map[y][nx] == "#":
            points.append((nx, y))
            break
    for nx in range(x + 1, width):
        if map[y][nx] == "#":
            points.append((nx, y))
            break
    for ny in range(y - 1, -1, -1):
        if map[ny][x] == "#":
            points.append((x, ny))
            break
    for ny in range(y + 1, width):
        if map[ny][x] == "#":
            points.append((x, ny))
            break

    for ox in range(-1, -width, -1):
        for oy in range(-1, -width, -1):
            if gcd(oy, ox) != 1:
                continue
            for oymult in [-1, 1]:
                for multiplier in range(1, width):
                    nx = x + ox * multiplier
                    ny = y + oy * multiplier * oymult
                    # print(nx, ny, ox, oy, oymult, multiplier)
                    if 0 <= nx < width and 0 <= ny < height:
                        if map[ny][nx] == "#":
                            points.append((nx, ny))
                            break

    for ox in range(1, width):
        for oy in range(1, width):
            if gcd(oy, ox) != 1:
                continue
            for oymult in [-1, 1]:
                for multiplier in range(1, width):
                    nx = x + ox * multiplier
                    ny = y + oy * multiplier * oymult
                    # print(nx, ny, ox, oy, oymult, multiplier)
                    if 0 <= nx < width and 0 <= ny < height:
                        if map[ny][nx] == "#":
                            points.append((nx, ny))
                            break

    return set(points)


tiles = {}
for y, row in enumerate(map):
    for x, tile in enumerate(row):
        if tile == "#":
            tiles[len(get_line_of_sight(x, y))] = x, y

key = max(tiles.keys())
print(key, tiles[key])

x, y = tiles[key]
asteroids = get_line_of_sight(x, y)

sorted_points = sorted(
    asteroids, key=lambda point: atan2(point[0] - x, y - point[1]) % (2 * pi)
)
point = sorted_points[199]
print(point[0] * 100 + point[1])
