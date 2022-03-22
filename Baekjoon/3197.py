from collections import deque


INF = 1500 + 1500 + 1
deltas_full = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def solution():
    get_input()

    # 최소 시간 초기화, 백조 위치 구하기
    init_info()

    # 오른쪽, 아래 방향으로 훑으면서 빙판이 녹는 시간 구하기 (-> 왼쪽 위부터 차례차례 증가)
    get_minimum_time((0, 0), deltas_full[:2])

    # 왼쪽, 위 방향으로 훑으면서 빙판이 녹는 시간 구하기 (-> 오른쪽 아래부터 차례차례 증가)
    get_minimum_time((R - 1, C - 1), deltas_full[2:])

    # 백조들이 만나는 최소 시간 구하기
    e = find_the_earliest_day()

    print(e)


# 빙판이 녹는 최소 시간 초기화하고 백조 위치 얻기
def init_info():
    global minimum_time, swan
    minimum_time = [[INF for _ in range(C)] for _ in range(R)]
    swan = []

    for i in range(R):
        for j in range(C):
            # X가 아니면 물이므로 0이고, 특히 L이면 백조의 위치이므로 좌표값을 저장해둠
            if lake[i][j] != 'X':
                if lake[i][j] == 'L':
                    swan.append((i, j))
                minimum_time[i][j] = 0


def get_input():
    global R, C, lake

    # 행, 열 입력
    R, C = map(int, input().split())

    # 호수 입력
    lake = [list(input()) for _ in range(R)]


# 백조 간의 길이 생기는 시간의 최소값 구하기
def find_the_earliest_day():
    # 빙판이 녹는 시간은 0부터 749까지 가능
    s = 0
    e = 749

    # 이분 탐색
    while s <= e:
        m = (s + e) // 2
        if is_path(m):
            e = m - 1
        else:
            s = m + 1

    return s


# 최소 시간 얻기
def get_minimum_time(start, deltas):
    will_visit = deque([start])
    visited = [[False for _ in range(C)] for _ in range(R)]

    while len(will_visit) > 0:
        now_y, now_x = will_visit.popleft()

        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx

            if not is_valid(adj_y, adj_x):
                continue

            # 주변 위치들의 최소 시간을 갱신함. 이때 갱신하는 건 방문 여부랑 상관 없음
            minimum_time[adj_y][adj_x] = min(minimum_time[now_y][now_x] + 1, minimum_time[adj_y][adj_x])

            if visited[adj_y][adj_x]:
                continue

            visited[adj_y][adj_x] = True
            will_visit.append((adj_y, adj_x))


def is_valid(i, j):
    return 0 <= i < R and 0 <= j < C


# 길 있는지 여부 구하기
def is_path(days):
    will_visit = deque([swan[0]])
    visited = [[False for _ in range(C)] for _ in range(R)]

    while len(will_visit) > 0:
        now_y, now_x = will_visit.popleft()

        # 길 있음
        if (now_y, now_x) == swan[1]:
            return True

        for dy, dx in deltas_full:
            adj_y, adj_x = now_y + dy, now_x + dx

            if not is_valid(adj_y, adj_x):
                continue
            if visited[adj_y][adj_x]:
                continue
            if minimum_time[adj_y][adj_x] > days:
                # 현재 날짜보다 큰 곳은 아직 안 녹았으므로 못 감
                continue

            visited[adj_y][adj_x] = True
            will_visit.append((adj_y, adj_x))

    return False


solution()