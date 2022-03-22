from collections import deque


def solution():
    T = int(input())
    for t in range(1, T + 1):
        answer = tc()
        print("#%d %d" % (t, answer))


def tc():
    D, W, K, films = get_input()
    bfs(D, W, K, films)
    return 0


def get_input():
    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]
    return D, W, K, films


def bfs(D, W, K, films):
    will_visit = deque([[]])

    while len(will_visit) > 0:
        inject_to = will_visit.popleft()

        if len(inject_to) == K:
            continue

        last = -1 if len(inject_to) == 0 else inject_to[-1]

        for next_i in range(last + 1, D):
            will_visit.append(inject_to + [next_i])


def check(inject_to, D, W, K, films):
    

solution()