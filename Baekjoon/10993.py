delta = [(1, 1), (-1, 1), (0, -1), -1]


def draw_triangle(n):
    k = 2 ** (n + 1) - 1
    k_ = 2 * k - 1
    board = [[False for _ in range(k_)] for _ in range(k)]

    if n % 2 == 0:
        d = 1
        y, x = 0, 0
    else:
        d = -1
        y, x = k - 1, k_ - 1

    for i in range(n):
        for j in range(3):
            dy, dx = d * delta[j][0], d * delta[j][1]
            for l in range(k):
                board[y][x] = True
                y, x = y + dy, x + dx

            y, x = y - dy, x - dx

        d *= -1