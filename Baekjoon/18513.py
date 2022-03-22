from collections import deque


def solution():
    N, K, springs = get_input()
    return bfs(springs, K)


def get_input():
    N, K = map(int, input().split())
    springs = list(map(int, input().split()))
    return N, K, springs


def bfs(springs, K):
    will_visit = deque([(s, s) for s in springs])
    visited = set()

    for s in springs:
        visited.add(s)

    cnt = 0
    unhappy_rate = 0

    while len(will_visit) > 0:
        now = will_visit.popleft()

        now_visit, now_from = now

        for adj in [now_visit - 1, now_visit + 1]:
            if adj in visited:
                continue
            visited.add(adj)
            will_visit.append((adj, now_from))
            cnt += 1
            unhappy_rate += abs(now_from - adj)

            if cnt == K:
                return unhappy_rate


    return unhappy_rate


print(solution())