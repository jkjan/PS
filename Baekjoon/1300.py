import sys


def solution():
    get_input()

    s = 1
    e = N ** 2

    while s <= e:
        m = (s + e) // 2
        if get_under(m) < k:
            s = m + 1
        else:
            e = m - 1

    sys.stdout.write("%d" % s)


def get_input():
    global N, k
    N = int(sys.stdin.readline())
    k = int(sys.stdin.readline())


def get_under(x):
    cnt = 0
    for i in range(1, min(N, x) + 1):
        cnt += min(x // i, N)
    return cnt


solution()

"""
1 2 2 3 3 4 6 6 9
1 2 3 4 5 6 7 8 9

1 2 3
2 4
3

"""