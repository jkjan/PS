from collections import deque


deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution(n, k):
    MAX = 2 * n
    dist = [[MAX for _ in range(n)] for _ in range(n)]

    i = 0
    while True:
        spot_y, spot_x = find_spot(dist, n)
        i += 1
        if i == k:
            return [spot_y + 1, spot_x + 1]
        seated(dist, n, spot_y, spot_x)


def find_spot(dist, n):
    spot = -1
    spot_y, spot_x = -1, -1
    for j in range(n):
        for i in range(n):
            if dist[i][j] > spot:
                spot_y, spot_x = i, j
                spot = dist[i][j]

    return spot_y, spot_x


def seated(dist, n, spot_y, spot_x):
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[spot_y][spot_x] = True
    dist[spot_y][spot_x] = 0
    will_visit = deque([[spot_y, spot_x, 0]])

    while len(will_visit) > 0:
        [now_y, now_x, now_dist] = will_visit.popleft()
        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx
            if not is_valid(n, adj_y, adj_x):
                continue
            if visited[adj_y][adj_x]:
                continue

            dist[adj_y][adj_x] = min(dist[adj_y][adj_x], now_dist + 1)
            visited[adj_y][adj_x] = True
            will_visit.append([adj_y, adj_x, now_dist + 1])


def is_valid(n, i, j):
    return 0 <= i < n and 0 <= j < n


n = 5
k = 25
answer = solution(n, k)
print(answer)