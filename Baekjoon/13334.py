import sys


def solution():
    terms, d = get_input()
    answer = 0
    add = []

    for i in range(len(terms)):
        a, b = terms[i]
        if b - a <= d:
            add.append((a, 1))
            add.append((b - d, -1))

    now_cnt = 0
    add.sort()

    for i in range(len(add)):
        now_cnt -= add[i][1]
        answer = max(now_cnt, answer)

    sys.stdout.write("%d" % answer)


def get_input():
    n = int(sys.stdin.readline())
    terms = []

    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        if b < a: a, b = b, a
        terms.append((a, b))

    d = int(sys.stdin.readline())

    return terms, d


solution()
