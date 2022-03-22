# https://programmers.co.kr/learn/courses/30/lessons/12952\

from collections import deque

def solution(n):
    cnt = [0]
    for i in range(1, n + 1):
        bfs(n, i, cnt)
    return cnt[0]


def bfs(n, start, cnt):
    will_visit = deque([[1 << (start - 1), [start]]])
    while 0 < len(will_visit):
        [mask, path] = will_visit.popleft()
        if mask == pow(2, n) - 1:
            cnt[0] += 1

        for i in range(1, n + 1):
            if (mask >> (i - 1)) % 2 == 0:
                possible = True
                for pi, p in enumerate(path):
                    if abs(i - p) == len(path) - pi:
                        possible = False
                if possible:
                    i_bit = 1 << (i - 1)
                    will_visit.append([mask + i_bit, path + [i]])


n = 12
print(solution(n))