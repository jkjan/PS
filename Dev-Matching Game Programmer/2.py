



def solution(h, w, n, board):
    answer = 0
    deltas = [(0, 1), (1, 1), (1, 0), (1, -1)]
    visited = [[[False for _ in range(4)] for _ in range(w)] for _ in range(h)]
    dp = [[[0 for _ in range(4)] for _ in range(w)] for _ in range(h)]

    def is_valid(i, j):
        return 0 <= i < h and 0 <= j < w

    def dfs(i, j, cnt, direction):
        print(i, j, cnt, direction)

        for next_dir in range(4):
            dy, dx = deltas[next_dir]
            adj_i, adj_j = i + dy, j + dx

            if is_valid(adj_i, adj_j) and board[adj_i][adj_j] == '1':
                if not visited[adj_i][adj_j][next_dir]:
                    visited[adj_i][adj_j][next_dir] = True
                    next_cnt = 2 if direction != next_dir else cnt + 1
                    dfs(adj_i,adj_j, next_cnt, next_dir)
                    dp[i][j][next_dir] = dp[adj_i][adj_j][next_dir] + 1
                else:
                    new_n = dp[i][j][next_dir] + dp[adj_i][adj_j][next_dir]
                    if new_n > n:
                        dp[adj_i][adj_j][next_dir] = 0

            elif (not is_valid(adj_i, adj_j) or (is_valid(adj_i, adj_j) and board[adj_i][adj_j] == '0')) and direction == next_dir:
                dp[i][j][direction] = 1


    for i in range(h):
        for j in range(w):
            for d in range(4):
                if board[i][j] == '1' and not visited[i][j][d]:
                    visited[i][j][d] = True
                    dfs(i, j, 1, d)

    for i in range(h):
        for j in range(w):
            for d in range(4):
                answer += dp[i][j][d] == n

    for d in range(4):
        for i in range(h):
            for j in range(w):
                print(dp[i][j][d], end='')
            print()
        print()

    return answer


h, w, n = 7, 9, 4

board = ["111100000",
         "000010011",
         "111100011",
         "111110011",
         "111100011",
         "111100010",
         "111100000"]

"""
h, w, n = 5, 5, 5
board = ["11111",
         "11111",
         "11111",
         "11111",
         "11111"
         ]
"""

print(solution(h, w, n, board))