N = 0
field = [[0]]
deltas = [[0, -1], [1, 0], [0, 1], [-1, 0]]
to_rotate = {(x, y): i for i, (x, y) in enumerate(deltas)}
spread_rate = [
                               [-2, 0, 0.02],
                [-1, -1, 0.1], [-1, 0, 0.07], [-1, 1, 0.01],
    [0, -2, 0.05],
                [1, -1, 0.1],  [1, 0, 0.07],  [1, 1, 0.01],
                               [2, 0, 0.02],

    [0, -1, 0]
]
outsider = 0


def solution():
    get_input()
    tornado()
    print(outsider)


def get_input():
    global N, field
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]


def get_directions():
    directions = []

    for i in range(1, N):
        directions += [[i], [i]]

    for i in range(0, len(directions), 4):
        for j in range(4):
            directions[i + j].append(deltas[j])

    return directions


def tornado():
    directions = get_directions()
    i = j = N // 2

    for [n, [dy, dx]] in directions:
        for _ in range(n):
            i += dy
            j += dx
            spread(i, j, dy, dx)

    for j in range(N-1, -1, -1):
        spread(0, j, 0, -1)


def spread(i, j, dy, dx):
    global outsider
    to_spread = []
    n_rotate = to_rotate[(dy, dx)]
    y_sand = field[i][j]

    for [sy, sx, sr] in spread_rate:
        for n in range(n_rotate):
            sy, sx = -sx, sy

        adj_y, adj_x = i + sy, j + sx

        if sr != 0:
            spread_sand = int(field[i][j] * sr)
            to_spread.append([adj_y, adj_x, spread_sand])
            y_sand -= spread_sand
        else:
            to_spread.append([adj_y, adj_x, y_sand])

    for [adj_y, adj_x, sand] in to_spread:
        if 0 <= adj_y < N and 0 <= adj_x < N:
            field[adj_y][adj_x] += sand
        else:
            outsider += sand

    field[i][j] = 0


solution()