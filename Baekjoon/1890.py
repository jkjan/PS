

def solution():
    N, game_table = get_input()

    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if dp[i][j] > 0 and game_table[i][j] > 0:
                to_add = dp[i][j]
                to_jump = game_table[i][j]
                add_cases(dp, to_add, i + to_jump, j, N)
                add_cases(dp, to_add, i, j + to_jump, N)

    answer = dp[N-1][N-1]
    return answer


def add_cases(dp, to_add, i, j, N):
    if is_valid(i, N) and is_valid(j, N):
        dp[i][j] += to_add


def is_valid(x, N):
    return 0 <= x < N


def get_input():
    N = int(input())
    game_table = [list(map(int, input().split())) for _ in range(N)]
    return N, game_table


print(solution())