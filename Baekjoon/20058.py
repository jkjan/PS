from collections import deque


N = 0
A = [[0]]
deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solution():
    Ls = get_input()

    for L in Ls:
        firestorm(L)
        decrease_ice()

    ice_sum = get_sum()
    max_cluster_size = get_max_cluster_size()

    print(ice_sum)
    print(max_cluster_size)


def get_input():
    global N, A
    N, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(2 ** N)]
    Ls = list(map(int, input().split()))
    return Ls


def firestorm(L):
    divided = get_divide(L)

    for [y, x] in divided:
        partial = []

        for i in range(2 ** L):
            partial.append([])
            for j in range(2 ** L):
                partial[i].append(A[y + i][x + j])

        rotate(partial)

        for i in range(2 ** L):
            for j in range(2 ** L):
                A[y + i][x + j] = partial[i][j]


def decrease_ice():
    to_decrease = []

    for i in range(2 ** N):
        for j in range(2 ** N):
            adj_cnt = 0

            for dy, dx in deltas:
                adj_y, adj_x = i + dy, j + dx
                if is_valid(adj_y, adj_x) and A[adj_y][adj_x] > 0:
                    adj_cnt += 1

            if adj_cnt < 3:
                to_decrease.append([i, j])

    for [i, j] in to_decrease:
        if A[i][j] > 0:
            A[i][j] -= 1


def get_max_cluster_size():
    visited = [[False for _ in range(2 ** N)] for _ in range(2 ** N)]
    max_cluster_size = 0

    for i in range(2 ** N):
        for j in range(2 ** N):
            if not visited[i][j] and A[i][j] != 0:
                visited[i][j] = True
                cluster_size = bfs(i, j, visited)
                max_cluster_size = max(max_cluster_size, cluster_size)

    return max_cluster_size


def bfs(s_y, s_x, visited):
    will_visit = deque([(s_y, s_x)])
    cluster_size = 0

    while len(will_visit) > 0:
        now_y, now_x = will_visit.popleft()
        cluster_size += 1

        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx
            if not is_valid(adj_y, adj_x):
                continue
            if visited[adj_y][adj_x]:
                continue
            if A[adj_y][adj_x] == 0:
                continue

            will_visit.append((adj_y, adj_x))
            visited[adj_y][adj_x] = True

    return cluster_size


def is_valid(i, j):
    return 0 <= i < 2 ** N and 0 <= j < 2 ** N


def get_sum():
    ice_sum = 0

    for i in range(2 ** N):
        for j in range(2 ** N):
            ice_sum += A[i][j]

    return ice_sum


def get_divide(L):
    divided = []

    for i in range(0, 2 ** N, 2 ** L):
        for j in range(0, 2 ** N, 2 ** L):
            divided.append([i, j])

    return divided


def rotate(partial):
    rotated = [[0 for _ in range(len(partial[0]))] for _ in range(len(partial))]

    for i in range(len(partial)):
        for j in range(len(partial[0])):
            rotated[j][len(partial) - 1 - i] = partial[i][j]

    for i in range(len(partial)):
        for j in range(len(partial[0])):
            partial[i][j] = rotated[i][j]


solution()