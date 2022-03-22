# https://programmers.co.kr/learn/courses/30/lessons/49189
import math
from collections import deque


def solution(n, edge):
    graph = build_graph(n, edge)
    return bfs(n, graph)


def bfs(n, graph):
    will_visit = deque([1])
    visited = [False for i in range(n + 1)]
    dist = [math.inf for i in range(n + 1)]
    dist[1] = 0
    visited[1] = True

    while 0 < len(will_visit):
        now_visit = will_visit.popleft()
        for adj in graph[now_visit]:
            if not visited[adj]:
                dist[adj] = dist[now_visit] + 1
                visited[adj] = True
                will_visit.append(adj)

    furthest_node = max(dist[1:])
    return dist[1:].count(furthest_node)


def build_graph(n, edge):
    graph = [[] for i in range(n + 1)]
    for [a, b] in edge:
        graph[a].append(b)
        graph[b].append(a)
    return graph


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n, vertex))