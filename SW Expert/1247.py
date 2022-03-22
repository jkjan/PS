import math
import time
from copy import deepcopy

min_cost = 0

def solve():
    T = int(input())
    for t in range(1, T+1):
        tc()
        print("#%d %d" % (t, min_cost))


def tc():
    N, customers, company, home = get_input()
    # answer = dfs(N, customers, company, home)
    global min_cost
    min_cost = math.inf
    dfs_rec(N, [company], 0, [False for _ in range(N)], customers, home)
    # dfs(N, customers, company, home)
    # return answer


def get_input():
    N = int(input())
    customers = []
    pos = list(map(int, input().split()))

    company = (pos[0], pos[1])
    home = (pos[2], pos[3])

    for i in range(4, len(pos), 2):
        customers.append((pos[i], pos[i+1]))

    return N, customers, company, home


def dfs_rec(N, seq, i, visited, customers, home):
    global min_cost

    if i == N:
        min_cost = min(min_cost, calc_cost(N, seq + [home]))
        return

    for next_c in range(N):
        if not visited[next_c]:
            visited[next_c] = True
            dfs_rec(N, seq + [customers[next_c]], i + 1, visited, customers, home)
            visited[next_c] = False


def dfs(N, customers, company, home):
    global min_cost

    will_visit = [[[company], set(), 0]]

    while len(will_visit) > 0:
        [now_seq, now_visited, now_i] = will_visit.pop()

        if now_i == N:
            min_cost = min(min_cost, calc_cost(N, now_seq + [home]))
            continue

        for next_c in range(0, N):
            if next_c not in now_visited:
                will_visit.append([now_seq + [customers[next_c]], now_visited.union({next_c}), now_i + 1])


def calc_cost(N, seq):
    cost = 0
    for i in range(N + 1):
        from_, _to = seq[i], seq[i + 1]
        cost += abs(from_[0] - _to[0]) + abs(from_[1] - _to[1])
    return cost


solve()