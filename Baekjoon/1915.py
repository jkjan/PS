import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
    max_area = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                if i >= 1 and j >= 1:
                    arr[i][j] += min([arr[i-1][j-1], arr[i-1][j], arr[i][j-1]])
                max_area = max(max_area, arr[i][j] ** 2)

    sys.stdout.write("%d" % max_area)


solution()
