import sys


def solution():
    t = int(sys.stdin.readline())
    for i in range(t):
        tc()


def tc():
    n, ps, s = get_input()
    songs = [[], []]
    qs = [0 for _ in range(n)]

    for i in range(n):
        songs[int(s[i])].append(ps[i])

    songs[0].sort()
    songs[1].sort()
    songs = songs[0] + songs[1]

    for i in range(n):
        qs[songs[i] - 1] = i + 1

    for i in range(n):
        print(qs[ps[i] - 1], end=' ')
    print()



def get_input():
    n = int(sys.stdin.readline())
    ps = list(map(int, sys.stdin.readline().split()))
    s = sys.stdin.readline()
    return n, ps, s


solution()