from copy import deepcopy


board = [[[0]]]
score = 0

GREEN = 0
BLUE = 1


def solution():
    blocks = get_input()
    init_board()
    put_blocks(blocks)
    cnt = count_tiles()

    print(score)
    print(cnt)


def get_input():
    N = int(input())
    blocks = [list(map(int, input().split())) for _ in range(N)]
    return blocks


def init_board():
    global board
    board = [[[0 for _ in range(4)] for _ in range(6)] for _ in range(2)]


def count_tiles():
    tiles = 0

    for color in [GREEN, BLUE]:
        for r in range(2, 6):
            tiles += sum(board[color][r])

    return tiles


def get_block(t):
    if t == 1:
        return [[1]]
    elif t == 2:
        return [[1, 1]]
    else:
        return [[1], [1]]


def put_blocks(blocks):
    for block in blocks:
        put_block(block)


def get_green_blue_block(block):
    [t, x, y] = block

    # 파란색에 넣을 블록은 x값이 3-x 임 (단, t=3일 때 제외)
    blue_y = 3 - x

    # 파란색에 넣을 블록의 모양이 달라짐
    if t == 1:
        blue_t = 1
    elif t == 2:
        blue_t = 3
    else:
        # t=3 이면 세로로 긴 블록인데, 이건 기준점이 위에 있음
        # 파란색에 가면 기준이 오른쪽에 있는 가로로 긴 블록이 되므로 y 값에서 1 빼줌
        blue_y -= 1
        blue_t = 2

    green_block, green_y = get_block(t), y
    blue_block, blue_y = get_block(blue_t), blue_y
    block = [green_block, blue_block]
    y = [green_y, blue_y]

    return block, y


def put_block(block):
    global score
    block, y = get_green_blue_block(block)

    for color in [GREEN, BLUE]:
        # 블록을 떨어뜨림
        row = fall_block(block[color], y[color], color)

        # 블록이 최종적으로 도달한 행에 한해서 지워질 행을 얻음
        erased = get_erased(row, color)

        # 점수 추가
        score += len(erased)

        # 지워진 행만큼 내림
        get_down(erased, color)

        # 맨 위의 특별한 행에 대해 작업해줌
        erased = get_special_erased(color)

        # 지워진 행만큼 내림
        get_down(erased, color)


def fall_block(block, y, color):
    x = 1
    flag = False

    # 블록이 땅이나 다른 블록에 걸릴 때까지 내림
    while x < 6:
        for i in range(len(block[-1])):
            if board[color][x][y+i] == 1:
                flag = True
                break

        if flag:
            break

        x += 1

    x -= 1

    # 블록이 최종적으로 도달한 행
    row = set()
    for i in range(len(block)):
        for j in range(len(block[0])):
            board[color][x-i][y+j] = 1
            row.add(x-i)

    return row


def get_erased(row, color):
    # 모든 열이 채워진 (행의 합이 4인) 행
    erased = []
    for r in row:
        if sum(board[color][r]) == 4:
            erased.append(r)
    return erased


def get_down(erased, color):
    if len(erased) == 0:
        return

    bottom = min(erased) - 1
    to_move = []

    # 0부터 bottom 까지를 옮김
    for r in range(bottom + 1):
        to_move.append(board[color][r])

    # 지워진 행 개수만큼 내려서 위의 to_move 를 그대로 복사
    for i, r in enumerate(range(len(erased), bottom + len(erased) + 1)):
        board[color][r] = deepcopy(to_move[i])

    # 위에는 0으로 채움
    for r in range(len(erased)):
        board[color][r] = [0, 0, 0, 0]


def get_special_erased(color):
    special_row = [0, 1]

    # 특수 행에 타일이 들어있는 행의 개수를 셈
    special_filled = sum([sum(board[color][s]) > 0 for s in special_row])

    # 아래에서 그 행의 개수만큼을 지움
    erased = list(range(5, 5 - special_filled, -1))
    return erased


solution()