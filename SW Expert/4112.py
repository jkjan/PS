from collections import deque


LIMIT = 10000


def solve():
    T = int(input())
    for t in range(1, T+1):
        print("#%d %d" % (t, tc()))


def tc():
    a, b = map(int, input().split())
    return bfs(a, b)


def get_first_num(level):
    return ((level ** 2) - level + 2) // 2


def get_level(x):
    s = 1
    e = 142
    while s <= e:
        m = (s + e) // 2
        if get_first_num(m) <= x:
            s = m + 1
        else:
            e = m - 1
    return e


def bfs(start, end):
    will_visit = deque([[start, 0]])
    visited = [False for _ in range(0, LIMIT + 1)]
    visited[start] = True

    def go_if_able(adj, time, from_, _to):
        if 1 <= adj <= LIMIT and from_ <= adj < _to and not visited[adj]:
            visited[adj] = True
            will_visit.append([adj, time + 1])


    while len(will_visit) > 0:
        [now_visit, now_time] = will_visit.popleft()

        if now_visit == end:
            return now_time
        elif now_visit > LIMIT:
            continue

        level = get_level(now_visit)

        prev_first = get_first_num(level-1)
        now_first = get_first_num(level)
        next_first = get_first_num(level + 1)
        next_next_first = get_first_num(level + 2)

        go_if_able(now_visit - level, now_time, prev_first, now_first)
        go_if_able(now_visit - level + 1, now_time, prev_first, now_first)
        go_if_able(now_visit - 1, now_time, now_first, next_first)
        go_if_able(now_visit + 1, now_time, now_first, next_first)
        go_if_able(now_visit + level, now_time, next_first, next_next_first)
        go_if_able(now_visit + level + 1, now_time, next_first, next_next_first)


solve()