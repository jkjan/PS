from collections import deque


ERASED = 'x'
N = M = 0
circles = []
xdks = []
deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cnt_circles = 0


def solution():
    get_input()

    for xdk in xdks:
        special_rotate(*xdk)
        if cnt_circles == 0:
            break

    answer = get_sum_circles()
    return answer


def get_input():
    global N, M, circles, xdks, cnt_circles
    N, M, T = map(int, input().split())
    circles = []
    xdks = []

    for i in range(N):
        circles.append(list(map(int, input().split())))

    for i in range(T):
        xdks.append(list(map(int, input().split())))

    cnt_circles = N * M


def special_rotate(x, d, k):
    rotate(x, d, k)
    erased = erase()

    if not erased:
        normalize()


def rotate(x, d, k):
    for i, circle in enumerate(circles):
        if (i + 1) % x == 0:
            rotate_circle(i, d, k)


def rotate_circle(i, d, k):
    k = k % M

    if d == 0:
        circles[i] = circles[i][-k:] + circles[i][:-k]
    else:
        circles[i] = circles[i][k:] + circles[i][:k]


def erase():
    global cnt_circles
    visited = [[False for _ in range(M)] for _ in range(N)]
    group = []

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and circles[i][j] != ERASED:
                visited[i][j] = True
                group += get_group(visited, (i, j))

    if len(group) > 0:
        for gi, gj in group:
            circles[gi][gj] = ERASED
            cnt_circles -= 1
        return True
    return False


def get_group(visited, start):
    start_val = circles[start[0]][start[1]]
    will_visit = deque([start])
    group = []

    while len(will_visit) > 0:
        now_y, now_x = will_visit.popleft()
        group.append((now_y, now_x))

        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx

            if adj_x == M:
                adj_x = 0
            if adj_x == -1:
                adj_x = M - 1

            if not is_valid(adj_y, adj_x):
                continue
            if visited[adj_y][adj_x]:
                continue
            if circles[adj_y][adj_x] != start_val:
                continue

            visited[adj_y][adj_x] = True
            will_visit.append((adj_y, adj_x))

    if len(group) > 1:
        return group
    else:
        return []


def is_valid(i, j):
    return 0 <= i < N and 0 <= j < M


def get_sum_circles():
    sum_circles = 0
    for i in range(N):
        for j in range(M):
            if circles[i][j] != ERASED:
                sum_circles += circles[i][j]

    return sum_circles


def normalize():
    sum_circles = get_sum_circles()
    mean_circles = sum_circles / cnt_circles

    for i in range(N):
        for j in range(M):
            if circles[i][j] != ERASED:
                if circles[i][j] > mean_circles:
                    circles[i][j] -= 1
                elif circles[i][j] < mean_circles:
                    circles[i][j] += 1


print(solution())