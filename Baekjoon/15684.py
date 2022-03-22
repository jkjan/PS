import sys
from collections import deque


def solution():
    horizontal = get_input()
    will_visit = deque([[]])

    while len(will_visit) > 0:
        now_visit = will_visit.popleft()

        # 가로선 놓기
        for a, b in now_visit:
            horizontal[a][b] = True

        # 가능하면 추가된 가로선 수 리턴
        if is_possible(horizontal):
            return len(now_visit)

        # 추가된 가로선 3개 미만이면 하나 또 추가 가능
        if len(now_visit) < 3:
            # 시작은 맨 마지막에 추가된 가로선 위치, 없으면 0, 0
            s_i, s_j = now_visit[-1] if len(now_visit) > 0 else (0, 0)

            while s_i < H:
                # 점프할 거리 구함
                to_jump = get_to_jump(horizontal, s_i, s_j)

                # 점프할 거리 0이면 그 위치에 가로선 놓아도 됨
                if to_jump == 0:
                    will_visit.append(now_visit + [(s_i, s_j)])
                    s_j += 1
                else:
                    s_j += to_jump

                # 인덱스가 가로 크기 벗어남
                if s_j > last_v:
                    s_j = 0
                    s_i += 1

        # 가로선 복구
        for a, b in now_visit:
            horizontal[a][b] = False

    return -1


def get_input():
    global N, M, H, last_v
    N, M, H = map(int, sys.stdin.readline().split())
    horizontal = [[False for _ in range(N - 1)] for _ in range(H)]
    last_v = N - 2

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        horizontal[a - 1][b - 1] = True

    return horizontal


def is_possible(horizontal):
    for j in range(N):
        now_j = j

        for i in range(H):
            # 오른쪽/왼쪽에 가로선이 있음
            if now_j <= last_v and horizontal[i][now_j]:
                now_j += 1
            elif now_j > 0 and horizontal[i][now_j - 1]:
                now_j -= 1

        if j != now_j:
            return False

    return True


def get_to_jump(horizontal, i, j):
    # 이미 가로선이 있는 위치 -> 2칸 넘김
    if horizontal[i][j]:
        return 2
    # 왼쪽에 가로선이 있음
    if j >= 1 and horizontal[i][j - 1]:
        return 1
    # 오른쪽에 가로선이 있음
    if j + 1 <= last_v and horizontal[i][j + 1]:
        return 2

    # 해당 위치에 가로선을 놓을 수 있음
    return 0


sys.stdout.write("%d" % solution())