from collections import deque
from itertools import product


deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def solution(grid):
    grid = [list(g) for g in grid]
    wild_card_pos = get_wild_card_pos(grid)
    n = len(wild_card_pos)
    grid_h = len(grid)
    grid_w = len(grid[0])
    answer = 0

    for p in product(['a', 'b', 'c'], repeat=n):
        for i, (y, x) in enumerate(wild_card_pos):
            grid[y][x] = p[i]

        visited = [[False for _ in range(grid_w)] for _ in range(grid_h)]
        alphas = set()
        possible = True
        for i in range(grid_h):
            if not possible:
                break
            for j in range(grid_w):
                if not visited[i][j]:
                    visited[i][j] = True
                    if grid[i][j] in alphas:
                        possible = False
                        break

                    bfs(visited, (i, j), grid)
                    alphas.add(grid[i][j])

        if possible:
            answer += 1

    return answer


def get_wild_card_pos(grid):
    wild_card_pos = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '?':
                wild_card_pos.append((i, j))
    return wild_card_pos


def bfs(visited, start, grid):
    will_visit = deque([start])
    grid_h = len(visited)
    grid_w = len(visited[0])
    while len(will_visit) > 0:
        now_y, now_x = will_visit.popleft()
        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx
            if 0 <= adj_y < grid_h and 0 <= adj_x < grid_w:
                if not visited[adj_y][adj_x]:
                    if grid[adj_y][adj_x] == grid[start[0]][start[1]]:
                        visited[adj_y][adj_x] = True
                        will_visit.append((adj_y, adj_x))



grid = ["aa?"]
print(solution(grid))