from collections import Counter
import parameters as pt


def select_scenario(scenario):
    if scenario == 1:
        pt.N = 5
        pt.TRUCKS = 5
    else:
        pt.N = 60
        pt.TRUCKS = 10


def pos_to_id(i, j):
    return j * pt.N + pt.N - 1 - i


def id_to_pos(id):
    return pt.N - 1 - (id % pt.N), id // pt.N


def init_rental():
    global rental
    rental = [[0 for _ in range(pt.N)] for _ in range(pt.N)]


def renew_rental(locations_info):
    for location_info in locations_info:
        y, x = id_to_pos(location_info["id"])
        rental[y][x] = location_info["located_bikes_count"]


def get_n_hot_places(history, n):
    rent_return_count = [[Counter(), Counter()] for _ in range(3)]

    for h in history:
        for time in h.keys():
            pattern = int(time) // pt.PATTERN_INTERVAL
            for method in [pt.RENT, pt.RETURN]:
                for req in h[time]:
                    rent_return_count[pattern][method][req[method]] += 1

    hot_places = [[[], []] for _ in range(3)]
    for pattern in range(3):
        for method in [pt.RENT, pt.RETURN]:
            hot_places[pattern][method] = rent_return_count[pattern][method].most_common(n)

    return hot_places


def print_rental():
    for i in range(pt.N):
        for j in range(pt.N):
            print(rental[i][j], end=' ')
        print()


def find_nearest_spot(truck_pos, hot_places, pattern, method, visited):
    min_dist = pt.N + pt.N + 1
    nearest_spot = (-1, -1)
    truck_y, truck_x = id_to_pos(truck_pos)

    for spot_id, bikes in hot_places[pattern][method]:
        if visited[spot_id]:
            continue

        spot_y, spot_x = id_to_pos(spot_id)
        dist_here = abs(truck_y - spot_y) + abs(truck_x - spot_x)

        if min_dist > dist_here:
            min_dist = dist_here
            nearest_spot = (spot_y, spot_x)

    nearest_id = pos_to_id(*nearest_spot)
    visited[nearest_id] = True
    return nearest_spot


def add_to_truck_command_queue(truck_pos, pick_up, put):
    queue = []
    t_y, t_x = id_to_pos(truck_pos)
    pu_y, pu_x = pick_up
    put_y, put_x = put
    to_move = rental[pu_y][pu_x] // 2

    move(t_y, t_x, pu_y, pu_x, queue)

    for bike in range(to_move):
        queue.append(5)

    move(pu_y, pu_x, put_y, put_x, queue)

    for bike in range(to_move):
        queue.append(6)

    return queue


def move(from_y, from_x, to_y, to_x, queue):
    dy = to_y - from_y
    move_(dy, queue, 1, 3)

    dx = to_x - from_x
    move_(dx, queue, 4, 2)


def move_(d, queue, backward, forward):
    if d < 0:
        to_add = backward
    elif d > 0:
        to_add = forward
    else:
        return

    d = abs(d)
    for i in range(d):
        queue.append(to_add)


#
# def find_nearest_spot(truck_pos, method, visited):
#     will_visit = deque([truck_pos])
#     visited[truck_pos[0]][truck_pos[1]] = True
#
#     while len(will_visit) > 0:
#         now_y, now_x = will_visit.popleft()
#
#         if rental[now_y][now_x][method]:
#             return now_y, now_x
#
#         for dy, dx in deltas:
#             adj_y, adj_x = now_y + dy, now_x + dx
#             if not is_valid(adj_y, adj_x):
#                 continue
#             if visited[adj_y][adj_x]:
#                 continue
#
#             will_visit.append((adj_y, adj_x))
#             visited[adj_y][adj_x] = True
#
#
#
#
# def is_valid(i, j):
#     return 0 <= i < N and 0 <= j < N