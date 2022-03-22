import sys
from collections import deque


deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution():
    T = int(sys.stdin.readline())
    for t in range(T):
        tc()


def tc():
    building, keys = get_input()
    is_keys = init_key(keys)
    sys.stdout.write("%d\n" % bfs(building, is_keys))


def get_input():
    h, w = map(int, sys.stdin.readline().split())

    building = ['.' * (w + 2)]
    for i in range(h):
        building.append('.' + sys.stdin.readline().strip() + '.')
    building.append('.' * (w + 2))

    keys = sys.stdin.readline().strip()

    return building, keys


def init_key(keys):
    is_key = [False for _ in range(26)]

    if keys != '0':
        for k in keys:
            is_key[ord(k) - ord('a')] = True

    return is_key


def bfs(building, is_key):
    h, w = len(building), len(building[0])
    will_visit = deque([(0, 0)])
    visited = [[False for _ in range(w)] for _ in range(h)]
    needed_key = [deque() for _ in range(26)]
    doc_cnt = 0

    while len(will_visit) > 0:
        now_y, now_x = will_visit.popleft()

        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx

            if not is_valid(h, w, adj_y, adj_x):
                continue
            if visited[adj_y][adj_x]:
                continue
            if building[adj_y][adj_x] == '*':
                continue
            if building[adj_y][adj_x] == '$':
                doc_cnt += 1

            if building[adj_y][adj_x].isupper():
                key = ord(building[adj_y][adj_x]) - ord('A')

                if not is_key[key]:
                    needed_key[key].append((adj_y, adj_x))
                    continue

            if building[adj_y][adj_x].islower():
                key = ord(building[adj_y][adj_x]) - ord('a')

                if not is_key[key]:
                    is_key[key] = True

                    while len(needed_key[key]) > 0:
                        will_visit.appendleft(needed_key[key].pop())

            visited[adj_y][adj_x] = True
            will_visit.append((adj_y, adj_x))

    return doc_cnt


def is_valid(h, w, i, j):
    return 0 <= i < h and 0 <= j < w


solution()