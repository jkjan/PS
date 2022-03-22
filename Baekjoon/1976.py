import sys


def solution():
    N, adj_matrix, path = get_input()
    floyd(N, adj_matrix)
    answer = is_possible(adj_matrix, path)
    sys.stdout.write("%s" % ("YES" if answer else "NO"))


def floyd(N, adj_matrix):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    adj_matrix[i][i] = True
                if adj_matrix[i][k] and adj_matrix[k][j]:
                    adj_matrix[i][j] = True
                    adj_matrix[j][i] = True


def get_input():
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    adj_matrix = [list(map(lambda x: bool(int(x)), sys.stdin.readline().split())) for _ in range(N)]
    path = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    return N, adj_matrix, path


def is_possible(adj_matrix, path):
    for i in range(len(path) - 1):
        if not adj_matrix[path[i]][path[i + 1]]:
            return False
    return True


solution()