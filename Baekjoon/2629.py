import sys


scan = sys.stdin.readline


def solution():
    n_weight, weights = get_input()
    n_bead, beads = get_input()
    dp = [[0 for _ in range(n_weight + 1)] for _ in range(40001)]

    for i in range(1, n_weight + 1):
        dp[weights[i]][i] = True
        for j in range(1, 40001):
            dont = dp[j][i - 1]
            left = dp[j + weights[i]][i - 1] if j + weights[i] <= 40000 else 0
            right = dp[abs(j - weights[i])][i - 1] if abs(j - weights[i]) <= 40000 else 0
            dp[j][i] = dp[j][i] | dont | right | left

    for i in range(1, n_bead + 1):
        sys.stdout.write("%s " % ('Y' if dp[beads[i]][n_weight] else 'N'))


def get_input():
    n = int(scan())
    arr = [0] + list(map(int, scan().split()))
    return n, arr


solution()