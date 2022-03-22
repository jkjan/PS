from collections import deque


HORIZONTAL = 0
VERTICAL = 1

deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(board):
    global N
    N = len(board)

    will_visit = deque([[(0, 0), HORIZONTAL, 0]])
    visited = [[[False for _ in range(2)] for _ in range(N)] for _ in range(N)]

    while len(will_visit) > 0:
        [now_primary, now_shape, now_cnt] = will_visit.popleft()
        now_secondary = add(now_primary, deltas[now_shape])
        now_block = (now_primary, now_secondary)

        if is_arrived(now_block):
            return now_cnt

        for i in range(4):
            next_primary = translate(board, now_block, i)
            next_move(next_primary, now_shape, now_cnt + 1, visited, will_visit)

        cases = [(True, 1), (True, -1), (False, 1), (False, -1)]
        for i in range(4):
            next_primary = rotate(board, now_block, cases[i][0], cases[i][1])
            next_move(next_primary, not now_shape, now_cnt + 1, visited, will_visit)

    return -1


def next_move(next_primary, next_shape, next_cnt, visited, will_visit):
    if next_primary is not None and not visited[next_primary[0]][next_primary[1]][next_shape]:
        visited[next_primary[0]][next_primary[1]][next_shape] = True
        will_visit.append([next_primary, next_shape, next_cnt])


def translate(board, block, direction):
    primary, secondary = block
    primary_moved = add(primary, deltas[direction])
    secondary_moved = add(secondary, deltas[direction])

    if is_valid(board, primary_moved) and is_valid(board, secondary_moved):
        return primary_moved
    else:
        return None


def rotate(board, block, turn_primary, clockwise):
    primary, secondary = block
    to_turn, center = (primary, secondary) if turn_primary else (secondary, primary)

    x = sub(to_turn, center)
    idx = deltas.index(x)

    for i in range(1, 3):
        to_turn = add(to_turn, deltas[(idx + clockwise * i) % 4])
        if not is_valid(board, to_turn):
            return None

    return sorted([to_turn, center])[0]


def is_arrived(block):
    for b in block:
        if b == (N - 1, N - 1):
            return True
    return False


def is_valid(board, pos):
    return 0 <= pos[0] < N and 0 <= pos[1] < N and board[pos[0]][pos[1]] != 1


def add(a, b):
    return tuple(a[i] + b[i] for i in range(len(a)))


def sub(a, b):
    return tuple(a[i] - b[i] for i in range(len(a)))


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))