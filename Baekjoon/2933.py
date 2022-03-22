from collections import deque


cave = []
R = C = N = 0
heights = []
deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution():
    # 문제 입력
    get_input()

    # 첫 번째 막대는 왼쪽에서 오른쪽으로 (= 정방향)
    direction = 1

    # 막대기를 던지면서
    for height in heights:
        # 높이를 밑에서부터 세므로 R에서 빼줌
        height = R - height

        # 던져서 깨진 미네랄의 x 좌표를 얻음
        c = throw(direction, height)

        # 새로운 클러스터 구하기
        new_cluster = get_new_cluster(height, c, direction)

        # 새로운 클러스터가 생겼다면
        if new_cluster is not None:
            # 떨어뜨리기
            fall(new_cluster)

        # 방향 전환
        direction *= -1

    # 정답 출력
    print_cave()


# 동굴 출력하기
def print_cave():
    for i in range(R):
        for j in range(C):
            print(cave[i][j], end='')
        print()
    print()


# 입력 받기
def get_input():
    global R, C, N, heights

    # 행, 열 입력
    R, C = map(int, input().split())

    # 동굴 입력
    for i in range(R):
        cave.append(list(input()))

    # 날아온 높이
    N = int(input())
    heights = list(map(int, input().split()))


# height 에서 direction 방향으로 던지기
def throw(direction, height):
    # 날아온 방향에 따라 시작점과 끝점을 구함
    if direction == 1:
        s, e = 0, C
    else:
        s, e = C-1, -1

    # 방향대로 x축과 평행하게 날아가면서
    for i in range(s, e, direction):
        # 미네랄을 만나면 파괴하고 종료
        if cave[height][i] == 'x':
            cave[height][i] = '.'
            return i

    return -1


# (height, i) 에서 시작하는 공중에 뜬 클러스터 구하기
def get_new_cluster_from(height, i):
    # 좌표가 유효하지 않거나 그곳에 미네랄이 없을 경우 종료
    if not is_valid(height, i) or cave[height][i] != 'x':
        return None

    # bfs 준비
    will_visit = deque([(height, i)])
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[height][i] = True

    # 바닥에 닿아 있는 미네랄이 하나도 없는 (= 공중에 떠있는) 새로운 클러스터
    cluster = []

    while len(will_visit) > 0:
        now_y, now_x = will_visit.popleft()
        cluster.append((now_y, now_x))

        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx

            # 단 하나라도 바닥에 닿아있으면 공중에 뜬 게 아니므로 더 이상 진행할 필요 없음
            if adj_y == R:
                return None

            # 유효한 좌표가 아니거나, 이미 방문했거나, 빈칸이라면 방문하지 않음
            if not is_valid(adj_y, adj_x):
                continue
            if visited[adj_y][adj_x]:
                continue
            if cave[adj_y][adj_x] == '.':
                continue

            visited[adj_y][adj_x] = True
            will_visit.append((adj_y, adj_x))

    return cluster


# (height, c) 기준으로 위, direction 방향, 밑으로 클러스터 구하기
def get_new_cluster(height, c, direction):
    # 위쪽으로 클러스터 확인
    new_cluster = get_new_cluster_from(height - 1, c)

    # 옆 (날라온 방향대로) 으로 클러스터 확인
    if new_cluster is None:
        new_cluster = get_new_cluster_from(height, c + direction)

    # 아래로 클러스터 확인
    if new_cluster is None:
        new_cluster = get_new_cluster_from(height + 1, c)

    return new_cluster


# 유효한 좌표인지를 반환하기
def is_valid(i, j):
    return 0 <= i < R and 0 <= j < C


# 공중에 뜬 클러스터를 떨어뜨리기
def fall(cluster):
    dy = 0
    flag = True

    # 같은 클러스터임을 표시
    for c_y, c_x in cluster:
        cave[c_y][c_x] = 'c'

    while flag:
        dy += 1

        # 클러스터 내 모든 미네랄에 대해 높이를 내리면서
        for c_y, c_x in cluster:
            # 바닥이나 미네랄에 닿으면 종료
            if c_y + dy >= R or cave[c_y + dy][c_x] == 'x':
                flag = False
                break

    # 마지막으로 유효한 높이 변화량
    dy -= 1

    # 1칸 이상 내릴 수 있다면 다 내리기
    if dy > 0:
        # 과거 좌표에 미네랄 표시 지움
        for c_y, c_x in cluster:
            cave[c_y][c_x] = '.'

        # 새 좌표에 미네랄 표시
        for c_y, c_x in cluster:
            cave[c_y + dy][c_x] = 'x'


solution()