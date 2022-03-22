import heapq


parents = []

def solution(n, costs):
    edge_queue = make_edge_queue(costs)
    init_parents(n)
    min_cost = kruskal(n, edge_queue)
    return min_cost


def make_edge_queue(costs):
    edge_queue = []
    for [a, b, cost] in costs:
        heapq.heappush(edge_queue, [cost, a, b])
    return edge_queue


def kruskal(n, edge_queue):
    cnt = 0
    min_cost = 0
    while cnt < n - 1:
        [cost, a, b] = heapq.heappop(edge_queue)

        if not is_in_same_group(a, b):
            union(a, b)
            min_cost += cost
            cnt += 1
    return min_cost


def init_parents(n):
    global parents
    parents = [i for i in range(n + 1)]


def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)
    parents[b] = a

def is_in_same_group(a, b):
    return find(a) == find(b)
