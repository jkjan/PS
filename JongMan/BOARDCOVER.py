import sys


scan = sys.stdin.readline
blocks = [[(1, 0), (1, 1)], [(1, 0), (1, -1)], [(0, 1), (1, 1)], [(0, 1), (1, 0)]]


def solution():
    T = int(scan())

    for t in range(T):
        tc()


def tc():
    def is_valid(i, j):
        return 0 <= i < H and 0 <= j < W

    def fill(to_fill, what):
        for y, x in to_fill:
            board[y][x] = what

    def dfs(i, j, white_left):
        while True:
            if j >= W:
                i += 1
                j = 0
                if i >= H:
                    if white_left == 0:
                        return 1
                    else:
                        return 0

            if board[i][j] == '.':
                break
            j += 1

        cnt = 0
        for to_fill in blocks:
            to_fill = [(y, x) for y, x in [(i + dy, j + dx) for dy, dx in to_fill + [(0, 0)] ] if is_valid(y, x) and board[y][x] == '.']
            if len(to_fill) == 3:
                fill(to_fill, '#')
                cnt += dfs(i, j + 1, white_left - len(to_fill))
                fill(to_fill, '.')

        return cnt

    H, W = map(int, scan().split())
    board = [list(scan().strip()) for _ in range(H)]
    white = sum([sum([board[y][x] == '.' for x in range(W)]) for y in range(H)])

    if white % 3 == 0:
        answer = dfs(0, 0, white)
    else:
        answer = 0

    sys.stdout.write("%d\n" % answer)


solution()