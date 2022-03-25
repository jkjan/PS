from collections import deque


INF = 100 * 100 + 1
deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(rows, columns, queries):
    answer = []
    board = get_board(rows, columns)
    for y1, x1, y2, x2 in queries:
        min_rotated = r(y1-1, x1-1, y2-1, x2-1, board)
        answer.append(min_rotated)
    return answer


def get_board(rows, columns):
    n = 1
    board = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i][j] = n
            n += 1
    return board


def rotate(y1, x1, y2, x2, do):
    ny, nx = y1, x1
    lens = [x2 - x1, y2 - y1]

    for i in range(4):
        for j in range(lens[i % 2]):
            do(ny, nx)
            ny, nx = ny + deltas[i][0], nx + deltas[i][1]


def r(y1, x1, y2, x2, board):
    def put_in_queue(y, x):
        nonlocal min_rotated
        min_rotated = min(min_rotated, board[y][x])
        q.append(board[y][x])

    def pop_from_queue(y, x):
        board[y][x] = q.popleft()

    q = deque()
    min_rotated = INF
    rotate(y1, x1, y2, x2, put_in_queue)
    q.appendleft(q.pop())
    rotate(y1, x1, y2, x2, pop_from_queue)

    return min_rotated


rows = 3
columns = 3
queries =[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
print(solution(rows, columns, queries))