from collections import deque
from copy import deepcopy


deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution():
    T = int(input())
    for t in range(1, T + 1):
        answer = tc()
        print("#%d %d" % (t, answer))


def tc():
    N, K, heights = get_input()
    highest_spots = get_highest_spots(N, heights)
    max_len = 0

    for hy, hx in highest_spots:
        here_max_len = bfs((hy, hx), N, K, heights)
        max_len = max(max_len, here_max_len)

    return max_len


def bfs(start, N, K, heights):
    will_visit = deque([[start, [], {start}]])
    max_len = 0

    while len(will_visit) > 0:
        [(now_y, now_x), now_con, visited] = will_visit.popleft()

        max_len = max(max_len, len(visited))

        for [y, x, amt] in now_con:
            heights[y][x] -= amt

        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx

            if not is_valid(adj_y, adj_x, N):
                continue
            if (adj_y, adj_x) in visited:
                continue

            next_con = deepcopy(now_con)
            if heights[adj_y][adj_x] >= heights[now_y][now_x]:
                amt = heights[adj_y][adj_x] - (heights[now_y][now_x] - 1)

                if len(next_con) == 0 and amt <= K:
                    next_con.append([adj_y, adj_x, amt])
                else:
                    continue

            will_visit.append([(adj_y, adj_x), next_con, visited.union({(adj_y, adj_x)})])

        for [y, x, amt] in now_con:
            heights[y][x] += amt

    return max_len


def is_valid(i, j, N):
    return 0 <= i < N and 0 <= j < N


def get_highest_spots(N, heights):
    highest_spots = []
    max_height = -1

    for i in range(N):
        for j in range(N):
            if heights[i][j] > max_height:
                highest_spots = [(i, j)]
                max_height = heights[i][j]
            elif heights[i][j] == max_height:
                highest_spots.append((i, j))

    return highest_spots


def get_input():
    N, K = map(int, input().split())
    heights = [list(map(int, input().split())) for _ in range(N)]
    return N, K, heights


solution()