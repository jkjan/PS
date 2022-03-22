from collections import deque


# 구멍 위치
O_y, O_x = 0, 0

# 위치 변화량
deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 정렬 기준 (역순?, 행 or 열?)
std = [(1, 0), (-1, 1), (-1, 0), (1, 1)]


def solution():
    board = get_input()
    R, B = init_biz(board)
    answer = bfs(board, R, B)
    print(answer)


def get_input():
    global N, M
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    return board


def init_biz(board):
    global O_y, O_x
    R = [0, 0]
    B = [0, 0]

    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                R = [i, j]
            elif board[i][j] == 'B':
                B = [i, j]
            elif board[i][j] == 'O':
                O_y, O_x = i, j

    board[R[0]][R[1]] = '.'
    board[B[0]][B[1]] = '.'

    return R, B


# 구슬 굴려서 최종적으로 도달하는 위치
def roll(board, b_y, b_x, d):
    dy, dx = deltas[d]

    while True:
        b_y, b_x = b_y + dy, b_x + dx

        if not (is_valid(b_y, b_x) and board[b_y][b_x] == '.'):
            break

    if (b_y, b_x) == (O_y, O_x):
        return b_y, b_x
    else:
        return b_y - dy, b_x - dx


def tilt(board, R, B, d):
    bizs = [('R', R), ('B', B)]

    # 구슬 정렬하기 (0이면 위에 있는 것부터, 1이면 오른쪽부터, 2면 밑에부터, 3이면 왼쪽부터 먼저 움직임)
    bizs.sort(key=lambda x: std[d][0] * x[1][std[d][1]])
    moved = [(0, 0), (0, 0)]

    for color, (b_y, b_x) in bizs:
        # 구슬이 도달한 위치
        moved_y, moved_x = roll(board, b_y, b_x, d)

        # 기존 구슬 위치를 비었다고 표시
        board[b_y][b_x] = '.'

        # 만약 도달한 곳이 구멍일 경우 구멍으로 표시 (그래야 뒤에 오는 구슬에게 영향을 줄 수 있음)
        if (moved_y, moved_x) == (O_y, O_x):
            board[moved_y][moved_x] = 'O'
        else:
            # 아니면 색 표시
            board[moved_y][moved_x] = color

        # 구슬들이 도달한 곳 저장
        moved[0 if color == 'R' else 1] = (moved_y, moved_x)

    return moved


def bfs(board, R, B):
    will_visit = deque([[R, B, 0]])

    while len(will_visit) > 0:
        [now_R, now_B, cnt] = will_visit.popleft()

        # 현재 구슬을 보드에 표시
        board[now_R[0]][now_R[1]] = 'R'
        board[now_B[0]][now_B[1]] = 'B'

        if cnt >= 10:
            continue

        for d in range(4):
            moved = tilt(board, now_R, now_B, d)

            # 최종 빨간 구슬 위치, 파란 구슬 위치
            [moved_R, moved_B] = moved

            # 파란색은 구슬에 안 빠졌으면서 빨간색이 빠지면 종료
            if moved_R == (O_y, O_x) and moved_B != (O_y, O_x):
                return cnt + 1
            else:
                # 파란색이 빠진 게 아니라면 (둘 다 안 빠졌다면) 현재 위치를 기점으로 다시 탐색
                if moved_B != (O_y, O_x):
                    will_visit.append([moved_R, moved_B, cnt + 1])

                # 다음 탐색을 위해 이동 후 표시된 구슬을 다시 비었다고 표시
                board[moved_R[0]][moved_R[1]] = '.'
                board[moved_B[0]][moved_B[1]] = '.'

    return -1


def is_valid(i, j):
    return 0 <= i < N and 0 <= j < M


solution()