from collections import deque
from copy import deepcopy


HORSE_CNT = 4
DICE_CNT = 10
START = 0
ARRIVED = 32


# n번째 칸과 연결된 칸 -> [기본 칸, 서브 칸]
graph = [[1],

         [2], [3], [4], [5], [10, 6],
         [7], [8], [9], [23], [11],
         [12], [13], [14], [15, 30], [16],
         [17], [18], [19], [26, 20], [21],
         [22], [9], [24], [25], [ARRIVED],

         [27], [28], [29], [25], [31],
         [9], []]

score = [0,

         2, 4, 6, 8, 10,
         13, 16, 19, 25, 12,
         14, 16, 18, 20, 22,
         24, 26, 28, 30, 28,
         27, 26, 30, 35, 40,

         32, 34, 36, 38, 22,
         24, 0]


def solution():
    dice_seq = list(map(int, input().split()))

    # 처음에는 시작 칸에 말 4개가 있다.
    location_init = [START for _ in range(HORSE_CNT)]
    will_visit = deque([[0, 0, location_init]])
    max_score = 0

    while len(will_visit) > 0:
        score_sum, dice, location = will_visit.popleft()
        max_score = max(max_score, score_sum)

        if dice >= DICE_CNT:
            continue

        # 말 선택
        for horse_to_move in range(HORSE_CNT):
            # 도착 칸에 있지 않은 말을 하나 고른다.
            if location[horse_to_move] == ARRIVED:
                continue

            # 고른 말의 현재 위치
            moved_to = location_was = location[horse_to_move]

            # 말이 파란색 칸에서 이동을 시작하면 파란색 화살표를 타야 하고, 이동하는 도중이거나 파란색이 아닌 칸에서 이동을 시작하면 빨간색 화살표를 타야 한다.
            if len(graph[moved_to]) > 1:
                moved_to = graph[moved_to][1]
            else:
                moved_to = graph[moved_to][0]

            # 주사위 - 1 만큼 움직인다.
            for i in range(dice_seq[dice] - 1):
                # 말이 도착 칸으로 이동하면 주사위에 나온 수와 관계 없이 이동을 마친다.
                if moved_to == ARRIVED:
                    break
                # 그래프의 기본 경로만을 본다
                moved_to = graph[moved_to][0]

            # 말이 이동을 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없다. 단, 이동을 마치는 칸이 도착 칸이면 고를 수 있다.
            if moved_to != ARRIVED and moved_to in location:
                continue

            # 말이 이동을 마칠 때마다 칸에 적혀있는 수가 점수에 추가된다.
            new_score = score_sum + score[moved_to]

            location[horse_to_move] = moved_to
            will_visit.append([new_score, dice + 1, deepcopy(location)])
            location[horse_to_move] = location_was

    return max_score


print(solution())