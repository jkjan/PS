from collections import deque
from copy import deepcopy


MAX = 13



def bfs(a, b, m):
    will_visit = deque([[b, 0, 0]])
    while will_visit:
        [now_b, now_m, now_cnt] = will_visit.popleft()
        a.sort(); now_b.sort()
        if a == now_b:
            return now_cnt

        next_b = [(aa, bb) for [aa, bb] in now_b]
        now_b_set = set([(aa, bb) for [aa, bb] in now_b])
        for j in range(len(b)):
            for k in range(len(b)):
                if (j, k) not in now_b_set:
                    for l, ll in next_b:
                        now_b_set.remove((l, ll))
                        now_b_set.add((j, k))
                        next_bb = [[bi, bj] for bi, bj in list(now_b_set)]
                        will_visit.append([next_bb, now_m, now_cnt + 1])
                        now_b_set.add((l, ll))
                        now_b_set.remove((j, k))

        for j in range(len(b)):
            for k in range(len(b)):
                if j == k: continue
                for l in range(len(b)):
                    if b[l][0] == j:
                        b[l][0] = k
                    elif b[l][1] == j:
                        b[l][1] = k
                    elif b[l][0] == k:
                        b[l][0] = j
                    elif b[l][1] == k:
                        b[l][1] = j
                next_b = deepcopy(b)
                will_visit.append([next_b, now_m + 1, now_cnt])
                for l in range(len(b)):
                    if b[l][0] == k:
                        b[l][0] = j
                    elif b[l][1] == k:
                        b[l][1] = j
                    elif b[l][0] == j:
                        b[l][0] = k
                    elif b[l][1] == j:
                        b[l][1] = k
    return -1

def solution(a, b, m):
    return bfs(a, b, m)


a = [[1, 2], [3, 1], [2, 4], [3, 5]]
b = [[2, 1], [4, 1], [2, 5], [3, 2]]
m = 1
print(solution(a, b, m))