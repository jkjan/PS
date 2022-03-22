import sys
import math


scan = sys.stdin.readline


def solution():
    N = int(scan())
    arr = [list(map(int, scan().split())) for _ in range(N)]

    dp = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(1, N):
        for j in range(N - i):
            dp[j][j + i] = math.inf
            for k in range(j, j + i):
                dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k+1][j + i] + arr[j][0] * arr[k][1] * arr[j + i][1])

    sys.stdout.write("%d" % dp[0][N-1])


solution()