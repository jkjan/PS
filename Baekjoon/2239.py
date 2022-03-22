import sys

ROW = 0
COL = 1
SQR = 2

def solution():
    init_sudoku()
    init_checker()
    dfs(0)


def init_sudoku():
    global sudoku
    sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]


def coord_to_sqr(i, j):
    return (i // 3) * 3 + (j // 3)


def init_checker():
    global checker
    checker = [[[False for _ in range(9 + 1)] for _ in range(9)] for _ in range(3)]

    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                checker[ROW][i][sudoku[i][j]] = True
                checker[COL][j][sudoku[i][j]] = True
                checker[SQR][coord_to_sqr(i, j)][sudoku[i][j]] = True


def dfs(v):
    if v == 81:
        for line in sudoku:
            sys.stdout.write("%s\n" % " ".join(str(_) for _ in line))
        exit(0)

    vi, vj = divmod(v, 9)
    if sudoku[vi][vj] == 0:
        sqr = coord_to_sqr(vi, vj)

        for n in range(1, 10):
            if not checker[ROW][vi][n] and not checker[COL][vj][n] and not checker[SQR][sqr][n]:
                sudoku[vi][vj] = n
                checker[ROW][vi][n] = True
                checker[COL][vj][n] = True
                checker[SQR][sqr][n] = True

                dfs(v + 1)

                sudoku[vi][vj] = 0
                checker[ROW][vi][n] = False
                checker[COL][vj][n] = False
                checker[SQR][sqr][n] = False
    else:
        dfs(v + 1)


solution()