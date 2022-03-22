# https://programmers.co.kr/learn/courses/30/lessons/72413
# naive
import heapq
import math


def solution(n, s, a, b, fares):
    adj_matrix = get_adj_matrix(n, fares)
    floyd(adj_matrix)
    answer = min([try_here(s, i, a, b, adj_matrix) for i in range(1, n + 1)])
    return answer


def get_adj_matrix(n, fares):
    adj_matrix = [[math.inf for i in range(n + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        adj_matrix[i][i] = 0
    for [c, d, f] in fares:
        adj_matrix[c][d] = f
        adj_matrix[d][c] = f
    return adj_matrix


def floyd(adj_matrix):
    for k in range(1, len(adj_matrix)):
        for i in range(1, len(adj_matrix)):
            for j in range(1, len(adj_matrix)):
                new_dist = adj_matrix[i][k] + adj_matrix[k][j]
                if adj_matrix[i][j] > new_dist:
                    adj_matrix[i][j] = new_dist


def try_here(s, x, a, b, adj_matrix):
    together = adj_matrix[s][x]
    a_dist = adj_matrix[x][a]
    b_dist = adj_matrix[x][b]
    total_cost = together + a_dist + b_dist
    return total_cost


def build_graph(n, fares):
    graph = [[] for i in range(n + 1)]
    for [c, d, f] in fares:
        graph[c].append([d, f])
        graph[d].append([c, f])
    return graph


def dijkstra(graph, start):
    will_visit = [(0, start)]
    dist = [math.inf for i in range(len(graph))]
    dist[start] = 0
    while 0 < len(will_visit):
        so_far, now_visit = heapq.heappop(will_visit)
        for [adj, w] in graph[now_visit]:
            new_dist = so_far + w
            if dist[adj] > new_dist:
                dist[adj] = new_dist
                heapq.heappush(will_visit, (dist[adj], adj))
    return dist


n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(solution(n, s, a, b, fares))