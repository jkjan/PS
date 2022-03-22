from collections import defaultdict, deque

START = 0
FINISH = 99


def solution():
    for i in range(10):
        tc()


def tc():
    T, graph = get_input()
    answer = bfs(graph)
    print("#%d %d" % (T, answer))


def get_input():
    T, E = map(int, input().split())
    edges = list(map(int, input().split()))
    graph = defaultdict(lambda: [])
    for i in range(0, len(edges) - 1, 2):
        graph[edges[i]].append(edges[i + 1])
    return T, graph


def bfs(graph):
    will_visit = deque([START])
    visited = set()

    while len(will_visit) > 0:
        now_visit = will_visit.popleft()
        if now_visit == FINISH:
            return 1

        for adj in graph[now_visit]:
            if adj not in visited:
                visited.add(adj)
                will_visit.append(adj)

    return 0


solution()