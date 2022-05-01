from collections import deque


deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

dice = []

to_change = [[(1, 0), (1, 1), (1, 2), (3, 1)],
             [(0, 1), (1, 1), (2, 1), (3, 1)]]

N, M, K = 0, 0, 0
field = []
dp = [[0]]
now_d = 0
now_y, now_x = 0, 0
score = 0


def solution():
    get_input()

    for k in range(K):
        move_dice()

    print(score)


def get_input():
    global N, M, K, dp, now_d, now_y, now_x, score, dice
    N, M, K = map(int, input().split())
    for i in range(N):
        field.append(list(map(int, input().split())))

    dp = [[-1 for _ in range(M)] for _ in range(N)]
    now_d = 0
    now_y, now_x = 0, 0
    score = 0

    dice = [[0, 2, 0],
            [4, 1, 3],
            [0, 5, 0],
            [0, 6, 0]]


def roll_dice(d):
    global now_y, now_x, now_d

    adj_y, adj_x = now_y + deltas[d][0], now_x + deltas[d][1]
    if not is_valid(adj_y, adj_x):
        if d % 2:
            d -= 1
        else:
            d += 1

    now_change = to_change[d >= 2]
    q = deque([dice[ny][nx] for ny, nx in now_change])
    if d % 2:
        x = q.popleft()
        q.append(x)
    else:
        x = q.pop()
        q.appendleft(x)
    for ny, nx in now_change:
        x = q.popleft()
        dice[ny][nx] = x

    now_y += deltas[d][0]
    now_x += deltas[d][1]
    now_d = d


def get_score(s_i, s_j):
    if dp[s_i][s_j] != -1:
        return dp[s_i][s_j] * field[s_i][s_j]

    def dfs(i, j):
        cluster.append((i, j))
        for dy, dx in deltas:
            adj_y, adj_x = i + dy, j + dx
            if not is_valid(adj_y, adj_x):
                continue
            if visited[adj_y][adj_x]:
                continue
            if field[adj_y][adj_x] != field[s_i][s_j]:
                continue
            visited[adj_y][adj_x] = True
            dfs(adj_y, adj_x)

    visited = [[False for _ in range(M)] for _ in range(N)]
    cluster = []
    visited[s_i][s_j] = True
    dfs(s_i, s_j)

    for c_i, c_j in cluster:
        dp[c_i][c_j] = len(cluster)

    return len(cluster) * field[s_i][s_j]


def is_valid(i, j):
    return 0 <= i < N and 0 <= j < M


def determine_direction():
    global now_d
    A = dice[3][1]
    B = field[now_y][now_x]
    if A > B:
        if now_d == 0:
            now_d = 2
        elif now_d == 3:
            now_d = 0
        elif now_d == 1:
            now_d = 3
        else:
            now_d = 1
    elif A < B:
        if now_d == 0:
            now_d = 3
        elif now_d == 3:
            now_d = 1
        elif now_d == 1:
            now_d = 2
        else:
            now_d = 0


def move_dice():
    global score
    roll_dice(now_d)
    score += get_score(now_y, now_x)
    determine_direction()


solution()
