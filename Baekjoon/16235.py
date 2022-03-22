import time
from collections import deque


N = M = K = 0
A = []
soil = [[1, []]]
deltas = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

NUTRITION = 0
TREES = 1


def solution():
    get_input()

    for year in range(K):
        spring()
        # summer()
        autumn()
        winter()

    return get_survived_trees()


def get_input():
    global N, M, K, A, soil
    N, M, K = map(int, input().split())
    soil = [[[5, []] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        A.append(list(map(int, input().split())))

    for i in range(M):
        x, y, z = map(int, input().split())
        soil[x-1][y-1][TREES].append(z)


def spring():
    for i in range(N):
        for j in range(N):
            for k in range(len(soil[i][j][TREES]) - 1, -1, -1):
                age = soil[i][j][TREES][k]

                if soil[i][j][NUTRITION] >= age:
                    soil[i][j][NUTRITION] -= age
                    soil[i][j][TREES][k] += 1
                else:
                    dead_trees = soil[i][j][TREES][:k+1]
                    for dead in dead_trees:
                        soil[i][j][NUTRITION] += (dead // 2)
                    soil[i][j][TREES] = soil[i][j][TREES][k+1:]
                    break


# def summer():
#     for y, x, age in dead_trees:
#         soil[y][x][NUTRITION] += (age // 2)


def autumn():
    for i in range(N):
        for j in range(N):
            valid_adj = get_valid_adj(i, j)

            for age in soil[i][j][TREES]:
                if age > 0 and age % 5 == 0:
                    for adj_y, adj_x in valid_adj:
                        soil[adj_y][adj_x][TREES].append(1)


def winter():
    for i in range(N):
        for j in range(N):
            soil[i][j][NUTRITION] += A[i][j]


def get_valid_adj(i, j):
    valid_adj = []

    for dy, dx in deltas:
        adj_y, adj_x = i + dy, j + dx
        if is_valid(adj_y, adj_x):
            valid_adj.append((adj_y, adj_x))

    return valid_adj


def is_valid(i, j):
    return 0 <= i < N and 0 <= j < N


def get_survived_trees():
    cnt = 0

    for i in range(N):
        for j in range(N):
            cnt += len(soil[i][j][TREES])

    return cnt


answer = solution()
print(answer)