from collections import deque

IMPOSSIBLE = -1
UNDEFINED = -2


def solution():
    global fuel
    taxi_y, taxi_x = get_input()
    init_dist_matrix()

    # 백준은 한 승객을 태워 목적지로 이동시키는 일을 M번 반복해야 한다.
    for i in range(M):
        # 가장 가까운 승객의 출발지와 목적지 좌표
        dept_y, dept_x, dest_y, dest_x = find_nearest(taxi_y, taxi_x)

        # 택시에서 출발지까지의 거리
        dist_to_dept = get_dist(taxi_y, taxi_x, dept_y, dept_x)

        # 출발지까지 가는 것이 불가능
        if dist_to_dept == IMPOSSIBLE:
            return -1

        # 출발지에서 목적지까지의 거리
        dist_to_dest = get_dist(dept_y, dept_x, dest_y, dest_x)

        # 목적지까지 가는 것이 불가능
        if dist_to_dept == IMPOSSIBLE:
            return -1

        # 목적지 도착 시의 연료 = 현재 남아있는 연료 - 출발지까지 드는 연료 - 목적지까지 드는 연료
        fuel_after_run = fuel - dist_to_dept - dist_to_dest

        # 이동하는 도중에 연료가 바닥나면 이동에 실패하고, 그 날의 업무가 끝난다.
        if fuel_after_run < 0:
            return -1

        # 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전된다.
        fuel = fuel_after_run + 2 * dist_to_dest

        # 택시 좌표를 목적지 좌표로 옮긴다.
        taxi_y, taxi_x = dest_y, dest_x

    return fuel


# 입력 받기
def get_input():
    global N, M, fuel, field, user, MAX
    N, M, fuel = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    taxi_y, taxi_x = map(int, input().split())
    user = [list(map(int, input().split())) for _ in range(M)]

    return taxi_y, taxi_x


# 가장 가깝거나, 행 번호가 제일 작거나, 열 번호가 제일 작은 승객 구하기
def find_nearest(taxi_y, taxi_x):
    nearest_user = min(user, key=lambda x: (get_dist(taxi_y, taxi_x, x[0], x[1]), x[0], x[1]))
    user.remove(nearest_user)

    return nearest_user


# 거리 행렬 초기화
def init_dist_matrix():
    global dist_matrix

    # dist_matrix[a][b][c][d]: (a, b)에서 (c, d)까지의 거리
    dist_matrix = [[[[UNDEFINED for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 자기자신으로의 거리는 0, 단 벽이라면 불가능
            dist_matrix[i][j][i][j] = 0 if field[i][j] == 0 else IMPOSSIBLE


# 좌표 유효 여부 체크
def is_valid(i, j):
    return 0 <= i < N and 0 <= j < N


# from 부터 to 까지의 거리 구하기
def get_dist(from_y, from_x, to_y, to_x):
    # 문제에서 인덱스가 1부터 시작하므로 1씩 빼줌
    from_y -= 1
    from_x -= 1
    to_y -= 1
    to_x -= 1

    # 이미 거리를 구한 적 있음
    if dist_matrix[from_y][from_x][to_y][to_x] != UNDEFINED:
        return dist_matrix[from_y][from_x][to_y][to_x]

    # 둘 중 하나가 벽이므로 불가능하다고 표시
    if field[from_y][from_x] == 1 or field[to_y][to_x] == 1:
        dist_matrix[from_y][from_x][to_y][to_x] = IMPOSSIBLE
        return IMPOSSIBLE

    # BFS 준비
    will_visit = deque([(from_y, from_x)])
    visited = [[False for _ in range(N)] for _ in range(N)]
    dist = [[0 for _ in range(N)] for _ in range(N)]
    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited[from_y][from_x] = True

    while len(will_visit) > 0:
        now_y, now_x = will_visit.popleft()

        # 도착
        if (now_y, now_x) == (to_y, to_x):
            return dist[to_y][to_x]

        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx

            # 좌표가 유효하지 않거나, 이미 방문했거나, 벽이라면 더 이상 진행하지 않음
            if not is_valid(adj_y, adj_x):
                continue
            if visited[adj_y][adj_x]:
                continue
            if field[adj_y][adj_x] == 1:
                continue

            # 거리 행렬 갱신하기
            dist[adj_y][adj_x] = dist[now_y][now_x] + 1
            dist_matrix[from_y][from_x][adj_y][adj_x] = dist[adj_y][adj_x]
            dist_matrix[adj_y][adj_x][from_y][from_x] = dist[adj_y][adj_x]

            # 방문 여부 표시하고 다음 방문할 큐에 삽입
            visited[adj_y][adj_x] = True
            will_visit.append((adj_y, adj_x))


    # 목적지까지 도달하지 못했음
    dist_matrix[from_y][from_x][to_y][to_x] = IMPOSSIBLE
    return IMPOSSIBLE


print(solution())
