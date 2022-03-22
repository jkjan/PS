from collections import deque
import sys


def solve():
    warehouse = get_input()
    cnt = count_unripe_tomatoes(warehouse)
    answer = bfs(cnt, warehouse)

    sys.stdout.write("%d\n" % answer)


def get_input():
    global M, N
    M, N = map(int, sys.stdin.readline().split())
    warehouse = []

    for i in range(N):
        warehouse.append(list(map(int, sys.stdin.readline().split())))

    return warehouse


def count_unripe_tomatoes(warehouse):
    return sum(row.count(0) for row in warehouse)


def init_bfs(warehouse):
    will_visit = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]

    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == 1:
                will_visit.append([(i, j), 0])
                visited[i][j] = True

    return will_visit, visited


def bfs(tmt_cnt, warehouse):
    will_visit, visited = init_bfs(warehouse)

    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    max_day = -1

    while 0 < len(will_visit):
        (now_y, now_x), now_day = will_visit.popleft()

        # 지금 방문한 노드에서 할 일
        if warehouse[now_y][now_x] == 0:
            max_day = now_day
            tmt_cnt -= 1

        # 주변 노드를 방문할 로직
        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx

            # 인덱스가 벗어난 경우
            if not is_valid(adj_y, adj_x):
                continue

            # 벽인 경우
            if warehouse[adj_y][adj_x] == -1:
                continue

            # 이미 방문한 토마토인 경우
            if visited[adj_y][adj_x]:
                continue

            will_visit.append([(adj_y, adj_x), now_day + 1])
            visited[adj_y][adj_x] = True

    return max_day if tmt_cnt <= 0 else -1


def is_valid(y, x):
    return 0 <= y < N and 0 <= x < M


solve()