import math
from heapq import heappop, heappush


def tc():
    T = int(input())

    for t in range(T):
        answer = dijkstra(*get_input())
        print("#%d %d" % (t + 1, answer))


def get_input():
    N = int(input())
    field = [list(map(int, list(input()))) for _ in range(N)]
    return N, field


def dijkstra(N, field):
    dist = [[math.inf for _ in range(N)] for _ in range(N)]
    dist[0][0] = 0
    dist_q = []
    heappush(dist_q, [0, 0, 0])
    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while len(dist_q) > 0:
        [from_s, now_y, now_x] = heappop(dist_q)

        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx

            if not is_valid(N, adj_y, adj_x):
                continue

            new_dist = from_s + field[adj_y][adj_x]
            if dist[adj_y][adj_x] > new_dist:
                dist[adj_y][adj_x] = new_dist
                heappush(dist_q, [new_dist, adj_y, adj_x])

    return dist[N - 1][N - 1]


def is_valid(N, i, j):
    return 0 <= i < N and 0 <= j < N


tc()