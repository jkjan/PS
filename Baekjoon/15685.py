board = [[False for _ in range(101)] for _ in range(101)]
delta = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def solution():
    dragon_curves = get_input()

    for dragon_curve in dragon_curves:
        draw_dragon_curve(dragon_curve)

    cnt = count_surrounded_squares()
    print(cnt)


def get_input():
    N = int(input())
    dragon_curves = []
    for _ in range(N):
        dragon_curve_info = map(int, input().split())
        dragon_curves.append(get_dragon_curve(*dragon_curve_info))
    return dragon_curves


def rotate(ai, aj, ei, ej):
    return ei - (ej - aj), ej + (ei - ai)


def make_next_dragon_curve(dragon_pos):
    dl = len(dragon_pos)
    for i in range(dl - 2, -1, -1):
        curved = rotate(*dragon_pos[i], *dragon_pos[dl - 1])
        dragon_pos.append(curved)


def get_dragon_curve(x, y, d, g):
    dragon_curve = [(y, x), (y + delta[d][0], x + delta[d][1])]
    for _ in range(g):
        make_next_dragon_curve(dragon_curve)
    return dragon_curve


def draw_dragon_curve(dragon_curve):
    for dc_y, dc_x in dragon_curve:
        if 0 <= dc_y <= 100 and 0 <= dc_x <= 100:
            board[dc_y][dc_x] = True


def count_surrounded_squares():
    cnt = 0
    for i in range(0, 100):
        for j in range(0, 100):
            dragon_cnt = board[i][j] + board[i][j+1] + board[i+1][j] + board[i+1][j+1]
            cnt += (dragon_cnt == 4)
    return cnt


solution()