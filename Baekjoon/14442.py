import sys
from collections import deque


deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def solution():
    N, M, K, field = get_input()
    visited = [[[0 for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    will_visit = deque([(0, 0, 0)])

    while len(will_visit) > 0:
        now_y, now_x, now_broken = will_visit.popleft()

        if now_y == N - 1 and now_x == M - 1:
            sys.stdout.write("%d" % visited[now_y][now_x][now_broken])
            return

        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx
            next_broken = now_broken

            if not (0 <= adj_y < N and 0 <= adj_x < M):
                continue
            if visited[adj_y][adj_x][now_broken]:
                continue
            if field[adj_y][adj_x] == '1':
                if now_broken >= K:
                    continue
                else:
                    next_broken += 1

            visited[adj_y][adj_x][next_broken] = visited[now_y][now_x][now_broken] + 1
            will_visit.append((adj_y, adj_x, next_broken))

    sys.stdout.write("%d" % -1)
    return


def get_input():
    N, M, K = map(int, sys.stdin.readline().split())
    field = [list(sys.stdin.readline().strip()) for _ in range(N)]
    return N, M, K, field


solution()