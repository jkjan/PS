from collections import defaultdict
import sys

sys.setrecursionlimit(100000)
DIV = 10_000_019



def solution(width, height, diagonals):
    deltas = [(-1, 0), (0, 1)]
    graph = defaultdict(list)

    def is_valid(y, x):
        return 0 <= y <= height and 0 <= x <= width

    def make_graph():
        for i in range(height + 1):
            for j in range(width + 1):
                for dy, dx in deltas:
                    adj_y, adj_x = i + dy, j + dx
                    if is_valid(adj_y, adj_x):
                        graph[(i, j)].append((adj_y, adj_x))

        for x, y in diagonals:
            upper_left = (height - y, x - 1)
            lower_right = (height - y + 1, x)
            graph[upper_left].append(lower_right)
            graph[lower_right].append(upper_left)

    def dfs(y, x, d):
        if (y, x) == (0, width):
            if d:
                return 1
            else:
                return 0

        if dp[y][x][d] == -1:
            dp[y][x][d] = 0
            for adj_y, adj_x in graph[(y, x)]:
                if not visited[adj_y][adj_x][d]:
                    new_d = d
                    if abs(y - adj_y) + abs(x - adj_x) == 2:
                        if d == 1:
                            continue
                        else:
                            new_d = True
                    visited[adj_y][adj_x][new_d] = True
                    ret = dfs(adj_y, adj_x, new_d)
                    dp[y][x][d] = (dp[y][x][d] + (ret % DIV)) % DIV
                    visited[adj_y][adj_x][new_d] = False

        return dp[y][x][d]

    make_graph()
    dp = [[[-1 for _ in range(2)] for _ in range(width + 1)] for _ in range(height + 1)]
    visited = [[[False for _ in range(2)] for _ in range(width + 1)] for _ in range(height + 1)]

    return dfs(height, 0, False)
