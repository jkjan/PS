import sys


def solution():
    get_input()
    houses.sort()

    s = min([houses[i + 1] - houses[i] for i in range(len(houses) - 1)])
    e = houses[-1] - houses[0]

    while s <= e:
        m = (s + e) // 2
        if is_possible(m):
            s = m + 1
        else:
            e = m - 1

    sys.stdout.write("%d" % e)


def get_input():
    global N, C, houses
    N, C = map(int, sys.stdin.readline().split())
    houses = [int(sys.stdin.readline()) for _ in range(N)]


def is_possible(x):
    prev = houses[0]
    k = 1

    i = 1
    while i < N and k < C:
        if houses[i] - prev >= x:
            prev = houses[i]
            k += 1
        i += 1

    return k == C


solution()
