import math
import sys


scan = sys.stdin.readline


def solution():
    T = int(scan())
    for t in range(T):
        tc()


def tc():
    K, arr = get_input()
    sums = get_sums(K, arr)
    dp = [[0 for _ in range(K)] for _ in range(K)]

    for i in range(1, K):
        for j in range(K - i):
            dp[j][j + i] = math.inf
            for k in range(j, j + i):
                dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k+1][j + i])
            dp[j][j + i] += (sums[j + i] - sums[j] + arr[j])

    sys.stdout.write("%d\n" % dp[0][K-1])


def get_input():
    K = int(scan())
    arr = list(map(int, scan().split()))
    return K, arr


def get_sums(K, arr):
    sums = [0 for _ in range(K)]
    sums[0] = arr[0]
    for i in range(1, K):
        sums[i] = sums[i-1] + arr[i]
    return sums


solution()