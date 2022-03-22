# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    dp[1][1] = 1
    for [pi, pj] in puddles:
        dp[pi][pj] = -1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 1 and j == 1:
                continue
            if dp[i][j] != -1:
                dp[i][j] = ((dp[i][j-1] if dp[i][j-1] > 0 else 0) +
                           (dp[i-1][j] if dp[i-1][j] > 0 else 0)) % 1_000_000_007
    return dp[m][n]


m = 1
n = 2
puddles = []

print(solution(m, n, puddles))