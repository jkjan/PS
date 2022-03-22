deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution():
    T = get_input()
    init()

    indices = get_indices()

    for t in range(T):
        spread()
        run_purifier(indices)

    answer = get_sum() + 2
    print(answer)


def get_input():
    global R, C, house
    R, C, T = map(int, input().split())
    house = [list(map(int, input().split())) for _ in range(R)]
    return T


def init():
    global purifier
    purifier = []
    for i in range(R):
        for j in range(C):
            if house[i][j] == -1:
                purifier.append((i, j))


def spread():
    to_add = []

    for i in range(R):
        for j in range(C):
            if house[i][j] <= 0:
                continue
            cnt = 0

            for dy, dx in deltas:
                adj_y, adj_x = i + dy, j + dx

                if is_valid(adj_y, adj_x) and (adj_y, adj_x) not in purifier:
                    cnt += 1
                    to_add.append([adj_y, adj_x, house[i][j] // 5])

            house[i][j] -= ((house[i][j] // 5) * cnt)

    for [y, x, dust] in to_add:
        house[y][x] += dust


def is_valid(i, j):
    return 0 <= i < R and 0 <= j < C


def run_purifier(indices):
    for idc in indices:
        rotate(idc)


def rotate(indices):
    q = []

    for y, x in indices[:-1]:
        q.append(house[y][x])

    for e, (y, x) in enumerate(indices[1:]):
        house[y][x] = q[e]

    y, x = indices[0]
    house[y][x] = 0


def get_indices():
    upper_r = purifier[0][0]
    lower_r = upper_r + 1
    upper_indices = []
    lower_indices = []

    for i in range(1, C):
        upper_indices.append((upper_r, i))
    for i in range(upper_r - 1, -1, -1):
        upper_indices.append((i, C-1))
    for i in range(C-2, -1, -1):
        upper_indices.append((0, i))
    for i in range(1, upper_r):
        upper_indices.append((i, 0))

    for i in range(1, C):
        lower_indices.append((lower_r, i))
    for i in range(lower_r + 1, R):
        lower_indices.append((i, C-1))
    for i in range(C-2, -1, -1):
        lower_indices.append((R-1, i))
    for i in range(R-2, lower_r, -1):
        lower_indices.append((i, 0))

    return [upper_indices, lower_indices]


def get_sum():
    dust_sum = 0
    for i in range(R):
        dust_sum += sum(house[i])
    return dust_sum


solution()