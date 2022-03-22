from collections import deque


def solution(places):
    answer = [is_safe(place) for place in places]
    return answer


def is_safe(place):
    participants = get_participants(place)

    deltas = [
        (-1, 0), (0, 1), (1, 0), (0, -1)
    ]

    for p in participants:
        if not bfs(p, place, deltas):
            return 0

    return 1


def get_participants(place):
    participants = []

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                participants.append((i, j))

    return participants


def is_valid(idx):
    return 0 <= idx < 5


def bfs(start, place, deltas):
    will_visit = deque([start])

    dist = [[-1 for _ in range(5)] for _ in range(5)]

    dist[start[0]][start[1]] = 0

    while len(will_visit) > 0:
        now_y, now_x = will_visit.popleft()

        if (now_y, now_x) != start and place[now_y][now_x] == 'P' and dist[now_y][now_x] <= 2:
            return False

        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx

            if is_valid(adj_y) + is_valid(adj_x) < 2:
                continue

            if dist[adj_y][adj_x] != -1:
                continue

            if place[adj_y][adj_x] == 'X':
                continue

            dist[adj_y][adj_x] = dist[now_y][now_x] + 1

            will_visit.append((adj_y, adj_x))

    return True


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))