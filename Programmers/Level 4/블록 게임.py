from collections import Counter, defaultdict


def solution(board):
    global N
    N = len(board)
    pos = init_pos(board)
    answer = 0

    while True:
        popped = pop_blocks(board, pos)
        if popped == 0:
            break
        answer += popped

    return answer


def init_pos(board):
    pos = defaultdict(lambda: [])
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                pos[board[i][j]].append((i, j))
    return pos


def get_blanks(blocks):
    counts = [sorted(Counter([block[i] for block in blocks]).items(), key=lambda x: -x[1]) for i in range(2)]
    target_idx = [i for i in range(2) if counts[i][0][1] == 3][0]

    axis = counts[target_idx][1][0]
    counter_idx = (target_idx + 1) % 2
    counter_axis = [counts[counter_idx][i][0] for i in range(3) if counts[counter_idx][i][1] == 1]

    blanks = []
    for c in counter_axis:
        temp = [0, 0]
        temp[target_idx] = axis
        temp[counter_idx] = c
        blanks.append(temp)

    return blanks


def is_fillable(board, blanks):
    for blank in blanks:
        for i in range(blank[0], -1, -1):
            if board[i][blank[1]] != 0:
                return False
    return True


def pop_blocks(board, pos):
    cnt = 0
    popped = []

    for n, p in pos.items():
        blanks = get_blanks(p)

        if is_fillable(board, blanks):
            cnt += 1
            for py, px in p:
                board[py][px] = 0
            popped.append(n)

    for p in popped:
        pos.pop(p)

    return cnt

# N = 5
# blocks = [(N - 1, 0), (N - 1, 1), (N - 1, 2), (N - 2, 0)]
# get_blanks(blocks)

board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
print(solution(board))