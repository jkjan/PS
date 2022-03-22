from copy import deepcopy


DEAD = -2
EMPTY = -1
ROW = 0
COL = 1
STATUS = 2

deltas = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
MAX_FISH = 16
MAX_LEN = 4


def solution():
    # 입력값으로 주어지는 초기 수족관과 물고기 정보
    initial_aquarium, initial_fish_info = get_input()

    # 초기 상태, 상어는 (0, 0)에서 시작
    will_visit = [[deepcopy(initial_aquarium), deepcopy(initial_fish_info), 0, 0, 0]]
    max_fish_sum = -1

    while len(will_visit) > 0:
        # 현재 분기의 정보
        [aquarium, fish_info, shark_y, shark_x, fish_sum] = will_visit.pop()

        # 상어가 자리에 있는 물고기를 먹음
        fish_sum, shark_dir = eat(aquarium, fish_info, shark_y, shark_x, fish_sum)

        # 최대값에 여태 먹은 물고기 번호 합 반영
        max_fish_sum = max(max_fish_sum, fish_sum)

        # 물고기를 모두 이동시킴
        move_all_fish(aquarium, fish_info, shark_y, shark_x)

        # 상어의 방향에 따른 y, x의 증가량
        dy, dx = deltas[shark_dir]

        while True:
            # 상어가 방향따라 한 칸 이동
            shark_y, shark_x = shark_y + dy, shark_x + dx

            # 더 나아갈 곳이 없으면 해당 분기의 탐색 종료
            if not is_valid(shark_y, shark_x):
                break

            # 빈 칸이 아니라면 상어가 이동할 수 있으므로 탐색할 분기 추가
            if aquarium[shark_y][shark_x] != EMPTY:
                will_visit.append([deepcopy(aquarium), deepcopy(fish_info), shark_y, shark_x, fish_sum])

    return max_fish_sum


def get_input():
    # 물고기 정보: [행, 열, 상태(방향 혹은 사망)]
    fish_info = [[0, 0, 0] for _ in range(MAX_FISH + 1)]

    # aquarium[y][x]: (y, x) 칸에 있는 물고기 번호
    aquarium = [[0 for _ in range(MAX_LEN)] for _ in range(MAX_LEN)]

    for i in range(MAX_LEN):
        row = list(map(int, input().split()))
        for j in range(0, len(row) - 1, 2):
            a, b = row[j], row[j + 1]
            aquarium[i][j//2] = a
            # 계산 용이하게 하기 위해서 방향을 1 빼서 저장
            fish_info[row[j]] = [i, j // 2, b - 1]

    return aquarium, fish_info


def move_all_fish(aquarium, fish_info, shark_y, shark_x):
    # 작은 물고기 번호부터 움직임
    for fish_id in range(1, MAX_FISH + 1):
        if fish_info[fish_id][STATUS] != DEAD:
            move_fish(aquarium, fish_info, fish_id, shark_y, shark_x)


def move_fish(aquarium, fish_info, fish_id, shark_y, shark_x):
    # 현재 물고기의 좌표
    [fish_y, fish_x] = fish_info[fish_id][:2]

    for i in range(8):
        # 현재 물고기의 방향에 따른 y, x의 변화량
        dy, dx = deltas[fish_info[fish_id][STATUS]]

        # 현재 바라보고 있는 칸의 좌표
        adj_y, adj_x = fish_y + dy, fish_x + dx

        # 이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸이다.
        if (adj_y, adj_x) == (shark_y, shark_x) or not is_valid(adj_y, adj_x):
            # 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
            fish_info[fish_id][STATUS] = (fish_info[fish_id][STATUS] + 1) % 8
            continue

        # 물고기가 이동할 수 있는 주변 칸
        adj = aquarium[adj_y][adj_x]

        # 물고기가 있는 칸이라면
        if adj != EMPTY:
            # 물고기 정보의 위치 값을 서로 바꿔줌
            fish_info[adj][:2], fish_info[fish_id][:2] = fish_info[fish_id][:2], fish_info[adj][:2]
        else:
            # 없는 칸이라면 바꿀 필요 없이 수정
            fish_info[fish_id][:2] = [adj_y, adj_x]

        # 수족관 칸에 있는 물고기 번호를 바꿈
        aquarium[adj_y][adj_x], aquarium[fish_y][fish_x] = \
            aquarium[fish_y][fish_x], aquarium[adj_y][adj_x]
        break


def eat(aquarium, fish_info, shark_y, shark_x, fish_sum):
    # 상어 위치에 있던 물고기
    eaten_fish_id = aquarium[shark_y][shark_x]

    # 상어 위치에 있던 물고기의 방향
    shark_dir = fish_info[eaten_fish_id][STATUS]

    # 물고기 번호 합에 추가
    fish_sum += eaten_fish_id

    # 물고기 상태를 죽었음으로 표시하고 상어 자리가 비었다고 표시
    fish_info[eaten_fish_id][STATUS] = DEAD
    aquarium[shark_y][shark_x] = EMPTY

    return fish_sum, shark_dir


def is_valid(i, j):
    return 0 <= i < MAX_LEN and 0 <= j < MAX_LEN


print(solution())