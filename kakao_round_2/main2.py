import requests
import json
from collections import defaultdict
import random

BASE_URL = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
AUTHORIZATION = ''
TRUCKS_COUNT = 10

n = 60
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 이동 방향 명령어
direction_convert = dict()
direction_convert[(-1, 0)] = 1
direction_convert[(0, 1)] = 2
direction_convert[(1, 0)] = 3
direction_convert[(0, -1)] = 4

locations = [[3 for _ in range(n)] for _ in range(n)]
# 위치 x, y, 가지고 있는 바이크 수
trucks = defaultdict(lambda: [n - 1, 0, 0])
# 먼 곳으로 이동하거나 바이크를 여러 개 담는 경우 명령이 사라지지 않게 하기 위해 큐 형식으로 동작
# 큐의 원소가 10개 이하이면 새롭게 명령어 세트를 삽입
trucks_cmd_list = [[] for _ in range(TRUCKS_COUNT)]


def convert_pos(idx):
    x = (n - 1) - (idx % n)
    y = idx // n

    return x, y


def startAPI(question_num):
    global AUTHORIZATION
    response = requests.post(BASE_URL + '/start',
                             headers={'X-Auth-Token': 'a77b51b2c1ac954eb34fa5ba6c0ae39b',
                                      'Content-Type': 'application/json'},
                             data=json.dumps({'problem': question_num})).json()
    AUTHORIZATION = response['auth_key']


def locationsAPI():
    response = requests.get(BASE_URL + '/locations',
                            headers={'Authorization': AUTHORIZATION,
                                     'Content-Type': 'application/json'}).json()
    for i in response['locations']:
        idx = i['id']
        located_bikes_count = i['located_bikes_count']
        x, y = convert_pos(idx)
        locations[x][y] = located_bikes_count


def trucksAPI():
    response = requests.get(BASE_URL + '/trucks',
                            headers={'Authorization': AUTHORIZATION,
                                     'Content-Type': 'application/json'}).json()
    for i in response['trucks']:
        id = i['id']
        location_id = i['location_id']
        loaded_bikes_count = i['loaded_bikes_count']
        x, y = convert_pos(location_id)
        trucks[id] = [x, y, loaded_bikes_count]


def simulationAPI(data):
    response = requests.put(BASE_URL + '/simulate',
                            headers={'Authorization': AUTHORIZATION,
                                     'Content-Type': 'application/json'},
                            data=json.dumps(data)).json()
    print(json.dumps(response, indent=2))
    return response


def scoreAPI():
    response = requests.get(BASE_URL + '/score',
                            headers={'Authorization': AUTHORIZATION,
                                     'Content-Type': 'application/json'}).json()
    return response['score']


def get_dir(fr, to):
    if to - fr < 0:
        return -1
    elif to - fr > 0:
        return 1
    else:
        return 0


def make_cmd(truck_idx, rental_pos):
    temp_cmd = []
    # 가지고 있는 바이크 개수
    loaded_bike_count = trucks[truck_idx][2]

    # 트럭 위치
    truck_x, truck_y = trucks[truck_idx][:2]
    rental_x, rental_y = rental_pos

    # 리턴 위치에서 렌탈 위치(자전거 하차할 위치)까지 이동
    # 이동 도중 자전거 개수가 0인 자리가 있다면 자전거를 하나 내림
    # 이동 도중 자전거 개수가 3개 초과인 자리가 있다면 자전거를 절반만큼 올림
    # 상하 위치 계산
    d = (get_dir(truck_x, rental_x), 0)
    now_x, now_y = truck_x, truck_y
    for _ in range(abs(truck_x - rental_x)):
        temp_cmd.append(direction_convert[d])
        now_x, now_y = now_x + d[0], now_y + d[1]
        if loaded_bike_count and locations[now_x][now_y] <= 0:
            temp_cmd += [6]
            loaded_bike_count -= 1
            locations[now_x][now_y] += 1
        elif locations[now_x][now_y] > 3:
            for _ in range(locations[now_x][now_y] // 2):
                temp_cmd += [5]
                loaded_bike_count += 1
                locations[now_x][now_y] -= 1

    # 좌우 위치 계산
    d = (0, get_dir(truck_y, rental_y))
    for _ in range(abs(truck_y - rental_y)):
        temp_cmd.append(direction_convert[d])
        now_x, now_y = now_x + d[0], now_y + d[1]
        if loaded_bike_count and locations[now_x][now_y] <= 0:
            temp_cmd += [6]
            loaded_bike_count -= 1
            locations[now_x][now_y] += 1
        elif locations[now_x][now_y] > 3:
            for _ in range(locations[now_x][now_y] // 2):
                temp_cmd += [5]
                loaded_bike_count += 1
                locations[now_x][now_y] -= 1

    # 렌탈 위치 도착하면 가지고 있는 모든 바이크 하차
    temp_cmd += [6] * loaded_bike_count

    trucks_cmd_list[truck_idx] += temp_cmd


def get_rental_spots():
    result = []

    for i in range(n):
        for j in range(n):
            if locations[i][j] <= 0:
                result.append((i, j))

    random.shuffle(result)
    return result[:TRUCKS_COUNT]


startAPI(2)
for t in range(720):
    # 자전거 및 트럭 설정
    locationsAPI()
    trucksAPI()

    rental_spots = get_rental_spots()

    data = dict()
    data['commands'] = []

    # 나머지 트럭들에 명령어 부여
    for idx in range(len(rental_spots)):
        truck_cmd = dict()
        if len(trucks_cmd_list[idx]) < 10:
            make_cmd(idx, rental_spots[idx])
        truck_cmd['command'] = trucks_cmd_list[idx][:10]
        truck_cmd['truck_id'] = idx
        del trucks_cmd_list[idx][:10]
        data['commands'].append(truck_cmd)

    simulationAPI(data)

print(scoreAPI())