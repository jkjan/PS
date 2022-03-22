def solution(money):
    N = len(money)
    dp = [[0 for _ in range(N)] for _ in range(2)]

    dp[0][0:2] = [money[0], money[0]]
    dp[1][0:2] = [0, money[1]]

    for i in range(2):
        for j in range(2, N - 1):
            dp[i][j] = max(dp[i][j - 2] + money[j], dp[i][j - 1])

    dp[0][N - 1] = dp[0][N - 2]
    dp[1][N - 1] = max(dp[1][N - 3] + money[N - 1], dp[1][N - 2])

    answer = max(dp[0][N - 1], dp[1][N - 1])
    return answer


money = [1, 7, 3]
print(solution(money))