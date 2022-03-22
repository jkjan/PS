import sys
from collections import defaultdict

scan = sys.stdin.readline
deltas = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def solution():
    T = int(scan())
    for t in range(T):
        tc()


def tc():
    board, N, query = get_input()
    answer = [False for _ in range(N)]
    entry_points = get_entry_points(board)

    for i in range(N):
        is_possible(board, query, answer, i, entry_points)
        sys.stdout.write("%s %s\n" % (query[i], "YES" if answer[i] else "NO"))


def get_input():
    board = [list(scan().strip()) for _ in range(5)]
    N = int(scan())
    query = [scan().strip() for _ in range(N)]
    return board, N, query


def get_entry_points(board):
    entry_points = defaultdict(lambda: [])
    for i in range(5):
        for j in range(5):
            entry_points[board[i][j]].append((i, j))
    return entry_points


def is_possible(board, query, answer, i, entry_points):
    for ey, ex in entry_points[query[i][0]]:
        dfs(board, query, answer, i, 0, ey, ex)
        if answer[i]:
            break


def dfs(board, query, answer, i, j, y, x):
    if j == len(query[i]):
        answer[i] = True
        return

    if not answer[i]:
        if is_valid(y, x):
            if board[y][x] == query[i][j]:
                for dy, dx in deltas:
                    adj_y, adj_x = y + dy, x + dx
                    dfs(board, query, answer, i, j + 1, adj_y, adj_x)


def is_valid(i, j):
    is_in = lambda x: 0 <= x < 5
    return is_in(i) and is_in(j)



solution()