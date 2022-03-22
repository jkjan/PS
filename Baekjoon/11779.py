import sys
import heapq

INF = 100_000 * (1000 - 1) + 1


def solution():
    n, graph, s, e = get_input()
    min_cost, num_city, path = dijkstra(n, s, e, graph)

    sys.stdout.write("%d\n" % min_cost)
    sys.stdout.write("%d\n" % num_city)

    for p in path:
        sys.stdout.write("%d " % (p + 1))


def get_input():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    graph = [{} for _ in range(n)]

    for i in range(m):
        from_, _to, cost = map(int, sys.stdin.readline().split())
        from_ -= 1
        _to -= 1
        graph[from_][_to] = min(cost, (graph[from_][_to] if _to in graph[from_].keys() else INF))

    for i in range(n):
        graph[i] = [(k, v) for k, v in graph[i].items()]

    s, e = map(int, sys.stdin.readline().split())

    return n, graph, s - 1, e - 1


def dijkstra(n, s, e, graph):
    dist = [INF for _ in range(n)]
    dist[s] = 0
    will_visit = [(0, s)]
    path = [[s] for _ in range(n)]

    while len(will_visit) > 0:
        mid_dist, mid = heapq.heappop(will_visit)

        for adj, w in graph[mid]:
            new_dist = mid_dist + w

            if dist[adj] > new_dist:
                dist[adj] = new_dist
                path[adj] = path[mid] + [adj]
                heapq.heappush(will_visit, (new_dist, adj))

    return dist[e], len(path[e]), path[e]


solution()