import heapq
import sys

N = 0
parents = []


def solution():
    edge_queue = get_edge_queue()
    init_parents()
    spanning_tree_weight = kruskal(edge_queue)
    sys.stdout.write("%d" % spanning_tree_weight)


def get_edge_queue():
    global N
    V, E = map(int, sys.stdin.readline().split())
    edge_q = []

    for i in range(E):
        A, B, C = map(int, sys.stdin.readline().split())
        edge_q.append([C, A, B])

    heapq.heapify(edge_q)

    return edge_q


def kruskal(edge_q):
    spanning_tree_weight = 0

    cnt = 0
    while cnt != N - 1:
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
    parents[b_parent] = a_parent


def find(x):
    while parents[x] != x:
        x = parents[x]
    return x


def is_in_same_group(a, b):
    return find(a) == find(b)


solution()