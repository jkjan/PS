import heapq
import math
from collections import defaultdict


def solution(n, start, end, roads, traps):
    graph = make_graph(n, roads)
    traps = {traps[i]: i for i in range(len(traps))}
    dist = dijkstra(start, graph, traps)
    return min(dist[end])


def make_graph(n, roads):
    graph = [defaultdict(lambda: 3001) for _ in range(n + 1)]
    for P, Q, S in roads:
        graph[P][Q] = min(graph[P][Q], S)
        graph[Q][-P] = min(graph[Q][-P], S)
    return graph


def dijkstra(start, graph, traps):
    dist = [[math.inf for _ in range(2 ** 10)] for _ in range(len(graph))]
    dist[start][0] = 0
    pq = [(0, start, 0)]

    while len(pq) > 0:
        now_dist, now_node, now_status = heapq.heappop(pq)

        for adj, adj_dist in graph[now_node].items():
            direction = True if adj > 0 else False
            adj = abs(adj)

            adj_trapped = 0 if adj not in traps.keys() else ((now_status & (1 << traps[adj])) != 0)
            now_trapped = 0 if now_node not in traps.keys() else ((now_status & (1 << traps[now_node])) != 0)
            edge_reversed = adj_trapped != now_trapped

            if direction != edge_reversed:
                next_status = now_status

                if adj in traps:
                    next_status = now_status ^ (1 << traps[adj])

                new_dist = now_dist + adj_dist
                if dist[adj][next_status] > new_dist:
                    dist[adj][next_status] = new_dist
                    heapq.heappush(pq, (new_dist, adj, next_status))

    return dist


n = 1000
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]

print(solution(n, start, end, roads, traps))