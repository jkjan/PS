N = 0
n_students = 0
fav_friends = [[]]
students = []
deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution():
    get_input()
    classroom = place_students()
    satisfaction_score = get_satisfaction_score(classroom)
    print(satisfaction_score)


def get_input():
    global N, n_students, fav_friends
    N = int(input())
    n_students = N ** 2
    fav_friends = [[] for _ in range(n_students + 1)]

    for i in range(1, n_students + 1):
        input_line = list(map(int, input().split()))
        students.append(input_line[0])
        fav_friends[input_line[0]] = input_line[1:]


def get_score(i, j, student, classroom):
    fav_cnt = 0
    empty_cnt = 0

    for dy, dx in deltas:
        adj_y, adj_x = i + dy, j + dx

        if is_valid(adj_y, adj_x):
            if classroom[adj_y][adj_x] == 0:
                empty_cnt += 1
            elif classroom[adj_y][adj_x] in fav_friends[student]:
                fav_cnt += 1

    return [fav_cnt, empty_cnt, i, j]


def is_valid(i, j):
    return 0 <= i < N and 0 <= j < N


def find_spot(student, classroom):
    scores = []

    for i in range(N):
        for j in range(N):
            if classroom[i][j] == 0:
                scores.append(get_score(i, j, student, classroom))

    scores.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))

    spot_i = scores[0][2]
    spot_j = scores[0][3]

    return spot_i, spot_j


def place_students():
    classroom = [[0 for _ in range(N)] for _ in range(N)]

    for student in students:
        spot_i, spot_j = find_spot(student, classroom)
        classroom[spot_i][spot_j] = student

    return classroom


def get_satisfaction_score(classroom):
    satisfaction_score = 0

    for i in range(N):
        for j in range(N):
            fav_cnt = 0

            for dy, dx in deltas:
                adj_y, adj_x = i + dy, j + dx
                if is_valid(adj_y, adj_x):
                    if classroom[adj_y][adj_x] in fav_friends[classroom[i][j]]:
                        fav_cnt += 1

            satisfaction_score += pow(10, fav_cnt - 1) if fav_cnt >= 1 else 0

    return satisfaction_score


solution()