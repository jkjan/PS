from collections import deque
import math

def solution(board):
    N = len(board)
    U, R, D, L = 0, 1, 2, 3
    delta = [[-1, 0, U], [0, 1, R], [1, 0, D], [0, -1, L]]

    def is_valid(i):
        return 0 <= i < N

    will_visit = deque()
    visited = [[[math.inf for i in range(4)] for j in range(N)] for k in range(N)]
    will_visit.append([0, 0, 0, R, []])
    will_visit.append([0, 0, 0, D, []])
    visited[0][0][R] = 0
    visited[0][0][D] = 0

    while len(will_visit) > 0:
        [now_y, now_x, now_cost, now_dir, now_path] = will_visit.pop()

        if now_y == N-1 and now_x == N-1:
            continue

        for [dy, dx, d_dir] in delta:
            then_y = now_y + dy
            then_x = now_x + dx
            if is_valid(then_y) and is_valid(then_x):
                if board[then_y][then_x] == 0:
                    then_cost = now_cost + (600 if now_dir != d_dir else 100)
                    if visited[then_y][then_x][d_dir] > then_cost:
                        visited[then_y][then_x][d_dir] = then_cost
                        then_path = now_path + [(then_y, then_x)]
                        will_visit.append([then_y, then_x, then_cost, d_dir, then_path])

    return min(visited[N-1][N-1])


board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]

print(solution(board))