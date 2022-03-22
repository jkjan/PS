import sys
from collections import deque


# 상하좌우
deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 제수
DIVISOR = 10


def solution():
    N, M, field = get_input()

    visited = [[False for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            # 벽이 아니면서 아직 방문되지 않은 곳을 계속해서 방문 (클러스터의 시작점)
            if field[i][j] == -1 and not visited[i][j]:
                visited[i][j] = True
                bfs((i, j), visited, N, M, field)

    # 정답 출력
    for line in field:
        sys.stdout.write("%s\n" % "".join([str(x) if x != -1 else '0' for x in line]))


def bfs(start, visited, N, M, field):
    will_visit = deque([start])
    walls = set()
    cnt = 0

    # 0들의 클러스터 개수를 세면서, 클러스터 외곽의 벽 위치를 저장
    while len(will_visit) > 0:
        now_y, now_x = will_visit.popleft()
        cnt += 1

        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx

            if not (0 <= adj_y < N and 0 <= adj_x < M):
                continue
            if visited[adj_y][adj_x]:
                continue
            if field[adj_y][adj_x] != -1:
                # 인접 위치가 벽이면 해당 위치 저장
                walls.add((adj_y, adj_x))
                continue

            # 벽 아니면 이동
            visited[adj_y][adj_x] = True
            will_visit.append((adj_y, adj_x))

    # 저장된 벽 좌표에다 클러스터의 개수를 더해줌 (그 벽을 뚫었을 때 이동할 수 있는 곳의 개수)
    for wall_y, wall_x in walls:
        field[wall_y][wall_x] = (field[wall_y][wall_x] + cnt) % DIVISOR


def get_input():
    N, M = map(int, sys.stdin.readline().split())
    # 문제에서 값을 10의 나머지로 하라고 했으므로
    # 벽이 아닌 곳의 0과 벽을 10으로 나눈 나머지 0을 구분하기 위해 벽이 아닌 곳을 -1로 받음
    field = [list(map(lambda x: 1 if x == '1' else -1, sys.stdin.readline().strip())) for _ in range(N)]
    return N, M, field


solution()