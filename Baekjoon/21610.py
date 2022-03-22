N = 0
A = [[0]]

deltas = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


def solution():
    commands = get_input()
    cloud = [[N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]]

    for d, s in commands:
        move(cloud, d - 1, s)
        rain(cloud)
        water_copy_bug(cloud)
        cloud = create_cloud(cloud)

    water_sum = get_sum()
    print(water_sum)


def get_sum():
    return sum([sum(A[i]) for i in range(N)])


def get_input():
    global N, A
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    commands = [list(map(int, input().split())) for _ in range(M)]
    return commands


def move(cloud, d, s):
    for c in range(len(cloud)):
        for i in range(len(cloud[c])):
            cloud[c][i] += (deltas[d][i] * s) % N
            if cloud[c][i] < 0:
                cloud[c][i] = N + i
            elif cloud[c][i] >= N:
                cloud[c][i] = cloud[c][i] - N


def rain(cloud):
    for i, j in cloud:
        A[i][j] += 1


def water_copy_bug(cloud):
    will_increase = []

    for i, j in cloud:
        to_increase = 0

        for di, dj in diagonal:
            adj_i, adj_j = i + di, j + dj
            if 0 <= adj_i < N and 0 <= adj_j < N and A[adj_i][adj_j] > 0:
                to_increase += 1

        will_increase.append([i, j, to_increase])

    for [i, j, to_increase] in will_increase:
        A[i][j] += to_increase


def create_cloud(cloud):
    new_cloud = []
    prev_cloud = set()

    for cy, cx in cloud:
        prev_cloud.add((cy, cx))

    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and (i, j) not in prev_cloud:
                new_cloud.append([i, j])
                A[i][j] -= 2

    return new_cloud


solution()