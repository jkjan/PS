from collections import deque
LIMIT = 100


def solve():
    for t in range(10):
        tc()


def tc():
    t = int(input())
    field = [list(map(int, input().split())) for _ in range(LIMIT)]
    visited = [[False for _ in range(LIMIT)] for _ in range(LIMIT)]
    end_y, end_x = find_two(field)
    will_visit = deque([(end_y, end_x)])
    visited[end_y][end_x] = True
    deltas = [(0, 1), (0, -1), (-1, 0)]

    while len(will_visit) > 0:
        now_y, now_x = will_visit.popleft()
        if now_y == 0:
            print("#%d %d" % (t, now_x))
            return

        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx
            if not is_valid(adj_y, adj_x):
                continue
            if visited[adj_y][adj_x]:
                continue
            if field[adj_y][adj_x] != 1:
                continue

            visited[adj_y][adj_x] = True
            will_visit.append((adj_y, adj_x))
            break


def is_valid(i, j):
    return 0 <= i < LIMIT and 0 <= j < LIMIT


def find_two(field):
    for i in range(LIMIT):
        for j in range(LIMIT):
            if field[i][j] == 2:
                return i, j


solve()