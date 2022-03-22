from collections import deque

LIMIT = 16
deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solve():
    for i in range(10):
        print("#%d %d" % (int(input()), tc()))


def tc():
    visited = [[False for _ in range(LIMIT)] for _ in range(LIMIT)]
    field = [list(map(int, list(input()))) for _ in range(LIMIT)]
    start, end = find_point(field)
    will_visit = deque([start])
    visited[start[0]][start[1]] = True

    while len(will_visit) > 0:
        [now_y, now_x] = will_visit.popleft()

        if [now_y, now_x] == end:
            return 1

        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx
            if not is_valid(adj_y, adj_x):
                continue
            if field[adj_y][adj_x] == 1:
                continue
            if visited[adj_y][adj_x]:
                continue
            visited[adj_y][adj_x] = True
            will_visit.append([adj_y, adj_x])

    return 0


def is_valid(i, j):
    return 0 <= i < LIMIT and 0 <= j < LIMIT


def find_point(field):
    start = []
    end = []

    for i in range(LIMIT):
        for j in range(LIMIT):
            if field[i][j] == 2:
                start = [i, j]
            elif field[i][j] == 3:
                end = [i, j]

    return start, end


solve()