import math
import sys


def solution():
    get_input()

    global dp
    dp = [[math.inf for _ in range(2 ** N)] for _ in range(N)]
    print(dfs(0, 1))


def dfs(now, so_far):
    if so_far == 2 ** N - 1:
        if adj_matrix[now][0] == 0:
            return math.inf
        return adj_matrix[now][0]

    if dp[now][so_far] != math.inf:
        return dp[now][so_far]

    for adj in range(N):
        if adj_matrix[now][adj] > 0 and so_far & (1 << adj) == 0:
            if_visit = so_far | (1 << adj)
            dp[now][so_far] = min(dp[now][so_far], dfs(adj, if_visit) + adj_matrix[now][adj])

    return dp[now][so_far]


def get_input():
    global N, adj_matrix
    N = int(sys.stdin.readline())
    adj_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    return N, adj_matrix


solution()