def solution():
    # 문제 입력
    get_input()

    # 변수 초기화
    init()

    for sec in range(1000 + 1):
        # 상어가 한 마리 빼고 다 추방 당함
        if exiled_shark == M - 1:
            return sec

        # 각 상어 위치에 냄새 뿌리기
        put_smell()

        # 상어 움직이기
        move_all_sharks()

        # 이전 냄새 감소
        erase_smell()

    return -1


def get_input():
    global N, M, K, sea, shark_d, priority
    # N, M, K 입력
    N, M, K = map(int, input().split())

    # 현재 격자 상태 입력
    # sea[i][j]: (i, j) 의 격자
    sea = [list(map(int, input().split())) for _ in range(N)]

    # 상어들의 방향 입력
    # shark_d[s]: 상어 s의 방향
    shark_d = list(map(lambda x: int(x)-1, input().split()))

    # 우선순위 입력
    # priority[s][d]: 상어 s가 방향 d일 때의 우선순위
    priority = []
    for m in range(M):
        priority.append([list(map(lambda x: int(x)-1, input().split())) for _ in range(4)])


def init():
    global smell, sharks, deltas, exiled_shark

    # 냄새 상태 초기화
    # smell[i][j]: (i, j)에서의 냄새-> (s, remain) 상어 s의 냄새가 remain 만큼 남음
    smell = [[[0, 0] for _ in range(N)] for _ in range(N)]

    # 상어 위치 초기화
    # sharks[s]: 상어 s의 위치
    sharks = [[0, 0] for _ in range(M)]
    for i in range(N):
        for j in range(N):
            if sea[i][j] != 0:
                sharks[sea[i][j]-1] = [i, j]

    # 위, 아래, 왼쪽, 오른쪽
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 추방된 상어 수
    exiled_shark = 0


def put_smell():
    for [y, x] in sharks:
        # 죽은 상어가 아니라면 현재 위치에 냄새를 뿌림
        if (y, x) != (-1, -1):
            s = sea[y][x]
            smell[y][x] = [s, K]


def erase_smell():
    for i in range(N):
        for j in range(N):
            [s, remain] = smell[i][j]
            # 남은 양이 1이라면 [0, 0]으로 냄새를 초기화
            if remain == 1:
                smell[i][j] = [0, 0]
            elif remain > 0:
                smell[i][j] = [s, remain - 1]


def move_all_sharks():
    for s in range(M):
        # 죽은 상어가 아니라면 상어를 이동시킴
        if sharks[s] != [-1, -1]:
            move_shark(s)


def move_shark(s):
    global exiled_shark
    i, j = sharks[s]

    # 상어가 이동할 위치를 구함
    [next_i, next_j] = get_shark_delta(i, j)

    # 상어가 이동을 할 수 없음
    if [next_i, next_j] == [-1, -1]:
        return

    # 현 위치에서 상어를 제거함
    sea[i][j] = 0

    """
    상어는 냄새가 없거나 자기 냄새가 있는 곳으로만 가기 때문에
    다른 상어가 있는 곳으로는 절대 가지 않음.
    즉, 이동하려는 빈 칸이 우연히 일치하는 경우만 존재함.
    이때, 코드 상 상어는 번호가 작은 것부터 움직이기 때문에
    가장 먼저 온 상어가 그곳을 점령하고, 이후 거기에 도달하는 상어들은 모두 추방 당함.
    따라서 가려는 곳의 숫자가 0이 아니라면 상어는 그곳에서 추방 당함.
    """

    # 가고자 하는 곳이 비었으면
    if sea[next_i][next_j] == 0:
        # 바다에 상어를 위치시킴
        sea[next_i][next_j] = s + 1

        # 상어의 위치 변경
        sharks[s] = [next_i, next_j]
    else:
        # 상어가 추방됨을 표시
        sharks[s] = [-1, -1]

        # 추방된 상어 수를 하나 늘림
        exiled_shark += 1


def get_shark_delta(i, j):
    # 상어가 이동할 수 있는 후보군을 얻음
    move_candidate = get_move_candidate(i, j)
    s = sea[i][j] - 1

    # 상어 s와 그 위치 d에 따른 우선순위
    now_priority = priority[s][shark_d[s]]

    # 우선순위대로 따졌을 때 가장 먼저 유효한 위치를 찾아 반환
    for np in now_priority:
        if np in move_candidate.keys():
            shark_d[s] = np
            return move_candidate[np]

    # 갈 수 있는 위치가 없음
    # 냄새 없는 칸이 주변에 없어도 자기 냄새 있는 칸
    # 즉, 최소 자기가 왔던 칸으로는 가기 때문에
    # 이런 경우는 절대 있을 수 없음
    return [-1, -1]


def get_zone(i, j, cond):
    # zone[n]: (i, j)에서 방향 n으로 갔을 때 좌표가 유효하면서 조건 cond 에 맞는 위치
    zone = {}
    for e, (dy, dx) in enumerate(deltas):
        adj_y, adj_x = i + dy, j + dx

        if is_valid(adj_y, adj_x) and cond(adj_y, adj_x):
            zone[e] = [adj_y, adj_x]

    return zone


def get_move_candidate(i, j):
    # 냄새가 없는 구역
    no_smell_zone = get_zone(i, j, lambda y, x: smell[y][x] == [0, 0])

    # 냄새 없는 구역이 없다면
    if len(no_smell_zone) == 0:
        # 내 냄새가 있는 구역
        my_smell_zone = get_zone(i, j, lambda y, x: smell[y][x][0] == sea[i][j])
        return my_smell_zone
    else:
        return no_smell_zone


def is_valid(i, j):
    return 0 <= i < N and 0 <= j < N


print(solution())