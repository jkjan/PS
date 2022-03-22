import sys
from collections import deque
import random


def solution():
    K, M, adj_matrix = get_input()
    K_dist_matrix = m_pow(adj_matrix, K)

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        sys.stdout.write("%s\n" % ("death" if K_dist_matrix[a][b] else "life"))


def zeros_like(N):
    zeros = [[False for i in range(N + 1)] for j in range(N + 1)]
    return zeros


def get_input():
    N, K, M = map(int, sys.stdin.readline().split())
    adj_matrix = zeros_like(N)
    for i in range(1, N + 1):
        a, b = map(int, sys.stdin.readline().split())
        adj_matrix[i][a] = True
        adj_matrix[i][b] = True
    return K, M, adj_matrix


def m_pow(matrix, power):
    if power == 1:
        return matrix
    else:
        m = power // 2
        half = m_pow(matrix, m)
        powered = dot(half, half)
        if power % 2 == 1:
            powered = dot(powered, matrix)
        return powered


def dot(matrix_a, matrix_b):
    N = len(matrix_a) - 1
    result = zeros_like(N)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                result[i][j] |= (matrix_a[i][k] & matrix_b[k][j])
    return result


solution()