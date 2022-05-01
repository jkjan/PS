from collections import deque
from itertools import product


# 격자 사이즈
SIZE = 4

# 물고기의 방향 종류
D_SIZE = 8

# 상어의 방향 종류
SD_SIZE = 4

# 상어가 나아갈 수 없음
IMPOSSIBLE = -1

# 물고기 냄새
FISH_SMELL = 3

# 물고기, 상어 방향
dy  = [0, -1, -1, -1,
       0, 1, 1, 1]

dx = [-1, -1, 0, 1,
      1, 1, 0, -1]

sdy = [-1, 0, 1, 0]
sdx = [0, -1, 0, 1]

# 물고기의 수, 상어가 마법을 연습한 횟수
M, S = 0, 0

# 격자에 있는 물고기 큐
fish = [[deque()]]

# 상어 위치
sx, sy = 0, 0

# 복사할 물고기들 큐
to_copy = deque()

# 격자의 물고기 냄새
smell = [[0]]

# 상어가 이동 가능한 모든 방향 시퀀스
possible_shark_direction_sequences = list(product([_ for _ in range(4)], repeat=3))


def solution():
    T = 1
    for t in range(T):
        tc()


def tc():
    # 전역변수 초기화 및 입력
    init()

    # S번 마법 연습 시전
    for i in range(S):
        do_magic()
        pass

    # 정답 출력
    answer = get_answer()
    print(answer)


# 전역변수 초기화 및 입력
def init():
    global M, S, fish, sx, sy, smell, to_copy
    M, S = map(int, input().split())
    fish = [[deque() for _ in range(SIZE)] for _ in range(SIZE)]

    for i in range(M):
        fx, fy, d = map(int, input().split())
        fy -= 1; fx -= 1; d -= 1
        fy, fx = fx, fy
        fish[fy][fx].append(d)

    sx, sy = map(int, input().split())
    sx -= 1; sy -= 1
    sx, sy = sy, sx

    to_copy = deque()
    smell = [[0 for _ in range(SIZE)] for _ in range(SIZE)]


def do_magic():
    prepare_to_copy()
    move_all_fish()
    move_shark_via_best_way()
    reduce_smell()
    copy_fish()
    pass


def prepare_to_copy():
    for i in range(SIZE):
        for j in range(SIZE):
            fish_count = len(fish[i][j])
            for k in range(fish_count):
                d = fish[i][j].popleft()
                to_copy.append((i, j, d))
                fish[i][j].append(d)


def move_all_fish():
    # 이동 시킬 물고기들
    to_move = []
    for i in range(SIZE):
        for j in range(SIZE):
            s = len(fish[i][j])
            for k in range(s):
                # 칸에서 물고기를 빼서 이동할 큐에 삽입
                d = fish[i][j].popleft()
                moved_y, moved_x, d = move_fish(i, j, d)
                to_move.append([moved_y, moved_x, d])

    # 이동시킬 물고기들을 실제로 이동시킴
    for my, mx, d in to_move:
        fish[my][mx].append(d)


def move_fish(i, j, d):
    moved_y, moved_x = i, j

    for l in range(D_SIZE):
        adj_y = i + dy[d]
        adj_x = j + dx[d]

        if is_fish_movable(adj_y, adj_x):
            moved_y, moved_x = adj_y, adj_x
            break

        d = (d - 1) % D_SIZE

    return moved_y, moved_x, d


def is_fish_movable(i, j):
    return is_valid(i, j) and \
           (sy, sx) != (i, j) and \
           smell[i][j] == 0


def is_valid(i, j):
    return 0 <= i < SIZE and 0 <= j < SIZE


def move_shark_via_best_way():
    global sy, sx
    d_seq_candidates = []

    # 상어가 이동할 수 있는 모든 방향 시퀀스대로 움직여 봄
    for d_seq in possible_shark_direction_sequences:
        ret = move_shark(d_seq)
        if ret is not None:
            eaten_fish_count, v_sy, v_sx, eaten_fish_pos = ret
            d_seq_candidates.append([-eaten_fish_count, "".join(list(map(str, d_seq))), v_sy, v_sx, eaten_fish_pos])

    d_seq_candidates.sort()

    # 후보군이 하나라도 있다면 먹은 물고기 수가 가장 크거나 사전 순으로 앞에 있는 방향대로 실제로 움직임
    if len(d_seq_candidates) >= 1:
        _, _, v_sy, v_sx, eaten_fish_pos = d_seq_candidates[0]
        sy, sx = v_sy, v_sx

        for fy, fx in eaten_fish_pos:
            fish[fy][fx].clear()
            smell[fy][fx] = FISH_SMELL


def move_shark(d_seq):
    global sy, sx
    eaten_fish_count = 0
    eaten_fish_pos = []
    v_sy, v_sx = sy, sx
    visited = [[False for _ in range(SIZE)] for _ in range(SIZE)]

    for d in d_seq:
        adj_y, adj_x = v_sy + sdy[d], v_sx + sdx[d]

        if not is_valid(adj_y, adj_x):
            return None

        if not visited[adj_y][adj_x]:
            visited[adj_y][adj_x] = True

            if fish[adj_y][adj_x]:
                eaten_fish_count += len(fish[adj_y][adj_x])
                eaten_fish_pos.append((adj_y, adj_x))

        v_sy, v_sx = adj_y, adj_x

    return eaten_fish_count, v_sy, v_sx, eaten_fish_pos


def reduce_smell():
    for i in range(SIZE):
        for j in range(SIZE):
            if smell[i][j] > 0:
                smell[i][j] -= 1


def copy_fish():
    while to_copy:
        fy, fx, d = to_copy.popleft()
        fish[fy][fx].append(d)


def get_answer():
    answer = 0

    for i in range(SIZE):
        for j in range(SIZE):
            answer += len(fish[i][j])

    return answer


solution()
