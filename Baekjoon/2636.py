import sys
from collections import deque


delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

N, M = map(int, sys.stdin.readline().split())
rc = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        cnt += rc[i][j]


def bfs():
    global cnt
    will_visit = deque()
    will_visit.append((0, 0))
    visited = [[False for i in range(M)] for j in range(N)]
    visited[0][0] = True
    melt = []
    while len(will_visit) != 0:
        (ni, nj) = will_visit.popleft()
        for (di, dj) in delta:
            vi, vj = ni + di, nj + dj
            if 0 <= vi < N and 0 <= vj < M \
                and not visited[vi][vj]:
                if not rc[vi][vj]:
                    will_visit.append((vi, vj))
                else:
                    melt.append((vi, vj))
                visited[vi][vj] = True

    for (mi, mj) in melt:
        rc[mi][mj] = 0
        cnt -= 1


hour = 0
prev = cnt
while True:
    bfs()
    hour += 1
    if cnt == 0:
        break
    prev = cnt

print(hour)
print(prev)