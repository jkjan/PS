import sys

N, M = map(int, sys.stdin.readline().split())

A = [sys.stdin.readline().strip() for i in range(N)]
B = [sys.stdin.readline().strip() for i in range(N)]

D = [[1 for j in range(M)] for i in range(N)]
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            D[i][j] = -1

def get_flipped(i, j):
    flipped = 0
    for ii in range(i - 1, i + 2):
        for jj in range(j - 1, j + 2):
            if 0 <= ii < N and 0 <= jj < M:
                flipped += (D[ii][jj] == -1)
    return flipped - (D[i][j] == -1)

def flip(i, j):
    for ii in range(i - 1, i + 2):
        for jj in range(j - 1, j + 2):
            if 0 <= ii < N and 0 <= jj < M:
                D[ii][jj] = -1 * D[ii][jj]

def get_max_flipped():
    max_flipped = 0
    max_i, max_j = -1, -1
    for i in range(N):
        for j in range(M):
            flipped = get_flipped(i, j)
            if flipped > max_flipped:
                max_i, max_j = i, j
                max_flipped = flipped
    flip(max_i, max_j)
    print("flip", max_i, max_j)
    return max_flipped

def get_min_trial():
    trial = 0
    for i in range(N * M):
        flipped = get_max_flipped()
        print(D)
        if flipped == 0:
            break
        trial += 1
    return trial


print(D)
print(get_min_trial())