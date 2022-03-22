import math
from collections import defaultdict
import heapq


def solution(n, start, end, roads, traps):
    traps = list(set(traps))
    graph = make_graph(n, roads)
    dist = dijkstra(n, start, end, graph, traps)
    return dist


def make_graph(n, roads):
    graph = [[] for _ in range(n + 1)]

    for [from_, _to, weight] in roads:
        graph[from_].append([_to, weight, True])
        graph[_to].append([from_, weight, False])

    return graph


def is_trapped(traps, state, x):
    if x in traps:
        idx = traps.index(x)
        return state & (1 << idx) != 0
    else:
        return False


def dijkstra(n, start, end, graph, traps):
    dist = defaultdict(lambda: [math.inf if i != start else 0 for i in range(n + 1)])
    pq = [[0, start, 0]]
    min_dist = math.inf

    while len(pq) > 0:
        [d, now_node, state] = heapq.heappop(pq)
        is_now_trapped = is_trapped(traps, state, now_node)

        for [adj, weight, direction] in graph[now_node]:
            is_adj_trapped = is_trapped(traps, state, adj)

            now_direction = is_adj_trapped == is_now_trapped

            if direction == now_direction:
                if adj in traps:
                    new_state = (state ^ (1 << traps.index(adj)))
                else:
                    new_state = state

                if dist[new_state][adj] > d + weight:
                    dist[new_state][adj] = d + weight

                    if adj == end:
                        min_dist = min(min_dist, dist[new_state][adj])

                    heapq.heappush(pq, [dist[new_state][adj], adj, new_state])

    return min_dist


n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]

print(solution(n, start, end, roads, traps))