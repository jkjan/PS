import random
from collections import deque


deltas =  [(-1, 0), (1, 0), (0, -1), (0, 1)]
score = 0


def solution():
    commands = get_input()

    directions = get_directions()
    graph = get_graph(directions)

    for [d, s] in commands:
        blizzard(d-1, s)

        while True:
            move(directions)
            clusters = get_all_clusters(graph, directions, lambda x: len(x) >= 4)

            if len(clusters) == 0:
                break
            else:
                explode_clusters(clusters)

        clusters = get_all_clusters(graph, directions)
        transform_clusters(clusters, directions)

    print(score)


def print_biz():
    for i in range(N):
        for j in range(N):
            print(biz[i][j], end=' ')
        print()


def get_input():
    global N, biz, start
    N, M = map(int, input().split())
    biz = [list(map(int, input().split())) for _ in range(N)]
    commands = [list(map(int, input().split())) for _ in range(M)]
    start = (N//2, N//2)
    return commands


def get_directions():
    directions = [[1, (1, 0)]]
    directions_delta = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    for n in range(2, N):
        directions += [[n], [n]]

    for i in range(1, len(directions), 4):
        for j in range(4):
            if i + j < len(directions):
                directions[i + j].append(directions_delta[j])

    directions.append([N-1, (0, -1)])
    return directions


def get_graph(directions):
    graph = [[[] for _ in range(N)] for _ in range(N)]
    y, x = start
    x -= 1

    for [n, (dy, dx)] in directions:
        for i in range(n):
            adj_y, adj_x = y + dy, x + dx
            graph[adj_y][adj_x].append((y, x))
            graph[y][x].append((adj_y, adj_x))
            y, x = adj_y, adj_x

    return graph


def move(directions):
    not_destroyed = []
    y, x = start
    x -= 1

    if biz[y][x] != 0:
        not_destroyed.append(biz[y][x])

    for [n, (dy, dx)] in directions:
        for i in range(n):
            y, x = y + dy, x + dx
            if biz[y][x] != 0:
                not_destroyed.append(biz[y][x])

    refill_biz(directions, not_destroyed)


def refill_biz(directions, to_fill):
    if len(to_fill) == 0:
        return

    y, x = start
    x -= 1
    biz[y][x] = to_fill[0]
    nd = 1

    for [n, (dy, dx)] in directions:
        for i in range(n):
            y, x = y + dy, x + dx

            if nd < len(to_fill):
                biz[y][x] = to_fill[nd]
                nd += 1
            else:
                biz[y][x] = 0


def blizzard(d, s):
    y, x = start
    dy, dx = deltas[d]

    for n in range(s):
        y, x = y + dy, x + dx
        if is_valid(y, x):
            biz[y][x] = 0


def explode_clusters(clusters):
    global score
    for c in clusters:
        for cy, cx in c:
            score += biz[cy][cx]
            biz[cy][cx] = 0


def get_all_clusters(graph, directions, cond=lambda x: True):
    y, x = start
    x -= 1
    visited = [[False for _ in range(N)] for _ in range(N)]
    clusters = []

    for [n, (dy, dx)] in directions:
        for i in range(n):
            if not visited[y][x] and biz[y][x] != 0:
                visited[y][x] = True
                cluster = get_cluster(graph, (y, x), visited)

                if cond(cluster):
                    clusters.append(cluster)

            y, x = y + dy, x + dx

    if not visited[0][0]:
        cluster = [(0, 0)]
        if cond(cluster) and biz[0][0] != 0:
            clusters.append(cluster)

    return clusters


def get_cluster(graph, start, visited):
    will_visit = deque([start])
    cluster_num = biz[start[0]][start[1]]
    cluster = [start]

    while len(will_visit) > 0:
        now_y, now_x = will_visit.popleft()

        for adj_y, adj_x in graph[now_y][now_x]:
            if visited[adj_y][adj_x]:
                continue
            if biz[adj_y][adj_x] != cluster_num:
                continue

            visited[adj_y][adj_x] = True
            cluster.append((adj_y, adj_x))
            will_visit.append((adj_y, adj_x))

    return cluster


def transform_clusters(clusters, directions):
    to_add = []
    for c in clusters:
        A = len(c)
        B = biz[c[0][0]][c[0][1]]
        to_add += [A, B]

    refill_biz(directions, to_add)


def is_valid(i, j):
    return 0 <= i < N and 0 <= j < N


solution()