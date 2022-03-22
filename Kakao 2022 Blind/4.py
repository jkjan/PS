from collections import deque


def solution(n, info):
    total_path = bfs(n, info)

    total_score = [(score(path, info), path) for path in total_path]
    total_score.sort(key=lambda x: (x[0], "".join(str(x[1]))[::-1]), reverse=True)

    if len(total_score) == 0 or total_score[0][0] <= 0:
        return [-1]

    return total_score[0][1]


def bfs(n, info):
    will_visit = deque([[10, n, []]])
    total_path = []

    while len(will_visit) > 0:
        [now_visit, arrow_left, path] = will_visit.popleft()

        if now_visit == -1:
            if arrow_left > 0:
                path[10] += arrow_left

            total_path.append(path)
            continue

        shoot = info[10 - now_visit] + 1

        if shoot <= arrow_left:
            will_visit.append([now_visit - 1, arrow_left - shoot, path + [shoot]])

        will_visit.append([now_visit - 1, arrow_left, path + [0]])

    return total_path


def score(path, info):
    apeach = 0
    ryan = 0

    for i in range(10, 0, -1):
        if path[10 - i] > 0 or info[10 - i] > 0:
            if path[10 - i] > info[10 - i]:
                ryan += i
            else:
                apeach += i

    return ryan - apeach


n = 1
info = 		[1,0,0,0,0,0,0,0,0,0,0]
print(solution(n, info))