from collections import deque, defaultdict


def solution(board, r, c):
    def dfs(i, now_pos, cnt):
        nonlocal answer
        if i == len_card:
            answer = min(answer, cnt)
            return

        for adj in range(len_card):
            if not visited[adj]:
                for j in range(2):
                    s1 = card_pos[cards[adj]][j]
                    s2 = card_pos[cards[adj]][j-1]
                    dist = get_min_dist(now_pos, s1) + get_min_dist(s1, s2) + 2

                    if cnt + dist < answer:
                        visited[adj] = True
                        dfs(i + 1, s2, cnt + dist)
                        visited[adj] = False

                    for py, px in card_pos[cards[adj]]:
                        board[py][px] = cards[adj]


    def is_valid(i, j):
        is_in = lambda x: 0 <= x < N
        return is_in(i) and is_in(j)


    def get_next_node(now_y, now_x):
        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx

            if is_valid(adj_y, adj_x):
                yield adj_y, adj_x

                while True:
                    if not is_valid(adj_y, adj_x):
                        adj_y -= dy
                        adj_x -= dx
                        break
                    if board[adj_y][adj_x]:
                        break
                    adj_y += dy
                    adj_x += dx

                yield adj_y, adj_x


    def get_min_dist(start, end):
        will_visit = deque([(start, 0)])
        check = {start}

        while will_visit:
            (now_y, now_x), now_dist = will_visit.popleft()

            if (now_y, now_x) == end:
                board[now_y][now_x] = 0
                return now_dist

            for adj in get_next_node(now_y, now_x):
                if adj not in check:
                    check.add(adj)
                    will_visit.append((adj, now_dist + 1))


    def get_card_pos():
        nonlocal card_pos
        for i in range(4):
            for j in range(4):
                if board[i][j]:
                    card_pos[board[i][j]].append((i, j))


    N = 4
    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    answer = float("inf")
    card_pos = defaultdict(list)
    get_card_pos()
    cards = list(card_pos.keys())
    len_card = len(card_pos)
    visited = [False for _ in range(len_card)]
    dfs(0, (r, c), 0)

    return answer