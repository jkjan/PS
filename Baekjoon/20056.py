N = 0
field = [[[]]]

deltas = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def solution():
    fireballs, K = get_input()
    init_field(fireballs)

    for k in range(K):
        move_all()
        merge()

    fireball_sum = get_sum()
    print(fireball_sum)


def get_sum():
    fireball_sum = 0

    for i in range(N):
        for j in range(N):
            for [m, s, d] in field[i][j]:
                fireball_sum += m

    return fireball_sum


def get_input():
    global N
    N, M, K = map(int, input().split())
    fireballs = [list(map(int, input().split())) for _ in range(M)]
    return fireballs, K


def init_field(fireballs):
    global field
    field = [[[] for _ in range(N)] for _ in range(N)]

    for [r, c, m, s, d] in fireballs:
        field[r-1][c-1].append([m, s, d])


def move(i, j, s, d):
    next_ij = []

    for e, idx in enumerate([i, j]):
        next_idx = idx + (deltas[d][e] * s) % N
        if next_idx >= N:
            next_idx = next_idx - N
        elif next_idx < 0:
            next_idx = next_idx + N
        next_ij.append(next_idx)

    [next_i, next_j] = next_ij

    return next_i, next_j


def move_all():
    will_move = []

    for i in range(N):
        for j in range(N):
            while len(field[i][j]) > 0:
                [m, s, d] = field[i][j].pop()
                next_i, next_j = move(i, j, s, d)
                will_move.append([next_i, next_j, m, s, d])

    for [next_i, next_j, m, s, d] in will_move:
        field[next_i][next_j].append([m, s, d])


def merge():
    for i in range(N):
        for j in range(N):
            if len(field[i][j]) >= 2:
                cnt = len(field[i][j])
                m_sum, s_sum = 0, 0

                cnt_even = 0
                cnt_odd = 0

                while len(field[i][j]) > 0:
                    [m, s, d] = field[i][j].pop()
                    m_sum += m
                    s_sum += s

                    cnt_even += (d % 2 == 0)
                    cnt_odd += (d % 2 == 1)

                m_sum = m_sum // 5
                s_sum = s_sum // cnt

                if cnt_odd == cnt or cnt_even == cnt:
                    next_deltas = [0, 2, 4, 6]
                else:
                    next_deltas = [1, 3, 5, 7]

                if m_sum != 0:
                    for f in range(4):
                        field[i][j].append([m_sum, s_sum, next_deltas[f]])


solution()