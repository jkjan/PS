def solution():
    N, L, field = get_input()

    # 검사해볼 모든 길
    roads = get_roads(N, field)
    cnt = 0

    # 모든 길에 대해서 가능 여부 검사
    for road in roads:
        cnt += is_possible(N, L, road)

    print(cnt)


def get_roads(N, field):
    roads = []

    # 행 길 추가
    for i in range(N):
        roads.append(field[i])

    # 열 길 추가
    for j in range(N):
        col = []
        for i in range(N):
            col.append(field[i][j])
        roads.append(col)

    return roads


def get_input():
    N, L = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    return N, L, field


def is_possible(N, L, road):
    # 경사로가 놓인 부분은 음수, 절대값은 높이 그대로
    i = 0
    while i < N - 1:
        if abs(abs(road[i]) - road[i + 1]) > 1:
            # 높이 차가 1이 넘음
            return False

        elif abs(road[i]) - road[i + 1] == 1:
            # 자신보다 한 칸 밑을 만남
            # 내려가는 경사로 설치
            next_i = put_slide(i + 1, N, L, road)
            if next_i == -1:
                return False
            else:
                # 경사로 끝 칸으로
                i = next_i

        elif abs(road[i]) - road[i + 1] == -1:
            # 자기보다 한 칸 위를 만남
            # L-1만큼 뒤로 후진
            back = i - (L - 1)

            # 후진했더니 범위 벗어나거나 이미 경사로 설치된 곳이면 불가능
            if not (0 <= back < N):
                return False
            if road[back] < 0:
                return False

            # 올라가는 경사로 설치
            next_i = put_slide(back, N, L, road)
            if next_i == -1:
                return False
            else:
                # 경사로 설치하고 다음 칸으로
                i = next_i + 1

        else:
            # 평지
            i += 1

    # 위 과정에서 중단되지 않으면 그 길은 갈 수 있는 길임
    return True


def put_slide(i, N, L, road):
    slide_len = 0
    start_height = road[i]

    while i < N and slide_len < L:
        # 경사로를 놓을 구간의 길이가 일정하지 않을 경우
        if road[i] != start_height:
            return -1

        # 경사로를 놓음
        road[i] *= -1
        slide_len += 1
        i += 1

    # 경사로를 다 놓음
    if slide_len == L:
        return i - 1
    else:
        # 경사로를 다 못 놓은 채 끝남
        return -1


solution()