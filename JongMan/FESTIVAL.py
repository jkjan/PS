# https://algospot.com/judge/problem/read/FESTIVAL

import sys


def solve():
    T = int(sys.stdin.readline().strip())
    for i in range(T):
        tc()


def tc():
    N, L = map(int, sys.stdin.readline().split())
    costs = list(map(int, sys.stdin.readline().split()))
    min_avg = 101

    for i in range(N - L + 1):
        j = 0
        now_sum = 0
        while i + j < N:
            now_sum += costs[i + j]
            if j + 1 >= L:
                min_avg = min(min_avg, (now_sum / (j + 1)))
            j += 1

    sys.stdout.write("%.8f\n" % min_avg)


solve()