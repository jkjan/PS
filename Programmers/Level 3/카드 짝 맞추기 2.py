from collections import deque, defaultdict


N = 4
deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = float("inf")


def solution(board, r, c):
    global len_card, answer, cards
    get_card_pos(board)
    len_card = len(card_pos)
    cards = list(card_pos.keys())
    visited = [False for _ in range(len_card)]
    dfs(board, visited, 0, r, c, 0)
    return answer


def dfs(board, visited, i, now_r, now_c, cnt):
    global answer
    if i == len_card:
        answer = min(answer, cnt)
        return

    for adj in range(len_card):
        if not visited[adj]:

            for j in range(2):
                s0 = now_r, now_c
                s1 = card_pos[cards[adj]][j]
                s2 = card_pos[cards[adj]][j-1]
                dist = get_min_dist(board, *s0, *s1) + get_min_dist(board, *s1, *s2) + 2

                if cnt + dist < answer:
                    visited[adj] = True
                    dfs(board, visited, i + 1, *s2, cnt + dist)
                    visited[adj] = False

                for py, px in card_pos[cards[adj]]:
                    board[py][px] = cards[adj]


def get_card_pos(board):
    global card_pos
    card_pos = defaultdict(lambda: [])
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                card_pos[board[i][j]].append((i, j))


def add_to_queue(will_visit, visited, i, j, dist):
    if not visited[i][j]:
        visited[i][j] = True
        will_visit.append((i, j, dist + 1))


def get_min_dist(board, sy, sx, ey, ex):
    will_visit = deque([(sy, sx, 0)])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[sy][sx] = True

    while will_visit:
        now_y, now_x, now_dist = will_visit.popleft()

        if (now_y, now_x) == (ey, ex):
            board[now_y][now_x] = 0
            return now_dist

        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx

            if is_valid(adj_y, adj_x):
                add_to_queue(will_visit, visited, adj_y, adj_x, now_dist)

                while True:
                    if not is_valid(adj_y, adj_x):
                        adj_y -= dy
                        adj_x -= dx
                        break
                    if board[adj_y][adj_x]:
                        break
                    adj_y += dy
                    adj_x += dx

                add_to_queue(will_visit, visited, adj_y, adj_x, now_dist)


def is_valid(i, j):
    is_in = lambda x: 0 <= x < N
    return is_in(i) and is_in(j)


board, r, c = [[1, 5, 0, 2], [6, 4, 3, 0], [0, 2, 1, 5], [3, 0, 6, 4]], 0, 0

print(solution(board, r, c))