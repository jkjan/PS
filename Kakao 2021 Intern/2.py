from collections import deque


def solution(places):
    answer = []
    for waiting_room in places:
        is_room_okay = check_waiting_room(waiting_room)
        answer.append(is_room_okay)
    return answer

def get_participants(waiting_room):
    participants = []
    for i in range(5):
        for j in range(5):
            if waiting_room[i][j] == 'P':
                participants.append((i, j))
    return participants

def check_waiting_room(waiting_room):
    participants = get_participants(waiting_room)
    for (part_y, part_x) in participants:
        is_person_okay = check_participant(part_y, part_x, waiting_room)
        if not is_person_okay:
            return 0
    return 1

def is_valid(i):
    return 0 <= i < 5

def check_participant(start_y, start_x, waiting_room):
    will_visit = deque()
    will_visit.append([start_y, start_x])
    visited = [[False for i in range(5)] for j in range(5)]
    visited[start_y][start_x] = True
    dist_arr = [[-1 for i in range(5)] for i in range(5)]
    dist_arr[start_y][start_x] = 0
    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while 0 < len(will_visit):
        [now_y, now_x] = will_visit.pop()

        for (dy, dx) in deltas:
            then_y, then_x = now_y + dy, now_x + dx
            if is_valid(then_y) and is_valid(then_x) \
                    and not visited[then_y][then_x]\
                    and waiting_room[then_y][then_x] != 'X':
                visited[then_y][then_x] = True
                dist_arr[then_y][then_x] = dist_arr[now_y][now_x] + 1

                if dist_arr[then_y][then_x] <= 2 and waiting_room[then_y][then_x] == 'P':
                    return False
                will_visit.append([then_y, then_x])

    return True


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))