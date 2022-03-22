from collections import deque


deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution():
    global snake, d
    snake = deque([(0, 0)])
    d = 1

    get_input()
    t = 0

    while move():
        t += 1
        rotate(t)

    print(t + 1)


def get_input():
    global N, board, rotate_info, snake_board
    N = int(input())
    K = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(K):
        r, c = map(lambda x: int(x) - 1, input().split())
        board[r][c] = 1

    L = int(input())
    rotate_info = [0 for _ in range(10001)]

    for i in range(L):
        [X, C] = input().split()
        rotate_info[int(X)] = (-1 if C == 'L' else 1)

    snake_board = [[False for _ in range(N)] for _ in range(N)]
    snake_board[0][0] = True


def move():
    head_y, head_x = snake[0]
    dy, dx = deltas[d]
    new_y, new_x = head_y + dy, head_x + dx

    if not is_valid(new_y, new_x):
        return False
    if snake_board[new_y][new_x]:
        return False

    snake.appendleft((new_y, new_x))
    snake_board[new_y][new_x] = True

    if board[new_y][new_x] != 1:
        tail_y, tail_x = snake.pop()
        snake_board[tail_y][tail_x] = False

    board[new_y][new_x] = 0

    return True


def is_valid(i, j):
    return 0 <= i < N and 0 <= j < N


def rotate(t):
    global d
    if t < len(rotate_info) and rotate_info[t] != 0:
        d += rotate_info[t]
        if d == -1:
            d = 3
        elif d == 4:
            d = 0


solution()