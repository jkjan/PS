from collections import defaultdict

# 방향 d가 1, 4면 역행 / 2, 3이면 순행
delta = [0, -1, 1, 1, -1]

# 인덱스에 의미 부여
R = 0
C = 1
S = 2
D = 3
Z = 4

# 전역변수 초기화
score = 0
soil = [[1]]
is_alive = []
sharks = [[1]]
rc = []


# 메인 로직
def solution():
    get_input()

    # 낚시왕이 왼쪽에서 오른쪽으로 이동하며 상어 낚시
    for n in range(1, rc[C] + 1):
        fish_shark(n)
        move_sharks()


# 입력 받기
def get_input():
    global sharks, rc, is_alive, soil
    r, c, M = map(int, input().split())
    rc = [r, c]
    sharks = [list(map(int, input().split())) for _ in range(M)]
    field = [[-1 for _ in range(c + 1)] for _ in range(r + 1)]

    for i in range(len(sharks)):
        r = sharks[i][R]
        c = sharks[i][C]

        # 이동은 주기성을 띄므로 속도를 상어가 속한 축이 n일 때 2(n - 1)로 나눈 나머지로 바꿈
        # 이 작업이 없으면 무조건 시간초과 뜸 (s값 최대값이 1000)
        to_move = (sharks[i][D] / 2) > 1
        sharks[i][S] %= 2 * (rc[to_move] - 1)

        # 필드에 상어 id 초기화
        field[r][c] = i

    # 처음에 모든 상어는 살아있음
    is_alive = [True for _ in range(M)]


def shift_direction(d):
    # 2->1, 1->2, 3->4, 4->3
    return (d + 1) if (d % 2) else (d - 1)


# 상어 이동
def move_sharks():
    # {(상어 위치): [상어 id들]}
    sharks_dict = defaultdict(lambda: [])

    # 상어 움직이기
    for i in range(len(sharks)):
        move_shark(i, sharks_dict)

    # 승자 독식
    for k, v in sharks_dict.items():
        # 제일 큰 상어 id
        winner = max(v, key=lambda x: sharks[x][Z])

        # 필드에 승자만 표시하고, 상어가 살았다고 표시
        soil[k[R]][k[C]] = winner
        is_alive[winner] = True


# 상어 한 마리 이동
def move_shark(i, sharks_dict):
    # 죽은 상어는 움직일 수 없음
    if not is_alive[i]:
        return

    shark = sharks[i]

    # 상어가 위치한 축
    to_move = (shark[D] / 2) > 1

    # 상어의 속력: 상어가 이동해야 할 거리
    s = shark[S]

    # 상어가 이동할 예정이므로 필드에 -1 표기
    soil[shark[R]][shark[C]] = -1

    while True:
        # 상어가 바라보는 벽
        end = 1 if delta[shark[D]] == -1 else rc[to_move]

        # 벽까지의 거리와 현재 가야할 거리 중 최소값
        k = min(s, abs(end - shark[to_move]))

        # 상어가 k만큼 이동함
        shark[to_move] = shark[to_move] + delta[shark[D]] * k

        # 이동할 거리에서 이동한 거리를 감소
        s -= k

        # 이동할 거리가 아직 남았다면 (벽이라면) 방향 전환
        if s > 0:
            shark[D] = shift_direction(shark[D])
        else:
            break

    # 딕셔너리에 현재 상어 추가
    sharks_dict[(shark[R], shark[C])].append(i)

    # 어차피 제일 큰 상어만 살아남으므로 일단 죽었다고 표시
    is_alive[i] = False


def fish_shark(n):
    global score

    for i in range(1, rc[R] + 1):
        if soil[i][n] != -1:
            # 발견되는 최초의 상어를 낚고 점수 추가
            score += sharks[soil[i][n]][Z]

            # 상어는 더이상 살아있지 않으며, 필드에 존재하지 않게 됨
            is_alive[soil[i][n]] = False
            soil[i][n] = -1
            break


solution()

print(score)