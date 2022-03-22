import heapq
import sys


def solution():
    edge_queue = get_edge_queue()
    init_parents()
    spanning_tree_weight = kruskal(edge_queue)
    sys.stdout.write("%d" % spanning_tree_weight)


def get_edge_queue():
    global N
    N, M = map(int, sys.stdin.readline().split())
    edge_q = []

    for i in range(M):
        A, B, C = map(int, sys.stdin.readline().split())
        edge_q.append([C, A, B])

    heapq.heapify(edge_q)

    return edge_q


def kruskal(edge_q):
    spanning_tree_weight = 0

    cnt = 0
    while cnt != N - 2:
        [weight, a, b] = heapq.heappop(edge_q)
        if not is_in_same_group(a, b):
            spanning_tree_weight += weight
            cnt += 1
            union(a, b)

    return spanning_tree_weight


def init_parents():
    global parents
    parents = [i for i in range(N + 1)]


def union(a, b):
    a_parent = find(a)
    b_parent = find(b)
    parents[a_parent] = b_parent


def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def is_in_same_group(a, b):
    return find(a) == find(b)


solution()