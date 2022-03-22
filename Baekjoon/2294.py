import sys


scan = sys.stdin.readline


def get_input():
    n, k = map(int, scan().split())
    coins = [int(scan()) for _ in range(n)]
    return n, k, coins


def solution(n, k, coins):
    dp = [10001 for _ in range(100000 + 1)]
    for coin in coins:
        dp[coin] = 1
    dp[0] = 0

    for i in range(n):
        for j in range(coins[i], k + 1):
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)

    return dp[k] if dp[k] < 10001 else -1


sys.stdout.write("%d" % solution(*get_input()))